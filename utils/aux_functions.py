from utils.apis.twitter import trend_countries
from utils.apis.google_trends import google_trends_countries
from utils.apis.countries import all_countries

from main.models import Country

from datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

### Auxiliar functions to use in schema.py ###

def load_countries():

    n_countries = Country.objects.count()

    if n_countries == 0:

        countries = all_countries()

        # Load countries from Twitter trends
        twitter_countries, _ = trend_countries()

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

            c = Country(name=country[0], native_name=country[1], acronym=country[2], flag=country[3], lat=country[4], lng=country[5], woeid=woeid, pn=country_pn)
            c.save()

def setup_countries(kwargs):

    load_countries()

    name = kwargs.get('country')
    trends_number = kwargs.get('trends_number') if kwargs.get('trends_number') else 5

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

    d1 = obj.insertion_datetime + timedelta(hours=1)
    d1 = datetime.strptime(str(d1).split("+")[0], DATE_FORMAT)
    
    d2 = datetime.strptime(str(datetime.now()), DATE_FORMAT)

    if d1 < d2 - timedelta(hours=1):
        return True
    return False