from django.test import TestCase
from main.models import Country, GoogleTrend, GoogleCountryTrend, GoogleWordTrendPeriod, GoogleWordTrend, GoogleTopic, GoogleRelatedTopic
from datetime import datetime
import pytz

# Tests of the Google Trends models

FLAG_URL_BR = 'https://flagcdn.com/br.svg'
FLAG_URL_AR = 'https://flagcdn.com/ar.svg'
TOPIC_TITLE = 'Topic title'
TOPIC_TYPE = 'Topic type'


class GoogleTrendsTestCase(TestCase):

    def assert_google_trend_attributes(self, google):
        self.assertEqual(GoogleTrend.objects.count(), 1)
        self.assertEqual(self.google_trend.name, 'Trend')
        self.assertEqual(self.google_trend.country_trend,
                         self.google_country_trend)
        self.assertTrue(isinstance(self.google_trend, GoogleTrend))
        self.assertEqual(self.google_trend.__str__(), self.google_trend.name)

    def setUp(self):

        country = Country.objects.create(
            name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL_BR, woeid=455189, pn='brazil')
        self.google_country_trend = GoogleCountryTrend.objects.create(
            country=country)
        self.google_trend = GoogleTrend.objects.create(
            name='Trend', country_trend=self.google_country_trend)

    ########################################
    ### GoogleTrend model creation tests ###
    ########################################

    def test_correct_google_trend_model_creation(self):

        self.assert_google_trend_attributes(self.google_trend)

    # 'name' field

    def test_correct_google_trend_model_creation_max_length_name(self):

        google_trend = GoogleTrend.objects.create(
            name='T'*100, country_trend=self.google_country_trend)
        self.assertEqual(google_trend.name, 'T'*100)

    def test_incorrect_google_trend_model_creation_without_name(self):

        with self.assertRaises(Exception):
            GoogleTrend.objects.create(
                name=None, country_trend=self.google_country_trend)

    def test_incorrect_google_trend_model_creation_blank_name(self):

        with self.assertRaises(Exception):
            google_trend = GoogleTrend.objects.create(
                name='', country_trend=self.google_country_trend)
            google_trend.full_clean()

    def test_incorrect_google_trend_model_creation_max_length_name(self):

        with self.assertRaises(Exception):
            GoogleTrend.objects.create(
                name='T'*101, country_trend=self.google_country_trend)

    # 'country_trend' field

    def test_incorrect_google_trend_model_creation_without_country_trend(self):

        with self.assertRaises(Exception):
            GoogleTrend.objects.create(name='Trend', country_trend=None)

    def test_incorrect_google_trend_model_creation_invalid_country_trend(self):

        with self.assertRaises(Exception):
            GoogleTrend.objects.create(
                name='Trend', country_trend='invalid_country_trend')

    #######################################
    ### GoogleTrend model update tests ####
    #######################################

    def test_correct_google_trend_model_update(self):

        self.assert_google_trend_attributes(self.google_trend)

        country = Country.objects.create(
            name='Argentina', native_name='Argentina', acronym='AR', flag=FLAG_URL_AR, woeid=332471, pn='argentina')
        google_country_trend = GoogleCountryTrend.objects.create(
            country=country)

        self.google_trend.name = 'New Trend'
        self.google_trend.country_trend = google_country_trend
        self.google_trend.save()

        self.assertEqual(GoogleTrend.objects.count(), 1)
        self.assertEqual(self.google_trend.name, 'New Trend')
        self.assertEqual(self.google_trend.country_trend, google_country_trend)

    # 'name' field

    def test_correct_google_trend_model_update_max_length_name(self):

        self.assertEqual(self.google_trend.name, 'Trend')
        self.google_trend.name = 'T'*100
        self.google_trend.save()
        self.assertEqual(self.google_trend.name, 'T'*100)

    def test_incorrect_google_trend_model_update_without_name(self):

        self.assertEqual(self.google_trend.name, 'Trend')

        with self.assertRaises(Exception):
            self.google_trend.name = None
            self.google_trend.save()

    def test_incorrect_google_trend_model_update_blank_name(self):

        self.assertEqual(self.google_trend.name, 'Trend')

        with self.assertRaises(Exception):
            self.google_trend.name = ''
            self.google_trend.full_clean()

    def test_incorrect_google_trend_model_update_max_length_name(self):

        self.assertEqual(self.google_trend.name, 'Trend')

        with self.assertRaises(Exception):
            self.google_trend.name = 'T'*101
            self.google_trend.save()

    # 'country_trend' field

    def test_incorrect_google_trend_model_update_without_country_trend(self):

        self.assertEqual(self.google_trend.country_trend,
                         self.google_country_trend)

        with self.assertRaises(Exception):
            self.google_trend.country_trend = None
            self.google_trend.save()

    def test_incorrect_google_trend_model_update_invalid_country_trend(self):

        self.assertEqual(self.google_trend.country_trend,
                         self.google_country_trend)

        with self.assertRaises(Exception):
            self.google_trend.country_trend = 'invalid_country_trend'

    #######################################
    ### GoogleTrend model delete tests ####
    #######################################

    def test_correct_google_trend_model_delete(self):

        self.assertEqual(GoogleTrend.objects.count(), 1)
        self.google_trend.delete()
        self.assertEqual(GoogleTrend.objects.count(), 0)


