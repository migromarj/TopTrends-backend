import re
from pytrends.request import TrendReq
from pytz import timezone
from django.core.exceptions import ObjectDoesNotExist

from main.models import Country, GoogleTrend, GoogleCountryTrend, GoogleWordTrend, GoogleWordTrendPeriod, GoogleTopic, GoogleRelatedTopic

# Convert snake_case to Title Case


def snake_to_title(string):
    words = re.findall(r'[a-zA-Z0-9]+', string)
    title_case = ' '.join([word.capitalize() for word in words])
    return title_case


pytrends = TrendReq(hl='en-US', tz=360)


def google_trends_countries():

    req_json = pytrends._get_data(
        url='https://trends.google.com/trends/hottrends/visualize/internal/data',
        method='get'
    )

    countries = {}

    for country in req_json:
        countries[snake_to_title(country)] = country

    return countries


def get_country_trends(country_name):

    try:

        country = Country.objects.get(name=country_name)
        pn = country.pn

        country_trends = pytrends.trending_searches(pn=pn)
        country_trends_list = country_trends.values.tolist()

        res = []
        for t in country_trends_list:
            res.append(t[0])

        return res
    except ObjectDoesNotExist:
        return []


def load_country_trends(country_name):

    trends = get_country_trends(country_name)

    if len(trends) > 0:

        country = Country.objects.get(name=country_name)

        if GoogleCountryTrend.objects.filter(country=country).exists():
            GoogleCountryTrend.objects.filter(country=country).delete()

        gct = GoogleCountryTrend(country=country)
        gct.save()

        for t in trends:
            t = GoogleTrend(name=t, country_trend=gct)
            t.save()


def get_period(period_type):

    period = None

    if period_type == 'daily':
        period = 'now 1-d'
    elif period_type == 'weekly':
        period = 'now 7-d'
    elif period_type == 'monthly':
        period = 'today 1-m'

    return period


def load_google_word_trend(word, country_name, period_type):

    period = get_period(period_type)

    if period is None:
        return

    country = Country.objects.get(name=country_name)

    if GoogleWordTrend.objects.filter(word=word, country=country, period_type=period_type).exists():
        GoogleWordTrend.objects.filter(
            word=word, country=country, period_type=period_type).delete()

    gwt = GoogleWordTrend(word=word, country=country, period_type=period_type)
    gwt.save()

    pytrends.build_payload(
        kw_list=[word], cat=0, timeframe=period, geo=country.acronym, gprop='')

    interest_over_time = pytrends.interest_over_time()

    for index, row in interest_over_time.iterrows():
        aux_index = timezone("UTC").localize(index.to_pydatetime())
        gwt_period = GoogleWordTrendPeriod(
            trend_datetime=aux_index, value=row[word], word_trend=gwt)
        gwt_period.save()


def load_related_topics(word, country_name, period_type):

    period = get_period(period_type)

    if period is None:
        return

    country = Country.objects.get(name=country_name)

    if GoogleRelatedTopic.objects.filter(word=word, country=country, period_type=period_type).exists():
        GoogleRelatedTopic.objects.filter(
            word=word, country=country, period_type=period_type).delete()

    grt = GoogleRelatedTopic(
        word=word, country=country, period_type=period_type)
    grt.save()

    pytrends.build_payload(
        kw_list=[word], cat=0, timeframe=period, geo=country.acronym, gprop='')
    trends_topics = pytrends.related_topics()
    top_topics = trends_topics.get(word).get("top")

    for _, row in top_topics.iterrows():
        gt = GoogleTopic(
            topic_title=row['topic_title'], topic_type=row['topic_type'], value=row['value'], main_topic=grt)
        gt.save()
