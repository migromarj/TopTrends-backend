from django.test import TestCase
from main.models import Country

# Tests of the Country model

FLAG_URL = 'https://flagcdn.com/br.svg'


class CountryModelTestCase(TestCase):

    def assert_country_attributes(self, country):
        self.assertEqual(country.name, 'Brazil')
        self.assertEqual(country.native_name, 'Brasil')
        self.assertEqual(country.acronym, 'BR')
        self.assertEqual(country.flag, FLAG_URL)
        self.assertEqual(country.woeid, 455189)
        self.assertEqual(country.pn, 'brazil')
        self.assertEqual(country.lat, -10)
        self.assertEqual(country.lng, -55)
        self.assertTrue(isinstance(country, Country))
        self.assertEqual(country.__str__(), country.name)

    def test_incorrect_country_model_creation(self):
        with self.assertRaises(Exception):
            country = Country.objects.create(
                name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=self.lng)
            country.full_clean()

    def setUp(self):

        self.country = Country.objects.create(
            name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)

    ####################################
    ### Country model creation tests ###
    ####################################

    def test_correct_country_model_creation(self):

        self.assertEqual(Country.objects.count(), 1)
        self.assert_country_attributes(self.country)

    # 'name' field

    def test_correct_country_model_creation_max_length_name(self):

        country = Country.objects.create(
            name='B'*60, native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)
        self.assertEqual(country.name, 'B'*60)

    def test_incorrect_country_model_creation_without_name(self):

        with self.assertRaises(Exception):
            Country.objects.create(name=None, native_name='Brasil', acronym='BR',
                                   flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)

    def test_incorrect_country_model_creation_blank_name(self):

        with self.assertRaises(Exception):
            country = Country.objects.create(
                name='', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)
            country.full_clean()

    def test_incorrect_country_model_creation_max_length_name(self):

        with self.assertRaises(Exception):
            Country.objects.create(name='B'*61, native_name='Brasil', acronym='BR',
                                   flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)

    # 'native_name' field

    def test_correct_country_model_creation_max_length_native_name(self):

        country = Country.objects.create(
            name='Brazil', native_name='B'*60, acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)
        self.assertEqual(country.native_name, 'B'*60)

    def test_incorrect_country_model_creation_without_native_name(self):

        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name=None, acronym='BR',
                                   flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)

    def test_incorrect_country_model_creation_blank_native_name(self):

        with self.assertRaises(Exception):
            country = Country.objects.create(
                name='Brazil', native_name='', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)
            country.full_clean()

    def test_incorrect_country_model_creation_max_length_native_name(self):

        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name='B'*61, acronym='BR',
                                   flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)

    # 'acronym' field

    def test_incorrect_country_model_creation_without_acronym(self):

        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name='Brasil', acronym=None,
                                   flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)

    def test_incorrect_country_model_creation_blank_acronym(self):

        with self.assertRaises(Exception):
            country = Country.objects.create(
                name='Brazil', native_name='Brasil', acronym='', flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)
            country.full_clean()

    def test_incorrect_country_model_creation_min_length_acronym(self):

        with self.assertRaises(Exception):
            country = Country.objects.create(
                name='Brazil', native_name='Brasil', acronym='B', flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)
            country.full_clean()

    def test_incorrect_country_model_creation_max_length_acronym(self):

        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name='Brasil', acronym='BRA',
                                   flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-55)

    # 'flag' field

    def test_correct_country_model_creation_max_length_flag(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR',
                                         flag='https://flagcdn.com/' + 'b' * 76 + '.svg', woeid=455189, pn='brazil', lat=-10, lng=-55)
        self.assertEqual(
            country.flag, 'https://flagcdn.com/' + 'b' * 76 + '.svg')

    def test_incorrect_country_model_creation_without_flag(self):

        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR',
                                   flag=None, woeid=455189, pn='brazil', lat=-10, lng=-55)

    def test_incorrect_country_model_creation_blank_flag(self):

        with self.assertRaises(Exception):
            country = Country.objects.create(
                name='Brazil', native_name='Brasil', acronym='BR', flag='', woeid=455189, pn='brazil', lat=-10, lng=-55)
            country.full_clean()

    def test_incorrect_country_model_creation_invalid_url_flag(self):

        with self.assertRaises(Exception):
            country = Country.objects.create(
                name='Brazil', native_name='Brasil', acronym='BR', flag='flag', woeid=455189, pn='brazil', lat=-10, lng=-55)
            country.full_clean()

    def test_incorrect_country_model_creation_max_length_flag(self):

        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR',
                                   flag='https://flagcdn.com/' + 'b' * 77 + '.svg', woeid=455189, pn='brazil', lat=-10, lng=-55)

    # 'woeid' field

    def test_correct_country_model_creation_max_integer_woeid(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR',
                                         flag=FLAG_URL, woeid=2147483647, pn='brazil', lat=-10, lng=-55)
        self.assertEqual(country.woeid, 2147483647)

    def test_incorrect_country_model_creation_invalid_integer_woeid(self):

        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR',
                                   flag=FLAG_URL, woeid='integer', pn='brazil', lat=-10, lng=-55)

    def test_incorrect_country_model_creation_max_integer_woeid(self):

        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR',
                                   flag=FLAG_URL, woeid=2147483648, pn='brazil', lat=-10, lng=-55)

    # 'pn' field

    def test_correct_country_model_creation_max_length_pn(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil',
                                         acronym='BR', flag=FLAG_URL, woeid=455189, pn='b'*30, lat=-10, lng=-55)
        self.assertEqual(country.pn, 'b'*30)

    def test_incorrect_country_model_creation_blank_pn(self):

        with self.assertRaises(Exception):
            country = Country.objects.create(
                name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='', lat=-10, lng=-55)
            country.full_clean()

    def test_incorrect_country_model_creation_max_length_pn(self):

        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR',
                                   flag=FLAG_URL, woeid=455189, pn='b'*31, lat=-10, lng=-55)

    # 'lat' field

    def test_correct_country_model_creation_max_integer_lat(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil',
                                         acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil', lat=90, lng=-55)
        self.assertEqual(country.lat, 90)

    def test_correct_country_model_creation_min_integer_lat(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil',
                                         acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil', lat=-90, lng=-55)
        self.assertEqual(country.lat, -90)

    def test_incorrect_country_model_creation_invalid_integer_lat(self):

        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR',
                                   flag=FLAG_URL, woeid=455189, pn='brazil', lat='integer', lng=-55)

    def test_incorrect_country_model_creation_max_integer_lat(self):

        with self.assertRaises(Exception):
            country = Country.objects.create(
                name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil', lat=91, lng=-55)
            country.full_clean()

    def test_incorrect_country_model_creation_min_integer_lat(self):

        with self.assertRaises(Exception):
            country = Country.objects.create(
                name='Brazil', native_name='Brasil', acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil', lat=-91, lng=-55)
            country.full_clean()

    # 'lng' field

    def test_correct_country_model_creation_max_integer_lng(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil',
                                         acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=180)
        self.assertEqual(country.lng, 180)

    def test_correct_country_model_creation_min_integer_lng(self):

        country = Country.objects.create(name='Brazil', native_name='Brasil',
                                         acronym='BR', flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng=-180)
        self.assertEqual(country.lng, -180)

    def test_incorrect_country_model_creation_invalid_integer_lng(self):

        with self.assertRaises(Exception):
            Country.objects.create(name='Brazil', native_name='Brasil', acronym='BR',
                                   flag=FLAG_URL, woeid=455189, pn='brazil', lat=-10, lng='integer')

    def test_incorrect_country_model_creation_max_integer_lng(self):

        self.lng = 181
        self.test_incorrect_country_model_creation()

    def test_incorrect_country_model_creation_min_integer_lng(self):

        self.lng = -181
        self.test_incorrect_country_model_creation()

    ##################################
    ### Country model update tests ###
    ##################################

    def test_correct_country_model_update(self):

        self.assert_country_attributes(self.country)

        self.country.name = 'Brasil Update'
        self.country.native_name = 'Brazil Update'
        self.country.acronym = 'BU'
        self.country.flag = 'https://flagcdn.com/bu.svg'
        self.country.woeid = 123456
        self.country.pn = 'brazil_update'
        self.country.lat = -20
        self.country.lng = -60
        self.country.save()

        self.assertEqual(self.country.name, 'Brasil Update')
        self.assertEqual(self.country.native_name, 'Brazil Update')
        self.assertEqual(self.country.acronym, 'BU')
        self.assertEqual(self.country.flag, 'https://flagcdn.com/bu.svg')
        self.assertEqual(self.country.woeid, 123456)
        self.assertEqual(self.country.pn, 'brazil_update')
        self.assertEqual(self.country.lat, -20)
        self.assertEqual(self.country.lng, -60)

    # 'name' field

    def test_correct_country_model_update_max_length_name(self):

        self.assertEqual(self.country.name, 'Brazil')
        self.country.name = 'B'*60
        self.country.save()
        self.assertEqual(self.country.name, 'B'*60)

    def test_incorrect_country_model_update_without_name(self):

        self.assertEqual(self.country.name, 'Brazil')

        with self.assertRaises(Exception):
            self.country.name = None
            self.country.save()

    def test_incorrect_country_model_update_blank_name(self):

        self.assertEqual(self.country.name, 'Brazil')

        with self.assertRaises(Exception):
            self.country.name = ''
            self.country.full_clean()

    def test_incorrect_country_model_update_max_length_name(self):

        self.assertEqual(self.country.name, 'Brazil')

        with self.assertRaises(Exception):
            self.country.name = 'B'*61
            self.country.save()

    # 'native_name' field

    def test_correct_country_model_update_max_length_native_name(self):

        self.assertEqual(self.country.native_name, 'Brasil')
        self.country.native_name = 'B'*60
        self.country.save()
        self.assertEqual(self.country.native_name, 'B'*60)

    def test_incorrect_country_model_update_without_native_name(self):

        self.assertEqual(self.country.native_name, 'Brasil')

        with self.assertRaises(Exception):
            self.country.native_name = None
            self.country.save()

    def test_incorrect_country_model_update_blank_native_name(self):

        self.assertEqual(self.country.native_name, 'Brasil')

        with self.assertRaises(Exception):
            self.country.native_name = ''
            self.country.full_clean()

    def test_incorrect_country_model_update_max_length_native_name(self):

        self.assertEqual(self.country.native_name, 'Brasil')

        with self.assertRaises(Exception):
            self.country.native_name = 'B'*61
            self.country.save()

    # 'acronym' field

    def test_incorrect_country_model_update_without_acronym(self):

        self.assertEqual(self.country.acronym, 'BR')

        with self.assertRaises(Exception):
            self.country.acronym = None
            self.country.save()

    def test_incorrect_country_model_update_blank_acronym(self):

        self.assertEqual(self.country.acronym, 'BR')

        with self.assertRaises(Exception):
            self.country.acronym = ''
            self.country.full_clean()

    def test_incorrect_country_model_update_min_length_acronym(self):

        self.assertEqual(self.country.acronym, 'BR')

        with self.assertRaises(Exception):
            self.country.acronym = 'B'
            self.country.full_clean()

    def test_incorrect_country_model_update_max_length_acronym(self):

        self.assertEqual(self.country.acronym, 'BR')

        with self.assertRaises(Exception):
            self.country.acronym = 'B'*3
            self.country.save()

    # 'flag' field

    def test_correct_country_model_update_max_length_flag(self):

        self.assertEqual(self.country.flag, FLAG_URL)
        self.country.flag = 'https://flagcdn.com/' + 'b'*76 + '.svg'
        self.country.save()
        self.assertEqual(self.country.flag,
                         'https://flagcdn.com/' + 'b'*76 + '.svg')

    def test_incorrect_country_model_update_without_flag(self):

        self.assertEqual(self.country.flag, FLAG_URL)

        with self.assertRaises(Exception):
            self.country.flag = None
            self.country.save()

    def test_incorrect_country_model_update_blank_flag(self):

        self.assertEqual(self.country.flag, FLAG_URL)

        with self.assertRaises(Exception):
            self.country.flag = ''
            self.country.full_clean()

    def test_incorrect_country_model_update_invalid_url_flag(self):

        self.assertEqual(self.country.flag, FLAG_URL)

        with self.assertRaises(Exception):
            self.country.flag = 'flag'
            self.country.full_clean()

    def test_incorrect_country_model_update_max_length_flag(self):

        self.assertEqual(self.country.flag, FLAG_URL)

        with self.assertRaises(Exception):
            self.country.flag = 'https://flagcdn.com/' + 'b'*77 + '.svg'
            self.country.save()

    # 'woeid' field

    def test_correct_country_model_update_max_integer_woeid(self):

        self.assertEqual(self.country.woeid, 455189)
        self.country.woeid = 2147483647
        self.country.save()
        self.assertEqual(self.country.woeid, 2147483647)

    def test_incorrect_country_model_update_invalid_integer_woeid(self):

        self.assertEqual(self.country.woeid, 455189)

        with self.assertRaises(Exception):
            self.country.woeid = 'invalid_integer'
            self.country.save()

    def test_incorrect_country_model_update_max_integer_woeid(self):

        self.assertEqual(self.country.woeid, 455189)

        with self.assertRaises(Exception):
            self.country.woeid = 2147483648
            self.country.save()

    # 'pn' field

    def test_correct_country_model_update_max_length_pn(self):

        self.assertEqual(self.country.pn, 'brazil')
        self.country.pn = 'b'*30
        self.country.save()
        self.assertEqual(self.country.pn, 'b'*30)

    def test_incorrect_country_model_update_blank_pn(self):

        self.assertEqual(self.country.pn, 'brazil')

        with self.assertRaises(Exception):
            self.country.pn = ''
            self.country.full_clean()

    def test_incorrect_country_model_update_max_length_pn(self):

        self.assertEqual(self.country.pn, 'brazil')

        with self.assertRaises(Exception):
            self.country.pn = 'b'*31
            self.country.save()

    # 'lat' field

    def test_correct_country_model_update_max_integer_lat(self):

        self.assertEqual(self.country.lat, -10)
        self.country.lat = 90
        self.country.save()
        self.assertEqual(self.country.lat, 90)

    def test_correct_country_model_update_min_integer_lat(self):

        self.assertEqual(self.country.lat, -10)
        self.country.lat = -90
        self.country.save()
        self.assertEqual(self.country.lat, -90)

    def test_incorrect_country_model_update_invalid_integer_lat(self):

        self.assertEqual(self.country.lat, -10)

        with self.assertRaises(Exception):
            self.country.lat = 'invalid_integer'
            self.country.save()

    def test_incorrect_country_model_update_max_integer_lat(self):

        self.assertEqual(self.country.lat, -10)

        with self.assertRaises(Exception):
            self.country.lat = 91
            self.country.full_clean()

    def test_incorrect_country_model_update_min_integer_lat(self):

        self.assertEqual(self.country.lat, -10)

        with self.assertRaises(Exception):
            self.country.lat = -91
            self.country.full_clean()

    # 'lng' field

    def test_correct_country_model_update_max_integer_lng(self):

        self.assertEqual(self.country.lng, -55)
        self.country.lng = 180
        self.country.save()
        self.assertEqual(self.country.lng, 180)

    def test_correct_country_model_update_min_integer_lng(self):

        self.assertEqual(self.country.lng, -55)
        self.country.lng = -180
        self.country.save()
        self.assertEqual(self.country.lng, -180)

    def test_incorrect_country_model_update_invalid_integer_lng(self):

        self.assertEqual(self.country.lng, -55)

        with self.assertRaises(Exception):
            self.country.lng = 'invalid_integer'
            self.country.save()

    def test_incorrect_country_model_update_max_integer_lng(self):

        self.assertEqual(self.country.lng, -55)

        with self.assertRaises(Exception):
            self.country.lng = 181
            self.country.full_clean()

    def test_incorrect_country_model_update_min_integer_lng(self):

        self.assertEqual(self.country.lng, -55)

        with self.assertRaises(Exception):
            self.country.lng = -181
            self.country.full_clean()

    ##################################
    ### Country model delete tests ###
    ##################################

    def test_correct_country_model_delete(self):

        self.assertEqual(Country.objects.count(), 1)
        self.country.delete()
        self.assertEqual(Country.objects.count(), 0)