class GoogleCountryTrendModelTestCase(TestCase):

    def setUp(self):

        self.country = Country.objects.create(
            name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL_BR, woeid=455189, pn='brazil')
        self.google_country_trend = GoogleCountryTrend.objects.create(
            country=self.country)
        self.google_trend = GoogleTrend.objects.create(
            name='Trend', country_trend=self.google_country_trend)

    ###############################################
    ### GoogleCountryTrend model creation tests ###
    ###############################################

    def test_correct_google_country_trend_model_creation(self):

        self.assertEqual(GoogleCountryTrend.objects.count(), 1)
        self.assertEqual(self.google_country_trend.country, self.country)
        self.assertTrue(isinstance(
            self.google_country_trend, GoogleCountryTrend))
        self.assertEqual(self.google_country_trend.__str__(),
                         self.country.name)

    # 'country' field

    def test_incorrect_google_country_trend_model_creation_without_country(self):

        with self.assertRaises(Exception):
            GoogleCountryTrend.objects.create(country=None)

    def test_incorrect_google_country_trend_model_creation_invalid_country(self):

        with self.assertRaises(Exception):
            GoogleCountryTrend.objects.create(country='invalid_country')

    ##############################################
    ### GoogleCountryTrend model update tests ###
    ##############################################

    def test_correct_google_country_trend_model_update(self):

        self.assertEqual(self.google_country_trend.country, self.country)

        country = Country.objects.create(
            name='Argentina', native_name='Argentina', acronym='AR', flag=FLAG_URL_AR, woeid=332471, pn='argentina')

        self.google_country_trend.country = country
        self.google_country_trend.save()

        self.assertEqual(GoogleCountryTrend.objects.count(), 1)
        self.assertEqual(self.google_country_trend.country, country)

    # 'country' field

    def test_incorrect_google_country_trend_model_update_without_country(self):

        self.assertEqual(self.google_country_trend.country, self.country)

        with self.assertRaises(Exception):
            self.google_country_trend.country = None
            self.google_country_trend.save()

    def test_incorrect_google_country_trend_model_update_invalid_country(self):

        self.assertEqual(self.google_country_trend.country, self.country)

        with self.assertRaises(Exception):
            self.google_country_trend.country = 'invalid_country'

    ##############################################
    ### GoogleCountryTrend model delete tests ###
    ##############################################

    def test_correct_google_country_trend_model_delete(self):

        self.assertEqual(GoogleCountryTrend.objects.count(), 1)
        self.assertEqual(GoogleTrend.objects.count(), 1)
        self.google_country_trend.delete()
        self.assertEqual(GoogleCountryTrend.objects.count(), 0)
        self.assertEqual(GoogleTrend.objects.count(), 0)


