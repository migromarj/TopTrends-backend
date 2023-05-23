import tweepy
from decouple import config
import json
from main.models import Country, TwitterTrend, TwitterCountryTrend
from django.core.exceptions import ObjectDoesNotExist
from googletrans import Translator
import re
import emoji

def api_setup():

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(
        config('TWITTER_API_KEY'), config('TWITTER_SECRET_API_KEY'))
    auth.set_access_token(config('TWITTER_ACCESS_TOKEN'),
                          config('TWITTER_SECRET_ACCESS_TOKEN'))

    # Create API object
    api = tweepy.API(auth)
    return api


def trend_countries():

    api = api_setup()

    # Get countries that have trends
    trends_available = api.available_trends()

    countries = {}
    acronyms = {}
    for t in trends_available:
        if t['country'] not in countries:
            if t['country'] != '':
                countries[t['country']] = t['woeid']
                acronyms[t['country']] = t['countryCode']
            else:
                countries[t['name']] = t['woeid']
                acronyms[t['name']] = 'WW'

    return (countries, acronyms)

# Get trends of a country


def get_country_trends(country_name):

    try:
        country = Country.objects.get(name=country_name)
        woeid = country.woeid

        api = api_setup()

        country_trends = api.get_place_trends(woeid)
        country_trends_json = json.dumps(country_trends)
        country_trends_dict = json.loads(country_trends_json)
        country_trends_list = country_trends_dict[0]['trends'][:25]

        res = []
        for t in country_trends_list:
            res.append((t['name'], t['url'], t['tweet_volume']))

        return res
    except ObjectDoesNotExist:
        return []


def load_country_trends(country_name):

    trends = get_country_trends(country_name)

    if len(trends) > 0:

        country = Country.objects.get(name=country_name)

        if TwitterCountryTrend.objects.filter(country=country).exists():
            TwitterCountryTrend.objects.filter(country=country).delete()

        tct = TwitterCountryTrend(country=country)
        tct.save()

        for t in trends:
            t = TwitterTrend.objects.create(
                name=t[0], url=t[1], tweet_volume=t[2], country_trend=tct)
            t.save()

def translate_to_english(text):
    translator = Translator()
    try:
        return translator.translate(text, dest='en').text
    except:
        return text
    
def clean_text(text):

    no_emoji_text = emoji.get_emoji_regexp().sub(u'', text)
    no_url_text = re.sub(r"http\S+", "", no_emoji_text)
    no_mention_text = re.sub(r"@\S+", "", no_url_text)
    no_hashtag_text = re.sub(r"#\S+", "", no_mention_text)
    english_tweet = translate_to_english(no_hashtag_text)
    clean_tweet = english_tweet.replace(
        '\n', ' ').replace('\r', '').strip()
    
    return clean_tweet

def get_relevant_tweets(trend):

    api = api_setup()

    tweets = api.search_tweets(q=trend, count=20, result_type='popular')

    res = []

    for tweet in tweets:
        if not tweet.retweeted and 'RT @' not in tweet.text:
            
            clean_tweet = clean_text(tweet.text)
            if clean_tweet != '':
                res.append(clean_tweet)

    return res
