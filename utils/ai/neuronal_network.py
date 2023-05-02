import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from datasets import load_dataset
import pickle
from utils.apis.twitter import get_relevant_tweets
from utils.apis.youtube import get_relevant_comments
from main.models import TrendEmotion

tokenizer_1 = None
tokenizer_2 = None

def init_tokenizer_1():
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

def init_tokenizer_2():
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

def get_sequences_1(tokenizer, texts):
    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, truncating='post', padding='post', maxlen=35)
    return padded

def get_sequences_2(tokenizer, texts):
    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, truncating='post', padding='post', maxlen=50)
    return padded

def model_predict(word, video_id):

    global tokenizer_1
    if not tokenizer_1:
        try:
            with open('tokenizer_1.pkl', 'rb') as f:
                tokenizer_1 = pickle.load(f)
        except:
            tokenizer_1 = init_tokenizer_1()

    global tokenizer_2
    if not tokenizer_2:
        try:
            with open('tokenizer_2.pkl', 'rb') as f:
                tokenizer_2 = pickle.load(f)
        except:
            tokenizer_2 = init_tokenizer_2()

    texts = []
    if word != None and video_id == None:
        texts = get_relevant_tweets(word)
    elif word == None and video_id != None:
        texts = get_relevant_comments(video_id, 50)

    if len(texts) == 0:
        return None, None, None, None, None, None, None, None, None
    
    model_1 = keras.models.load_model('trained_model_1.h5')
    model_2 = keras.models.load_model('trained_model_2.h5')

    negative, neutral, positive = 0, 0, 0
    sadness, fear, love, surprise, anger, joy = 0, 0, 0, 0, 0, 0

    for text in texts:
        seq_1 = get_sequences_1(tokenizer_1,[text])
        result_1 = model_1.predict(np.expand_dims(seq_1[0], axis=0), verbose = 0)[0]
        seq_2 = get_sequences_2(tokenizer_2,[text])
        result_2 = model_2.predict(np.expand_dims(seq_2[0], axis=0), verbose = 0)[0]

        negative += result_1[0]
        neutral += result_1[1]
        positive += result_1[2]

        sadness += result_2[0]
        fear += result_2[1]
        love += result_2[2]
        surprise += result_2[3]
        anger += result_2[4]
        joy += result_2[5]
        
    sum_1 = negative + neutral + positive
    total_negative = negative/sum_1
    total_neutral = neutral/sum_1
    total_positive = positive/sum_1

    sum_2 = sadness + fear + love + surprise + anger + joy
    total_sadness = sadness/sum_2
    total_fear = fear/sum_2
    total_love = love/sum_2
    total_surprise = surprise/sum_2
    total_anger = anger/sum_2
    total_joy = joy/sum_2
        
    return total_negative, total_neutral, total_positive, total_sadness, total_fear, total_love, total_surprise, total_anger, total_joy

def load_trend_emotions(word, video_id):
    
    if word != None and video_id == None:
        negative, neutral, positive, sadness, fear, love, surprise, anger, joy = model_predict(word, None)

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

    elif word == None and video_id != None:
        negative, neutral, positive, sadness, fear, love, surprise, anger, joy = model_predict(None, video_id)

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