class GoogleWordTrendPeriodModelTestCase(TestCase):

    def setUp(self):

        country = Country.objects.create(
            name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL_BR, woeid=455189, pn='brazil')
        self.google_word_trend = GoogleWordTrend.objects.create(
            word='Word', country=country, period_type='weekly')
        self.google_word_trend_period = GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(
            2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value=1, word_trend=self.google_word_trend)

    ##################################################
    ### GoogleWordTrendPeriod model creation tests ###
    ##################################################

    def test_correct_google_word_trend_period_model_creation(self):

        self.assertEqual(GoogleWordTrendPeriod.objects.count(), 1)
        self.assertEqual(self.google_word_trend_period.trend_datetime,
                         datetime(2023, 1, 25, 0, 0, 0, 0, pytz.UTC))
        self.assertEqual(self.google_word_trend_period.value, 1)
        self.assertEqual(
            self.google_word_trend_period.word_trend, self.google_word_trend)
        self.assertTrue(isinstance(
            self.google_word_trend_period, GoogleWordTrendPeriod))
        self.assertEqual(self.google_word_trend_period.__str__(), self.google_word_trend.country.name +
                         ' - ' + self.google_word_trend.word + ' - ' + str(self.google_word_trend_period.trend_datetime))

    # 'trend_datetime' field

    def test_incorrect_google_word_trend_period_model_creation_without_trend_datetime(self):

        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(
                trend_datetime=None, value=1, word_trend=self.google_word_trend)

    def test_incorrect_google_country_trend_model_creation_invalid_datetime_trend_datetime(self):

        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(
                trend_datetime='invalid_datetime', value=1, word_trend=self.google_word_trend)

    # 'value' field

    def test_correct_google_country_trend_model_creation_max_small_integer_value(self):

        google_word_trend_period = GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(
            2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value=32767, word_trend=self.google_word_trend)
        self.assertEqual(google_word_trend_period.value, 32767)

    def test_incorrect_google_word_trend_period_model_creation_without_value(self):

        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(
                2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value=None, word_trend=self.google_word_trend)

    def test_incorrect_google_country_trend_model_creation_invalid_integer_value(self):

        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(
                2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value='invalid_integer', word_trend=self.google_word_trend)

    def test_incorrect_google_country_trend_model_creation_max_small_integer_value(self):

        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(
                2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value=32768, word_trend=self.google_word_trend)

    # 'word_trend' field

    def test_incorrect_google_word_trend_period_model_creation_without_word_trend(self):

        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(
                2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value=1, word_trend=None)

    def test_incorrect_google_word_trend_period_model_creation_invalid_word_trend(self):

        with self.assertRaises(Exception):
            GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(
                2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value=1, word_trend='invalid_word_trend')

    ################################################
    ### GoogleWordTrendPeriod model update tests ###
    ################################################

    def test_correct_google_word_trend_period_model_update(self):

        self.assertEqual(self.google_word_trend_period.trend_datetime,
                         datetime(2023, 1, 25, 0, 0, 0, 0, pytz.UTC))
        self.assertEqual(self.google_word_trend_period.value, 1)
        self.assertEqual(
            self.google_word_trend_period.word_trend, self.google_word_trend)

        country = Country.objects.create(
            name='Argentina', native_name='Argentina', acronym='AR', flag=FLAG_URL_AR, woeid=332471, pn='argentina')
        google_word_trend = GoogleWordTrend.objects.create(
            word='Word', country=country, period_type='weekly')

        self.google_word_trend_period.trend_datetime = datetime(
            2023, 1, 24, 0, 0, 0, 0, pytz.UTC)
        self.google_word_trend_period.value = 21
        self.google_word_trend_period.word_trend = google_word_trend
        self.google_word_trend_period.save()

        self.assertEqual(GoogleWordTrendPeriod.objects.count(), 1)
        self.assertEqual(self.google_word_trend_period.trend_datetime,
                         datetime(2023, 1, 24, 0, 0, 0, 0, pytz.UTC))
        self.assertEqual(self.google_word_trend_period.value, 21)
        self.assertEqual(
            self.google_word_trend_period.word_trend, google_word_trend)

    # 'trend_datetime' field

    def test_incorrect_google_word_trend_period_model_update_without_trend_datetime(self):

        self.assertEqual(self.google_word_trend_period.trend_datetime,
                         datetime(2023, 1, 25, 0, 0, 0, 0, pytz.UTC))

        with self.assertRaises(Exception):
            self.google_word_trend_period.trend_datetime = None
            self.google_word_trend_period.save()

    def test_incorrect_google_word_trend_period_model_update_invalid_datetime_trend_datetime(self):

        self.assertEqual(self.google_word_trend_period.trend_datetime,
                         datetime(2023, 1, 25, 0, 0, 0, 0, pytz.UTC))

        with self.assertRaises(Exception):
            self.google_word_trend_period.trend_datetime = 'invalid_datetime'
            self.google_word_trend_period.save()

    # 'value' field

    def test_correct_google_country_trend_model_update_max_small_integer_value(self):

        self.assertEqual(self.google_word_trend_period.value, 1)
        self.google_word_trend_period.value = 32767
        self.google_word_trend_period.save()
        self.assertEqual(self.google_word_trend_period.value, 32767)

    def test_incorrect_google_word_trend_period_model_update_without_value(self):

        self.assertEqual(self.google_word_trend_period.value, 1)

        with self.assertRaises(Exception):
            self.google_word_trend_period.value = None
            self.google_word_trend_period.save()

    def test_incorrect_google_word_trend_period_model_update_invalid_integer_value(self):

        self.assertEqual(self.google_word_trend_period.value, 1)

        with self.assertRaises(Exception):
            self.google_word_trend_period.value = 'invalid_integer'
            self.google_word_trend_period.save()

    def test_incorrect_google_country_trend_model_update_max_small_integer_value(self):

        self.assertEqual(self.google_word_trend_period.value, 1)

        with self.assertRaises(Exception):
            self.google_word_trend_period.value = 32768
            self.google_word_trend_period.save()

    # 'word_trend' field

    def test_incorrect_google_word_trend_period_model_update_invalid_word_trend(self):

        self.assertEqual(
            self.google_word_trend_period.word_trend, self.google_word_trend)

        with self.assertRaises(Exception):
            self.google_word_trend_period.word_trend = 'invalid_word_trend'

    def test_incorrect_google_word_trend_period_model_update_without_word_trend(self):

        self.assertEqual(
            self.google_word_trend_period.word_trend, self.google_word_trend)

        with self.assertRaises(Exception):
            self.google_word_trend_period.word_trend = None
            self.google_word_trend_period.save()

    ################################################
    ### GoogleWordTrendPeriod model delete tests ###
    ################################################

    def test_correct_google_word_trend_period_model_delete(self):

        self.assertEqual(GoogleWordTrendPeriod.objects.count(), 1)
        self.google_word_trend_period.delete()
        self.assertEqual(GoogleWordTrendPeriod.objects.count(), 0)


