from main.models import TrendEmotion
from utils.apis.youtube import get_relevant_comments
from utils.apis.twitter import get_relevant_tweets
import pickle
from datasets import load_dataset
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


tokenizer_1 = None
tokenizer_2 = None


def get_tokenizer_1():
    global tokenizer_1
    if tokenizer_1:
        return tokenizer_1

    dataset = load_dataset("mteb/tweet_sentiment_extraction")
    train = dataset['train']
    texts = [x['text'] for x in train]

    tokenizer_1 = Tokenizer(num_words=1000, oov_token='<UNK>')
    tokenizer_1.fit_on_texts(texts)

    with open('tokenizer_1.pkl', 'wb') as f:
        pickle.dump(tokenizer_1, f)

    return tokenizer_1


def get_tokenizer_2():
    global tokenizer_2
    if tokenizer_2:
        return tokenizer_2

    dataset = load_dataset("SetFit/emotion")
    train = dataset['train']
    texts = [x['text'] for x in train]

    tokenizer_2 = Tokenizer(num_words=1000, oov_token='<UNK>')
    tokenizer_2.fit_on_texts(texts)

    with open('tokenizer_2.pkl', 'wb') as f:
        pickle.dump(tokenizer_2, f)

    return tokenizer_2


def get_sequences(tokenizer, texts, maxlen):
    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, truncating='post',
                           padding='post', maxlen=maxlen)
    return padded


def model_predict(word, video_id):

    tokenizer_1 = get_tokenizer_1()
    tokenizer_2 = get_tokenizer_2()

    texts = []

    if word and not video_id:
        texts = get_relevant_tweets(word)
    elif not word and video_id:
        texts = get_relevant_comments(video_id, 50, [])

    if not texts:
        return None, None, None, None, None, None, None, None, None

    model_1 = keras.models.load_model('trained_model_1.h5')
    model_2 = keras.models.load_model('trained_model_2.h5')

    seq_1 = get_sequences(tokenizer_1, texts, 35)
    seq_2 = get_sequences(tokenizer_2, texts, 50)

    result_1 = model_1.predict(seq_1, verbose=0)
    result_2 = model_2.predict(seq_2, verbose=0)

    negative, neutral, positive = result_1.sum(axis=0)
    sadness, fear, love, surprise, anger, joy = result_2.sum(axis=0)

    sum_1 = negative + neutral + positive
    total_negative, total_neutral, total_positive = negative / \
        sum_1, neutral/sum_1, positive/sum_1

    sum_2 = sadness + fear + love + surprise + anger + joy
    total_sadness, total_fear, total_love, total_surprise, total_anger, total_joy = sadness / \
        sum_2, fear/sum_2, love/sum_2, surprise/sum_2, anger/sum_2, joy/sum_2

    return total_negative, total_neutral, total_positive, total_sadness, total_fear, total_love, total_surprise, total_anger, total_joy


def load_trend_emotions(word, video_id):

    if word and not video_id:
        negative, neutral, positive, sadness, fear, love, surprise, anger, joy = model_predict(
            word, None)

        if not negative or not neutral or not positive or not sadness or not fear or not love or not surprise or not anger or not joy:
            return None

        if TrendEmotion.objects.filter(word=word).exists():
            TrendEmotion.objects.filter(word=word).delete()

        te = TrendEmotion(word=word,
                          negative_emotion=negative,
                          neutral_emotion=neutral,
                          positive_emotion=positive,
                          sadness_emotion=sadness,
                          fear_emotion=fear,
                          love_emotion=love,
                          surprise_emotion=surprise,
                          anger_emotion=anger,
                          joy_emotion=joy)
        te.save()

    elif not word and video_id:
        negative, neutral, positive, sadness, fear, love, surprise, anger, joy = model_predict(
            None, video_id)

        if not negative or not neutral or not positive or not sadness or not fear or not love or not surprise or not anger or not joy:
            return None

        if TrendEmotion.objects.filter(video_id=video_id).exists():
            TrendEmotion.objects.filter(video_id=video_id).delete()

        te = TrendEmotion(video_id=video_id,
                          negative_emotion=negative,
                          neutral_emotion=neutral,
                          positive_emotion=positive,
                          sadness_emotion=sadness,
                          fear_emotion=fear,
                          love_emotion=love,
                          surprise_emotion=surprise,
                          anger_emotion=anger,
                          joy_emotion=joy)
        te.save()
