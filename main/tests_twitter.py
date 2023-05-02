from django.test import TestCase
from main.models import Country, TwitterTrend, TwitterCountryTrend

# Tests of the Twitter models

TREND_URL = 'https://trend.com'


class TwitterTrendModelTestCase(TestCase):

    def setUp(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag='https://flagcdn.com/br.svg', woeid=455189, pn='brazil')
        self.twitter_country_trend = TwitterCountryTrend.objects.create(country=country)
        self.twitter_trend = TwitterTrend.objects.create(name='Trend', url=TREND_URL, tweet_volume=100, country_trend=self.twitter_country_trend)


    #########################################
    ### TwitterTrend model creation tests ###
    #########################################


    def test_correct_twitter_trend_model_creation(self):
        
        self.assertEqual(TwitterTrend.objects.count(), 1)
        self.assertEqual(self.twitter_trend.name, 'Trend')
        self.assertEqual(self.twitter_trend.url, TREND_URL)
        self.assertEqual(self.twitter_trend.tweet_volume, 100)
        self.assertTrue(isinstance(self.twitter_trend, TwitterTrend))
        self.assertEqual(self.twitter_trend.__str__(), self.twitter_trend.name)


    # 'name' field

    def test_correct_twitter_trend_model_creation_max_length_name(self):
        
        twitter_trend = TwitterTrend.objects.create(name='T'*100, url=TREND_URL, tweet_volume=100, country_trend=self.twitter_country_trend)
        self.assertEqual(twitter_trend.name, 'T'*100)

    def test_incorrect_twitter_trend_model_creation_without_name(self):
        
        with self.assertRaises(Exception):
            TwitterTrend.objects.create(name=None, url=TREND_URL, tweet_volume=100, country_trend=self.twitter_country_trend)

    def test_incorrect_twitter_trend_model_creation_blank_name(self):
        
        with self.assertRaises(Exception):
            twitter_trend = TwitterTrend.objects.create(name='', url=TREND_URL, tweet_volume=100, country_trend=self.twitter_country_trend)
            twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_creation_max_length_name(self):
        
        with self.assertRaises(Exception):
            TwitterTrend.objects.create(name='T'*101, url=TREND_URL, tweet_volume=100, country_trend=self.twitter_country_trend)

    # 'url' field

    def test_correct_twitter_trend_model_creation_max_length_url(self):
        
        twitter_trend = TwitterTrend.objects.create(name='Trend', url='https://' + 't'*88 + '.com', tweet_volume=100, country_trend=self.twitter_country_trend)
        self.assertEqual(twitter_trend.url, 'https://' + 't'*88 + '.com')

    def test_incorrect_twitter_trend_model_creation_without_url(self):
        
        with self.assertRaises(Exception):
            TwitterTrend.objects.create(name='Trend', url=None, tweet_volume=100, country_trend=self.twitter_country_trend)

    def test_incorrect_twitter_trend_model_creation_blank_url(self):
        
        with self.assertRaises(Exception):
            twitter_trend = TwitterTrend.objects.create(name='Trend', url='', tweet_volume=100, country_trend=self.twitter_country_trend)
            twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_creation_invalid_url(self):
        
        with self.assertRaises(Exception):
            twitter_trend = TwitterTrend.objects.create(name='Trend', url='invalid_url', tweet_volume=100, country_trend=self.twitter_country_trend)
            twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_creation_max_length_url(self):
        
        with self.assertRaises(Exception):
            TwitterTrend.objects.create(name='Trend', url='https://' + 't'*89 + '.com', tweet_volume=100, country_trend=self.twitter_country_trend)

    # 'tweet_volume' field

    def test_correct_twitter_trend_model_creation_max_value_tweet_volume(self):
        
        twitter_trend = TwitterTrend.objects.create(name='Trend', url=TREND_URL, tweet_volume=2147483647, country_trend=self.twitter_country_trend)
        self.assertEqual(twitter_trend.tweet_volume, 2147483647)

    def test_incorrect_twitter_trend_model_creation_invalid_integer_tweet_volume(self):
        
        with self.assertRaises(Exception):
            TwitterTrend.objects.create(name='Trend', url=TREND_URL, tweet_volume='invalid_integer', country_trend=self.twitter_country_trend)

    def test_incorrect_twitter_trend_model_creation_max_value_tweet_volume(self):
        
        with self.assertRaises(Exception):
            TwitterTrend.objects.create(name='Trend', url=TREND_URL, tweet_volume=2147483648, country_trend=self.twitter_country_trend)

    # 'country_trend' field

    def test_incorrect_twitter_trend_model_creation_without_country_trend(self):
        
        with self.assertRaises(Exception):
            TwitterTrend.objects.create(name='Trend', url=TREND_URL, tweet_volume=100, country_trend=None)

    def test_incorrect_twitter_trend_model_creation_invalid_country_trend(self):
        
        with self.assertRaises(Exception):
            TwitterTrend.objects.create(name='Trend', url=TREND_URL, tweet_volume=100, country_trend='invalid_country_trend')


    #######################################
    ### TwitterTrend model update tests ###
    #######################################


    def test_correct_twitter_trend_model_update(self):

        self.assertEqual(self.twitter_trend.name, 'Trend')
        self.assertEqual(self.twitter_trend.url, TREND_URL)
        self.assertEqual(self.twitter_trend.tweet_volume, 100)
        self.assertEqual(self.twitter_trend.country_trend, self.twitter_country_trend)

        country = Country.objects.create(name='Argentina', native_name='Argentina', acronym='AR', flag='https://flagcdn.com/ar.svg', woeid=332471, pn='argentina')
        twitter_country_trend = TwitterCountryTrend.objects.create(country=country)

        self.twitter_trend.name = 'TrendTrend'
        self.twitter_trend.url = 'https://trendtrend.com'
        self.twitter_trend.tweet_volume = 200
        self.twitter_trend.country_trend = twitter_country_trend
        self.twitter_trend.save()

        self.assertEqual(self.twitter_trend.name, 'TrendTrend')
        self.assertEqual(self.twitter_trend.url, 'https://trendtrend.com')
        self.assertEqual(self.twitter_trend.tweet_volume, 200)
        self.assertEqual(self.twitter_trend.country_trend, twitter_country_trend)


    # 'name' field

    def test_correct_twitter_trend_model_update_max_length_name(self):

        self.assertEqual(self.twitter_trend.name, 'Trend')

        self.twitter_trend.name = 'T'*100
        self.twitter_trend.save()

        self.assertEqual(self.twitter_trend.name, 'T'*100)

    def test_incorrect_twitter_trend_model_update_without_name(self):

        self.assertEqual(self.twitter_trend.name, 'Trend')
        
        with self.assertRaises(Exception):
            self.twitter_trend.name = None
            self.twitter_trend.save()

    def test_incorrect_twitter_trend_model_update_blank_name(self):

        self.assertEqual(self.twitter_trend.name, 'Trend')

        with self.assertRaises(Exception):
            self.twitter_trend.name = ''
            self.twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_update_max_length_name(self):

        self.assertEqual(self.twitter_trend.name, 'Trend')

        with self.assertRaises(Exception):
            self.twitter_trend.name = 'T'*101
            self.twitter_trend.save()

    # 'url' field

    def test_correct_twitter_trend_model_update_max_length_url(self):

        self.assertEqual(self.twitter_trend.url, TREND_URL)

        self.twitter_trend.url = 'https://' + 't'*88 + '.com'
        self.twitter_trend.save()
    
        self.assertEqual(self.twitter_trend.url, 'https://' + 't'*88 + '.com')

    def test_incorrect_twitter_trend_model_update_without_url(self):

        self.assertEqual(self.twitter_trend.url, TREND_URL)

        with self.assertRaises(Exception):
            self.twitter_trend.url = None
            self.twitter_trend.save()

    def test_incorrect_twitter_trend_model_update_blank_url(self):

        self.assertEqual(self.twitter_trend.url, TREND_URL)

        with self.assertRaises(Exception):
            self.twitter_trend.url = ''
            self.twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_update_invalid_url(self):
        
        self.assertEqual(self.twitter_trend.url, TREND_URL)

        with self.assertRaises(Exception):
            self.twitter_trend.url = 'invalid_url'
            self.twitter_trend.full_clean()

    def test_incorrect_twitter_trend_model_update_max_length_url(self):

        self.assertEqual(self.twitter_trend.url, TREND_URL)

        with self.assertRaises(Exception):
            self.twitter_trend.url = 'https://' + 't'*89 + '.com'
            self.twitter_trend.save()

    # 'tweet_volume' field

    def test_correct_twitter_trend_model_update_max_integer_tweet_volume(self):

        self.assertEqual(self.twitter_trend.tweet_volume, 100)

        self.twitter_trend.tweet_volume = 2147483647
        self.twitter_trend.save()

        self.assertEqual(self.twitter_trend.tweet_volume, 2147483647)

    def test_incorrect_twitter_trend_model_update_invalid_integer_tweet_volume(self):
            
        self.assertEqual(self.twitter_trend.tweet_volume, 100)

        with self.assertRaises(Exception):
            self.twitter_trend.tweet_volume = 'invalid_integer'
            self.twitter_trend.save()

    def test_incorrect_twitter_trend_model_update_max_integer_tweet_volume(self):

        self.assertEqual(self.twitter_trend.tweet_volume, 100)

        with self.assertRaises(Exception):
            self.twitter_trend.tweet_volume = 2147483648
            self.twitter_trend.save()

    # 'country_trend' field

    def test_incorrect_twitter_trend_model_update_without_country_trend(self):

        self.assertEqual(self.twitter_trend.country_trend, self.twitter_country_trend)

        with self.assertRaises(Exception):
            self.twitter_trend.country_trend = None
            self.twitter_trend.save()

    def test_incorrect_twitter_trend_model_update_invalid_country_trend(self):

        self.assertEqual(self.twitter_trend.country_trend, self.twitter_country_trend)

        with self.assertRaises(Exception):
            self.twitter_trend.country_trend = 'invalid_country_trend'


    #######################################
    ### TwitterTrend model delete tests ###
    #######################################


    def test_correct_twitter_trend_model_delete(self):

        self.assertEqual(TwitterTrend.objects.count(), 1)
        self.twitter_trend.delete()
        self.assertEqual(TwitterTrend.objects.count(), 0)