class GoogleWordTrendModelTestCase(TestCase):

    def setUp(self):

        self.country = Country.objects.create(
            name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL_BR, woeid=455189, pn='brazil')
        self.google_word_trend = GoogleWordTrend.objects.create(
            word='Word', country=self.country, period_type='weekly')
        self.google_word_trend_period = GoogleWordTrendPeriod.objects.create(trend_datetime=datetime(
            2023, 1, 25, 0, 0, 0, 0, pytz.UTC), value=1, word_trend=self.google_word_trend)

    ############################################
    ### GoogleWordTrend model creation tests ###
    ############################################

    def test_correct_google_word_trend_model_creation(self):

        self.assertEqual(GoogleWordTrend.objects.count(), 1)
        self.assertEqual(self.google_word_trend.word, 'Word')
        self.assertEqual(self.google_word_trend.country, self.country)
        self.assertEqual(self.google_word_trend.period_type, 'weekly')
        self.assertTrue(isinstance(self.google_word_trend, GoogleWordTrend))
        self.assertEqual(str(self.google_word_trend),
                         self.google_word_trend.country.name + ' - ' + self.google_word_trend.word)

    # 'word' field

    def test_correct_google_word_trend_model_creation_max_length_word(self):

        google_word_trend = GoogleWordTrend.objects.create(
            word='W' * 100, country=self.country, period_type='weekly')
        self.assertEqual(google_word_trend.word, 'W' * 100)

    def test_incorrect_google_word_trend_model_creation_without_word(self):

        with self.assertRaises(Exception):
            GoogleWordTrend.objects.create(
                word=None, country=self.country, period_type='weekly')

    def test_incorrect_google_word_trend_model_creation_blank_word(self):

        with self.assertRaises(Exception):
            google_word_trend = GoogleWordTrend.objects.create(
                word='', country=self.country, period_type='weekly')
            google_word_trend.full_clean()

    def test_incorrect_google_word_trend_model_creation_max_length_word(self):

        with self.assertRaises(Exception):
            GoogleWordTrend.objects.create(
                word='W' * 101, country=self.country, period_type='weekly')

    # 'country' field

    def test_incorrect_google_word_trend_model_creation_without_country(self):

        with self.assertRaises(Exception):
            GoogleWordTrend.objects.create(
                word='Word', country=None, period_type='weekly')

    def test_incorrect_google_word_trend_model_creation_invalid_country(self):

        with self.assertRaises(Exception):
            GoogleWordTrend.objects.create(
                word='Word', country='invalid_country', period_type='weekly')

    # 'period_type' field

    def test_correct_google_word_trend_model_creation_max_length_period_type(self):

        google_word_trend = GoogleWordTrend.objects.create(
            word='Word', country=self.country, period_type='P' * 10)
        self.assertEqual(google_word_trend.period_type, 'P' * 10)

    def test_incorrect_google_word_trend_model_creation_without_period_type(self):

        with self.assertRaises(Exception):
            GoogleWordTrend.objects.create(
                word='Word', country=self.country, period_type=None)

    def test_incorrect_google_word_trend_model_creation_blank_period_type(self):

        with self.assertRaises(Exception):
            google_word_trend = GoogleWordTrend.objects.create(
                word='Word', country=self.country, period_type='')
            google_word_trend.full_clean()

    def test_incorrect_google_word_trend_model_creation_max_lenght_period_type(self):

        with self.assertRaises(Exception):
            GoogleWordTrend.objects.create(
                word='Word', country=self.country, period_type='P' * 11)

    ##########################################
    ### GoogleWordTrend model update tests ###
    ##########################################

    def test_correct_google_word_trend_model_update(self):

        self.assertEqual(self.google_word_trend.word, 'Word')
        self.assertEqual(self.google_word_trend.country, self.country)
        self.assertEqual(self.google_word_trend.period_type, 'weekly')

        self.google_word_trend.word = 'Word update'
        country = Country.objects.create(
            name='Argentina', native_name='Argentina', acronym='AR', flag=FLAG_URL_AR, woeid=23424747, pn='argentina')
        self.google_word_trend.country = country
        self.google_word_trend.period_type = 'monthly'
        self.google_word_trend.save()

        self.assertEqual(self.google_word_trend.word, 'Word update')
        self.assertEqual(self.google_word_trend.country, country)
        self.assertEqual(self.google_word_trend.period_type, 'monthly')

    # 'word' field

    def test_correct_google_word_trend_model_update_max_length_word(self):

        self.assertEqual(self.google_word_trend.word, 'Word')
        self.google_word_trend.word = 'W' * 100
        self.google_word_trend.save()
        self.assertEqual(self.google_word_trend.word, 'W' * 100)

    def test_incorrect_google_word_trend_model_update_without_word(self):

        self.assertEqual(self.google_word_trend.word, 'Word')

        with self.assertRaises(Exception):
            self.google_word_trend.word = None
            self.google_word_trend.save()

    def test_incorrect_google_word_trend_model_update_blank_word(self):

        self.assertEqual(self.google_word_trend.word, 'Word')

        with self.assertRaises(Exception):
            self.google_word_trend.word = ''
            self.google_word_trend.full_clean()

    def test_incorrect_google_word_trend_model_update_max_length_word(self):

        self.assertEqual(self.google_word_trend.word, 'Word')

        with self.assertRaises(Exception):
            self.google_word_trend.word = 'W' * 101
            self.google_word_trend.save()

    # 'country' field

    def test_incorrect_google_word_trend_model_update_without_country(self):

        self.assertEqual(self.google_word_trend.country, self.country)

        with self.assertRaises(Exception):
            self.google_word_trend.country = None
            self.google_word_trend.save()

    def test_incorrect_google_word_trend_model_update_invalid_country(self):

        self.assertEqual(self.google_word_trend.country, self.country)

        with self.assertRaises(Exception):
            self.google_word_trend.country = 'invalid_country'

    # 'period_type' field

    def test_correct_google_word_trend_model_update_max_length_period_type(self):

        self.assertEqual(self.google_word_trend.period_type, 'weekly')
        self.google_word_trend.period_type = 'P' * 10
        self.google_word_trend.save()
        self.assertEqual(self.google_word_trend.period_type, 'P' * 10)

    def test_incorrect_google_word_trend_model_update_without_period_type(self):

        self.assertEqual(self.google_word_trend.period_type, 'weekly')

        with self.assertRaises(Exception):
            self.google_word_trend.period_type = None
            self.google_word_trend.save()

    def test_incorrect_google_word_trend_model_update_blank_period_type(self):

        self.assertEqual(self.google_word_trend.period_type, 'weekly')

        with self.assertRaises(Exception):
            self.google_word_trend.period_type = ''
            self.google_word_trend.full_clean()

    def test_incorrect_google_word_trend_model_update_max_length_period_type(self):

        self.assertEqual(self.google_word_trend.period_type, 'weekly')

        with self.assertRaises(Exception):
            self.google_word_trend.period_type = 'P' * 11
            self.google_word_trend.save()

    ##########################################
    ### GoogleWordTrend model delete tests ###
    ##########################################

    def test_correct_google_word_trend_model_delete(self):

        self.assertEqual(GoogleWordTrend.objects.count(), 1)
        self.assertEqual(GoogleWordTrendPeriod.objects.count(), 1)
        self.google_word_trend.delete()
        self.assertEqual(GoogleWordTrend.objects.count(), 0)
        self.assertEqual(GoogleWordTrendPeriod.objects.count(), 0)


