from main.models import Country, TwitterTrend, TwitterCountryTrend
from django.core.exceptions import ObjectDoesNotExist
from googletrans import Translator
import re
import emoji
from bs4 import BeautifulSoup
import requests


def trend_countries():

    countries = {
        'Algeria': 'algeria',
        'Argentina': 'argentina',
        'Australia': 'australia',
        'Austria': 'austria',
        'Bahrain': 'bahrain',
        'Belarus': 'belarus',
        'Belgium': 'belgium',
        'Brazil': 'brazil',
        'Canada': 'canada',
        'Chile': 'chile',
        'Colombia': 'colombia',
        'Denmark': 'denmark',
        'Dominican Republic': 'dominican-republic',
        'Ecuador': 'ecuador',
        'Egypt': 'egypt',
        'France': 'france',
        'Germany': 'germany',
        'Ghana': 'ghana',
        'Greece': 'greece',
        'Guatemala': 'guatemala',
        'India': 'india',
        'Indonesia': 'indonesia',
        'Ireland': 'ireland',
        'Israel': 'israel',
        'Italy': 'italy',
        'Japan': 'japan',
        'Jordan': 'jordan',
        'Kenya': 'kenya',
        'Korea': 'korea',
        'Kuwait': 'kuwait',
        'Latvia': 'latvia',
        'Lebanon': 'lebanon',
        'Malaysia': 'malaysia',
        'Mexico': 'mexico',
        'Netherlands': 'netherlands',
        'New Zealand': 'new-zealand',
        'Nigeria': 'nigeria',
        'Norway': 'norway',
        'Oman': 'oman',
        'Pakistan': 'pakistan',
        'Panama': 'panama',
        'Peru': 'peru',
        'Philippines': 'philippines',
        'Poland': 'poland',
        'Portugal': 'portugal',
        'Puerto Rico': 'puerto-rico',
        'Qatar': 'qatar',
        'Russia': 'russia',
        'Saudi Arabia': 'saudi-arabia',
        'Singapore': 'singapore',
        'South Africa': 'south-africa',
        'Spain': 'spain',
        'Sweden': 'sweden',
        'Switzerland': 'switzerland',
        'Thailand': 'thailand',
        'Turkey': 'turkey',
        'Ukraine': 'ukraine',
        'United Arab Emirates': 'united-arab-emirates',
        'United Kingdom': 'united-kingdom',
        'United States': 'united-states',
        'Venezuela': 'venezuela',
        'Vietnam': 'vietnam'
    }

    return countries

# Get trends of a country


def parse_tweet_volume(tweet_volume):

    if 'Under 10K' in tweet_volume:
        return None
    else:
        tweet_volume = tweet_volume.replace('Tweets', '').strip()
        if '.' in tweet_volume:
            return int(tweet_volume.replace('.', '').replace('K', '00'))
        else:
            return int(tweet_volume.replace('K', '000'))


def get_country_trends(country_name):

    try:
        country = Country.objects.get(name=country_name)
        woeid = country.woeid

        url = "https://twitter-trends.iamrohit.in/" + woeid
        country_trends_list = []

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        tbody = soup.find('tbody')
        rows = tbody.find_all('tr')

        cnt = 0
        for row in rows:
            if cnt == 20:
                break
            th_elements = row.find_all('th')
            if len(th_elements) > 1:
                second_th = th_elements[1]
                trend = second_th.find('a').text.strip()
                volume = parse_tweet_volume(second_th.find('div').text.strip())
                if trend[0] != '#':
                    country_trends_list.append((trend, volume))
                    cnt += 1

        return country_trends_list

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
                name=t[0], tweet_volume=t[1], country_trend=tct)
            t.save()


def translate_to_english(text):
    if text is None:
        return ""
    else:
        translator = Translator()
        try:
            english = translator.translate(text, dest='en').text
            if english:
                return english
            return ""
        except Exception:
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

    api = None  # api_setup()

    tweets = api.search_tweets(q=trend, count=20, result_type='popular')

    res = []

    for tweet in tweets:
        if not tweet.retweeted and 'RT @' not in tweet.text:

            clean_tweet = clean_text(tweet.text)
            if clean_tweet != '':
                res.append(clean_tweet)

    return res