class TwitterCountryTrendModelTestCase(TestCase):

    def setUp(self):

        self.country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR', flag='https://flagcdn.com/br.svg', woeid=455189, pn='brazil')
        self.twitter_country_trend = TwitterCountryTrend.objects.create(country=self.country)
        self.twitter_trend = TwitterTrend.objects.create(name='Trend', url=TREND_URL, tweet_volume=100, country_trend=self.twitter_country_trend)

        
    ################################################
    ### TwitterCountryTrend model creation tests ###
    ################################################


    def test_correct_twitter_country_trend_model_creation(self):

        self.assertEqual(TwitterCountryTrend.objects.count(), 1)
        self.assertEqual(self.twitter_country_trend.country, self.country)
        self.assertTrue(isinstance(self.twitter_country_trend, TwitterCountryTrend))
        self.assertEqual(self.twitter_country_trend.__str__(), self.country.name)


    # 'country' field

    def test_incorrect_twitter_country_trend_model_creation_without_country(self):

        with self.assertRaises(Exception):
            TwitterCountryTrend.objects.create(country=None)

    def test_incorrect_twitter_country_trend_model_creation_invalid_country(self):

        with self.assertRaises(Exception):
            TwitterCountryTrend.objects.create(country='invalid_country')


    ##############################################
    ### TwitterCountryTrend model update tests ###
    ##############################################


    def test_correct_twitter_country_trend_model_update(self):

        self.assertEqual(self.twitter_country_trend.country.name, 'Brazil')

        self.twitter_country_trend.country = Country.objects.create(name='Argentina', native_name='Argentina', acronym='AR', flag='https://flagcdn.com/ar.svg', woeid=332471, pn='argentina')
        self.twitter_country_trend.save()

        self.assertEqual(self.twitter_country_trend.country.name, 'Argentina')


    # 'country' field

    def test_incorrect_twitter_country_trend_model_update_without_country(self):

        self.assertEqual(self.twitter_country_trend.country, self.country)
            
        with self.assertRaises(Exception):
            self.twitter_country_trend.country = None
            self.twitter_country_trend.save()

    def test_incorrect_twitter_country_trend_model_update_invalid_country(self):

        self.assertEqual(self.twitter_country_trend.country, self.country)
            
        with self.assertRaises(Exception):
            self.twitter_country_trend.country = 'invalid_country'


    ##############################################
    ### TwitterCountryTrend model delete tests ###
    ##############################################


    def test_correct_twitter_country_trend_model_delete(self):

        self.assertEqual(TwitterCountryTrend.objects.count(), 1)
        self.assertEqual(TwitterTrend.objects.count(), 1)
        self.twitter_country_trend.delete()
        self.assertEqual(TwitterCountryTrend.objects.count(), 0)
        self.assertEqual(TwitterTrend.objects.count(), 0)