class GoogleTopicModelTestCase(TestCase):

    def assert_google_topic_model_fields(self, google_topic):
        self.assertEqual(GoogleTopic.objects.count(), 1)
        self.assertEqual(self.google_topic.topic_title, TOPIC_TITLE)
        self.assertEqual(self.google_topic.topic_type, TOPIC_TYPE)
        self.assertEqual(self.google_topic.value, 1)
        self.assertEqual(self.google_topic.main_topic,
                         self.google_related_topic)
        self.assertTrue(isinstance(self.google_topic, GoogleTopic))
        self.assertEqual(self.google_topic.__str__(
        ), self.google_topic.main_topic.word + ' - ' + self.google_topic.topic_title)

    def setUp(self):

        country = Country.objects.create(
            name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL_BR, woeid=455189, pn='brazil')
        self.google_related_topic = GoogleRelatedTopic.objects.create(
            word='Word', country=country, period_type='weekly')
        self.google_topic = GoogleTopic.objects.create(
            topic_title=TOPIC_TITLE, topic_type=TOPIC_TYPE, value=1, main_topic=self.google_related_topic)

    ########################################
    ### GoogleTopic model creation tests ###
    ########################################

    def test_correct_google_topic_model_creation(self):

        self.assert_google_topic_model_fields(self.google_topic)

    # 'topic_title' field

    def test_correct_google_topic_model_creation_max_length_topic_title(self):

        google_topic = GoogleTopic.objects.create(
            topic_title='T' * 100, topic_type=TOPIC_TYPE, value=1, main_topic=self.google_related_topic)
        self.assertEqual(google_topic.topic_title, 'T' * 100)

    def test_incorrect_google_topic_model_creation_without_topic_title(self):

        with self.assertRaises(Exception):
            GoogleTopic.objects.create(
                topic_title=None, topic_type=TOPIC_TYPE, value=1, main_topic=self.google_related_topic)

    def test_incorrect_google_topic_model_creation_blank_topic_title(self):

        with self.assertRaises(Exception):
            google_topic = GoogleTopic.objects.create(
                topic_title='', topic_type=TOPIC_TYPE, value=1, main_topic=self.google_related_topic)
            google_topic.full_clean()

    def test_incorrect_google_topic_model_creation_max_length_topic_title(self):

        with self.assertRaises(Exception):
            GoogleTopic.objects.create(
                topic_title='T' * 101, topic_type=TOPIC_TYPE, value=1, main_topic=self.google_related_topic)

    # 'topic_type' field

    def test_correct_google_topic_model_creation_max_length_topic_type(self):

        google_topic = GoogleTopic.objects.create(
            topic_title=TOPIC_TITLE, topic_type='T' * 100, value=1, main_topic=self.google_related_topic)
        self.assertEqual(google_topic.topic_type, 'T' * 100)

    def test_incorrect_google_topic_model_creation_without_topic_type(self):

        with self.assertRaises(Exception):
            GoogleTopic.objects.create(
                topic_title=TOPIC_TITLE, topic_type=None, value=1, main_topic=self.google_related_topic)

    def test_incorrect_google_topic_model_creation_blank_topic_type(self):

        with self.assertRaises(Exception):
            google_topic = GoogleTopic.objects.create(
                topic_title=TOPIC_TITLE, topic_type='', value=1, main_topic=self.google_related_topic)
            google_topic.full_clean()

    def test_incorrect_google_topic_model_creation_max_length_topic_type(self):

        with self.assertRaises(Exception):
            GoogleTopic.objects.create(
                topic_title=TOPIC_TITLE, topic_type='T' * 101, value=1, main_topic=self.google_related_topic)

    # 'value' field

    def test_correct_google_topic_model_creation_max_integer_value(self):

        google_topic = GoogleTopic.objects.create(
            topic_title=TOPIC_TITLE, topic_type=TOPIC_TYPE, value=32767, main_topic=self.google_related_topic)
        self.assertEqual(google_topic.value, 32767)

    def test_incorrect_google_topic_model_creation_without_value(self):

        with self.assertRaises(Exception):
            GoogleTopic.objects.create(
                topic_title=TOPIC_TITLE, topic_type=TOPIC_TYPE, value=None, main_topic=self.google_related_topic)

    def test_incorrect_google_topic_model_creation_invalid_integer_value(self):

        with self.assertRaises(Exception):
            GoogleTopic.objects.create(topic_title=TOPIC_TITLE, topic_type=TOPIC_TYPE,
                                       value='invalid_integer', main_topic=self.google_related_topic)

    def test_incorrect_google_topic_model_creation_max_integer_value(self):

        with self.assertRaises(Exception):
            GoogleTopic.objects.create(
                topic_title=TOPIC_TITLE, topic_type=TOPIC_TYPE, value=32768, main_topic=self.google_related_topic)

    # 'main_topic' field

    def test_incorrect_google_topic_model_creation_without_main_topic(self):

        with self.assertRaises(Exception):
            GoogleTopic.objects.create(
                topic_title=TOPIC_TITLE, topic_type=TOPIC_TYPE, value=1, main_topic=None)

    def test_incorrect_google_topic_model_creation_invalid_main_topic(self):

        with self.assertRaises(Exception):
            GoogleTopic.objects.create(
                topic_title=TOPIC_TITLE, topic_type=TOPIC_TYPE, value=1, main_topic='invalid main topic')

    ######################################
    ### GoogleTopic model update tests ###
    ######################################

    def test_correct_google_topic_model_update(self):

        self.assert_google_topic_model_fields(self.google_topic)

        country = Country.objects.create(
            name='Argentina', native_name='Argentina', acronym='AR', flag=FLAG_URL_AR, woeid=332471, pn='argentina')
        google_related_topic = GoogleRelatedTopic.objects.create(
            word='New Word', country=country, period_type='daily')

        self.google_topic.topic_title = 'New Topic title'
        self.google_topic.topic_type = 'New Topic type'
        self.google_topic.value = 2
        self.google_topic.main_topic = google_related_topic
        self.google_topic.save()

        self.assertEqual(GoogleTopic.objects.count(), 1)
        self.assertEqual(self.google_topic.topic_title, 'New Topic title')
        self.assertEqual(self.google_topic.topic_type, 'New Topic type')
        self.assertEqual(self.google_topic.value, 2)
        self.assertEqual(self.google_topic.main_topic, google_related_topic)

    # 'topic_title' field

    def test_correct_google_topic_model_update_max_length_topic_title(self):

        self.assertEqual(self.google_topic.topic_title, TOPIC_TITLE)
        self.google_topic.topic_title = 'T' * 100
        self.google_topic.save()
        self.assertEqual(self.google_topic.topic_title, 'T' * 100)

    def test_incorrect_google_topic_model_update_without_topic_title(self):

        self.assertEqual(self.google_topic.topic_title, TOPIC_TITLE)

        with self.assertRaises(Exception):
            self.google_topic.topic_title = None
            self.google_topic.save()

    def test_incorrect_google_topic_model_update_blank_topic_title(self):

        self.assertEqual(self.google_topic.topic_title, TOPIC_TITLE)

        with self.assertRaises(Exception):
            self.google_topic.topic_title = ''
            self.google_topic.full_clean()

    def test_incorrect_google_topic_model_update_max_length_topic_title(self):

        self.assertEqual(self.google_topic.topic_title, TOPIC_TITLE)

        with self.assertRaises(Exception):
            self.google_topic.topic_title = 'T' * 101
            self.google_topic.save()

    # 'topic_type' field

    def test_correct_google_topic_model_update_max_length_topic_type(self):

        self.assertEqual(self.google_topic.topic_type, TOPIC_TYPE)
        self.google_topic.topic_type = 'T' * 100
        self.google_topic.save()
        self.assertEqual(self.google_topic.topic_type, 'T' * 100)

    def test_incorrect_google_topic_model_update_without_topic_type(self):

        self.assertEqual(self.google_topic.topic_type, TOPIC_TYPE)

        with self.assertRaises(Exception):
            self.google_topic.topic_type = None
            self.google_topic.save()

    def test_incorrect_google_topic_model_update_blank_topic_type(self):

        self.assertEqual(self.google_topic.topic_type, TOPIC_TYPE)

        with self.assertRaises(Exception):
            self.google_topic.topic_type = ''
            self.google_topic.full_clean()

    def test_incorrect_google_topic_model_update_max_length_topic_type(self):

        self.assertEqual(self.google_topic.topic_type, TOPIC_TYPE)

        with self.assertRaises(Exception):
            self.google_topic.topic_type = 'T' * 101
            self.google_topic.save()

    # 'value' field

    def test_correct_google_topic_model_update_max_integer_value(self):

        self.assertEqual(self.google_topic.value, 1)
        self.google_topic.value = 32767
        self.google_topic.save()
        self.assertEqual(self.google_topic.value, 32767)

    def test_incorrect_google_topic_model_update_without_value(self):

        self.assertEqual(self.google_topic.value, 1)

        with self.assertRaises(Exception):
            self.google_topic.value = None
            self.google_topic.save()

    def test_incorrect_google_topic_model_update_invalid_integer_value(self):

        self.assertEqual(self.google_topic.value, 1)

        with self.assertRaises(Exception):
            self.google_topic.value = 'invalid_integer'
            self.google_topic.save()

    def test_incorrect_google_topic_model_update_max_integer_value(self):

        self.assertEqual(self.google_topic.value, 1)

        with self.assertRaises(Exception):
            self.google_topic.value = 32768
            self.google_topic.save()

    # 'main_topic' field

    def test_incorrect_google_topic_model_update_without_main_topic(self):

        self.assertEqual(self.google_topic.main_topic,
                         self.google_related_topic)

        with self.assertRaises(Exception):
            self.google_topic.main_topic = None
            self.google_topic.save()

    def test_incorrect_google_topic_model_update_invalid_main_topic(self):

        self.assertEqual(self.google_topic.main_topic,
                         self.google_related_topic)

        with self.assertRaises(Exception):
            self.google_topic.main_topic = 'invalid main topic'

    ######################################
    ### GoogleTopic model delete tests ###
    ######################################

    def test_correct_google_topic_model_delete(self):

        self.assertEqual(GoogleTopic.objects.count(), 1)
        self.google_topic.delete()
        self.assertEqual(GoogleTopic.objects.count(), 0)


