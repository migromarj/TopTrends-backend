from main.models import TrendEmotion
from utils.apis.youtube import get_relevant_comments
from utils.scraping.twitter import get_relevant_tweets
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow import keras
from keras.datasets import imdb
import numpy as np
import torch
from transformers import BertForSequenceClassification, BertTokenizer
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def get_sequences(tokenizer, texts, maxlen):
    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, truncating='post',
                           padding='post', maxlen=maxlen)
    return padded


def encode_text(text, index, max_words=10000):
    words = text.lower().split()
    encoded = [index.get(word, 2) + 3 for word in words]
    encoded = [i if i < max_words + 3 else 0 for i in encoded]
    return encoded


def vectorize(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results


def preprocess_text(text):
    index = imdb.get_word_index()
    encoded_text = encode_text(text, index)
    vectorized_text = vectorize([encoded_text])
    return vectorized_text


def model_1_predict(texts):

    if not texts:
        return None, None

    model_1 = keras.models.load_model('trained_model_1.h5')

    total_negative, total_positive = 0, 0

    for text in texts:
        preprocessed_text = preprocess_text(text)
        result = model_1.predict(preprocessed_text, verbose=0)
        negative, positive = result[0]
        total_negative += negative
        total_positive += positive

    negative = total_negative / (total_negative + total_positive)
    positive = total_positive / (total_negative + total_positive)

    return negative, positive


def model_2_predict(texts):
    def preprocess_function(examples):
        return tokenizer(examples["text"], truncation=True)

    if not texts:
        return None, None, None, None, None, None

    if not os.path.exists('trained_model_2.pth'):
        return 0.16, 0.16, 0.16, 0.16, 0.16, 0.16

    model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                          num_labels=6,
                                                          state_dict=torch.load('trained_model_2.pth'))
    tokenizer = BertTokenizer.from_pretrained('tokenizer.pth')

    total_sadness, total_joy, total_love, total_anger, total_fear, total_surprise = 0, 0, 0, 0, 0, 0

    for text in texts:
        preprocessed_input = preprocess_function({"text": text})
        input_ids = preprocessed_input["input_ids"]
        attention_mask = preprocessed_input["attention_mask"]
        inputs = {
            "input_ids": torch.tensor([input_ids]),
            "attention_mask": torch.tensor([attention_mask])
        }
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
        sadness, fear, love, surprise, anger, joy = probabilities.tolist()[0]
        total_sadness += sadness
        total_joy += joy
        total_love += love
        total_anger += anger
        total_fear += fear
        total_surprise += surprise

    sum_ = total_sadness + total_joy + total_love + \
        total_anger + total_fear + + total_surprise
    sadness, joy, love, anger, fear, surprise = total_sadness / sum_, total_joy / \
        sum_, total_love / sum_, total_anger / \
        sum_, total_fear / sum_, total_surprise / sum_

    return sadness, joy, love, anger, fear, surprise


def load_trend_emotions(word, video_id):

    if word and not video_id:
        texts = get_relevant_tweets(word)
        negative, positive = model_1_predict(texts)
        sadness, joy, love, anger, fear, surprise = model_2_predict(texts)
        if not negative or not positive or not sadness or not fear or not love or not surprise or not anger or not joy:
            return None

        if TrendEmotion.objects.filter(word=word).exists():
            TrendEmotion.objects.filter(word=word).delete()

        te = TrendEmotion(word=word,
                          negative_emotion=negative,
                          positive_emotion=positive,
                          sadness_emotion=sadness,
                          fear_emotion=fear,
                          love_emotion=love,
                          surprise_emotion=surprise,
                          anger_emotion=anger,
                          joy_emotion=joy)
        te.save()

    elif not word and video_id:
        texts = get_relevant_comments(video_id, 20, [])
        negative, positive = model_1_predict(texts)
        sadness, joy, love, anger, fear, surprise = model_2_predict(texts)

        if not negative or not positive or not sadness or not fear or not love or not surprise or not anger or not joy:
            return None

        if TrendEmotion.objects.filter(video_id=video_id).exists():
            TrendEmotion.objects.filter(video_id=video_id).delete()

        te = TrendEmotion(video_id=video_id,
                          negative_emotion=negative,
                          positive_emotion=positive,
                          sadness_emotion=sadness,
                          fear_emotion=fear,
                          love_emotion=love,
                          surprise_emotion=surprise,
                          anger_emotion=anger,
                          joy_emotion=joy)
        te.save()
