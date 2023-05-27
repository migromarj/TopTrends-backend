import requests
from decouple import config
from utils.scraping.twitter import translate_to_english


def get_relevant_news(trend):

    news_api_key = config('NEWS_API_KEY')

    url = "https://bing-news-search1.p.rapidapi.com/news/search"

    querystring = {"q": trend, "freshness": "Day",
                   "textFormat": "Raw", "safeSearch": "Off"}

    headers = {
        "X-BingApis-SDK": "true",
        "X-RapidAPI-Key": news_api_key,
        "X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    articles = response.json()['value']

    res = []

    for article in articles:
        description = article['description']
        description = translate_to_english(description)
        res.append(description)

    return res
