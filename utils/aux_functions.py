from utils.scraping.twitter import trend_countries
from utils.apis.google_trends import google_trends_countries
from utils.apis.countries import all_countries

from main.models import Country

from datetime import datetime
import pytz

### Auxiliar functions to use in schema.py ###


def load_countries():

    n_countries = Country.objects.count()

    if n_countries == 0:

        countries = all_countries()

        # Load countries from Twitter trends
        twitter_countries = trend_countries()

        # Load countries from Google Trends
        gt_countries = google_trends_countries()

        for country in countries:

            woeid, country_pn = None, None

            if country[0] in twitter_countries:
                woeid = twitter_countries[country[0]]
            elif country[1] in twitter_countries:
                woeid = twitter_countries[country[1]]
            if country[0] in gt_countries:
                country_pn = gt_countries[country[0]]
            elif country[1] in gt_countries:
                country_pn = gt_countries[country[1]]

            if woeid or country_pn:
                c = Country(name=country[0], native_name=country[1], acronym=country[2],
                            flag=country[3], lat=country[4], lng=country[5], woeid=woeid, pn=country_pn)
                c.save()


def setup_countries(kwargs):

    load_countries()

    name = kwargs.get('country')
    trends_number = kwargs.get(
        'trends_number') if kwargs.get('trends_number') else 5

    filtered_country = Country.objects.filter(name=name)

    return name, trends_number, filtered_country


def setup_words(kwargs):

    load_countries()

    word = kwargs.get('word')
    period_type = kwargs.get('period_type')
    country_name = kwargs.get('country')
    filtered_country = Country.objects.filter(name=country_name)

    return word, period_type, country_name, filtered_country


def remove_cache(obj):

    d1 = obj.insertion_datetime
    d2 = datetime.now(pytz.utc)
    elapsed_time = d2 - d1

    return elapsed_time.total_seconds() > 3600