class GoogleRelatedTopicModelTestCase(TestCase):

    def assert_google_related_topic_model_fields(self, google_related_topic):
        self.assertEqual(GoogleRelatedTopic.objects.count(), 1)
        self.assertEqual(self.google_related_topic.word, 'Word')
        self.assertEqual(self.google_related_topic.country, self.country)
        self.assertEqual(self.google_related_topic.period_type, 'weekly')
        self.assertTrue(isinstance(
            self.google_related_topic, GoogleRelatedTopic))
        self.assertEqual(self.google_related_topic.__str__(),
                         self.google_related_topic.country.name + ' - ' + self.google_related_topic.word)

    def setUp(self):

        self.country = Country.objects.create(
            name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL_BR, woeid=455189, pn='brazil')
        self.google_related_topic = GoogleRelatedTopic.objects.create(
            word='Word', country=self.country, period_type='weekly')
        self.google_topic = GoogleTopic.objects.create(
            topic_title=TOPIC_TITLE, topic_type=TOPIC_TYPE, value=1, main_topic=self.google_related_topic)

    ###############################################
    ### GoogleRelatedTopic model creation tests ###
    ###############################################

    def test_correct_google_related_topic_model_creation(self):

        self.assert_google_related_topic_model_fields(
            self.google_related_topic)

    # 'word' field

    def test_correct_google_related_topic_model_creation_max_length_word(self):

        google_related_topic = GoogleRelatedTopic.objects.create(
            word='W' * 100, country=self.country, period_type='weekly')
        self.assertEqual(google_related_topic.word, 'W' * 100)

    def test_incorrect_google_related_topic_model_creation_without_word(self):

        with self.assertRaises(Exception):
            GoogleRelatedTopic.objects.create(
                word=None, country=self.country, period_type='weekly')

    def test_incorrect_google_related_topic_model_creation_blank_word(self):

        with self.assertRaises(Exception):
            google_related_topic = GoogleRelatedTopic.objects.create(
                word='', country=self.country, period_type='weekly')
            google_related_topic.full_clean()

    def test_incorrect_google_related_topic_model_creation_max_length_word(self):

        with self.assertRaises(Exception):
            GoogleRelatedTopic.objects.create(
                word='W' * 101, country=self.country, period_type='weekly')

    # 'country' field

    def test_incorrect_google_related_topic_model_creation_without_country(self):

        with self.assertRaises(Exception):
            GoogleRelatedTopic.objects.create(
                word='Word', country=None, period_type='weekly')

    def test_incorrect_google_related_topic_model_creation_invalid_country(self):

        with self.assertRaises(Exception):
            GoogleRelatedTopic.objects.create(
                word='Word', country='invalid country', period_type='weekly')

    # 'period_type' field

    def test_correct_google_related_topic_model_creation_max_length_period_type(self):

        google_related_topic = GoogleRelatedTopic.objects.create(
            word='Word', country=self.country, period_type='P' * 10)
        self.assertEqual(google_related_topic.period_type, 'P' * 10)

    def test_incorrect_google_related_topic_model_creation_without_period_type(self):

        with self.assertRaises(Exception):
            GoogleRelatedTopic.objects.create(
                word='Word', country=self.country, period_type=None)

    def test_incorrect_google_related_topic_model_creation_blank_period_type(self):

        with self.assertRaises(Exception):
            google_related_topic = GoogleRelatedTopic.objects.create(
                word='Word', country=self.country, period_type='')
            google_related_topic.full_clean()

    def test_incorrect_google_related_topic_model_creation_max_length_period_type(self):

        with self.assertRaises(Exception):
            GoogleRelatedTopic.objects.create(
                word='Word', country=self.country, period_type='P' * 11)

    #############################################
    ### GoogleRelatedTopic model update tests ###
    #############################################

    def test_correct_google_related_topic_model_update(self):

        self.assert_google_related_topic_model_fields(
            self.google_related_topic)

        self.google_related_topic.word = 'New word'
        self.google_related_topic.country = self.country
        self.google_related_topic.period_type = 'monthly'
        self.google_related_topic.save()

        self.assertEqual(self.google_related_topic.word, 'New word')
        self.assertEqual(self.google_related_topic.country, self.country)
        self.assertEqual(self.google_related_topic.period_type, 'monthly')

    # 'word' field

    def test_correct_google_related_topic_model_update_max_length_word(self):

        self.assertEqual(self.google_related_topic.word, 'Word')
        self.google_related_topic.word = 'W' * 100
        self.google_related_topic.save()
        self.assertEqual(self.google_related_topic.word, 'W' * 100)

    def test_incorrect_google_related_topic_model_update_without_word(self):

        self.assertEqual(self.google_related_topic.word, 'Word')

        with self.assertRaises(Exception):
            self.google_related_topic.word = None
            self.google_related_topic.save()

    def test_incorrect_google_related_topic_model_update_blank_word(self):

        self.assertEqual(self.google_related_topic.word, 'Word')

        with self.assertRaises(Exception):
            self.google_related_topic.word = ''
            self.google_related_topic.full_clean()

    def test_incorrect_google_related_topic_model_update_max_length_word(self):

        self.assertEqual(self.google_related_topic.word, 'Word')

        with self.assertRaises(Exception):
            self.google_related_topic.word = 'W' * 101
            self.google_related_topic.save()

    # 'country' field

    def test_incorrect_google_related_topic_model_update_without_country(self):

        self.assertEqual(self.google_related_topic.country, self.country)

        with self.assertRaises(Exception):
            self.google_related_topic.country = None
            self.google_related_topic.save()

    def test_incorrect_google_related_topic_model_update_invalid_country(self):

        self.assertEqual(self.google_related_topic.country, self.country)

        with self.assertRaises(Exception):
            self.google_related_topic.country = 'invalid country'

    # 'period_type' field

    def test_correct_google_related_topic_model_update_max_length_period_type(self):

        self.assertEqual(self.google_related_topic.period_type, 'weekly')
        self.google_related_topic.period_type = 'P' * 10
        self.google_related_topic.save()
        self.assertEqual(self.google_related_topic.period_type, 'P' * 10)

    def test_incorrect_google_related_topic_model_update_without_period_type(self):

        self.assertEqual(self.google_related_topic.period_type, 'weekly')

        with self.assertRaises(Exception):
            self.google_related_topic.period_type = None
            self.google_related_topic.save()

    def test_incorrect_google_related_topic_model_update_blank_period_type(self):

        self.assertEqual(self.google_related_topic.period_type, 'weekly')

        with self.assertRaises(Exception):
            self.google_related_topic.period_type = ''
            self.google_related_topic.full_clean()

    def test_incorrect_google_related_topic_model_update_max_length_period_type(self):

        self.assertEqual(self.google_related_topic.period_type, 'weekly')

        with self.assertRaises(Exception):
            self.google_related_topic.period_type = 'P' * 11
            self.google_related_topic.save()

    #############################################
    ### GoogleRelatedTopic model delete tests ###
    #############################################

    def test_correct_google_related_topic_model_delete(self):

        self.assertEqual(GoogleRelatedTopic.objects.count(), 1)
        self.assertEqual(GoogleTopic.objects.count(), 1)
        self.google_related_topic.delete()
        self.assertEqual(GoogleRelatedTopic.objects.count(), 0)
        self.assertEqual(GoogleTopic.objects.count(), 0)
