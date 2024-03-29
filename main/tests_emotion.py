from django.test import TestCase
from main.models import TrendEmotion

# Tests of the TrendEmotion model


class TrendEmotionModelTestCase(TestCase):

    def assert_trend_emotion_attributes(self, trend_emotion):
        self.assertEqual(TrendEmotion.objects.count(), 1)
        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)
        self.assertEqual(self.trend_emotion.positive_emotion, 0.5)
        self.assertEqual(self.trend_emotion.sadness_emotion, 0.2)
        self.assertEqual(self.trend_emotion.fear_emotion, 0.3)
        self.assertEqual(self.trend_emotion.love_emotion, 0.2)
        self.assertEqual(self.trend_emotion.surprise_emotion, 0.1)
        self.assertEqual(self.trend_emotion.anger_emotion, 0.1)
        self.assertEqual(self.trend_emotion.joy_emotion, 0.1)
        self.assertEqual(self.trend_emotion.word, 'test')
        self.assertTrue(isinstance(self.trend_emotion, TrendEmotion))
        self.assertEqual(self.trend_emotion.__str__(
        ), self.trend_emotion.word + '-' + str(self.trend_emotion.insertion_datetime))

    def create_trend_emotion(self, negative_emotion, positive_emotion,
                             sadness_emotion, fear_emotion, love_emotion, surprise_emotion,
                             anger_emotion, joy_emotion, word=None, video_id=None):
        return TrendEmotion.objects.create(negative_emotion=negative_emotion,
                                           positive_emotion=positive_emotion,
                                           sadness_emotion=sadness_emotion,
                                           fear_emotion=fear_emotion,
                                           love_emotion=love_emotion,
                                           surprise_emotion=surprise_emotion,
                                           anger_emotion=anger_emotion,
                                           joy_emotion=joy_emotion,
                                           word=word,
                                           video_id=video_id
                                           )

    def setUp(self):

        self.trend_emotion = self.create_trend_emotion(
            0.5, 0.5, 0.2, 0.3, 0.2, 0.1, 0.1, 0.1, 'test')

    #########################################
    ### TrendEmotion model creation tests ###
    #########################################

    def test_correct_trend_emotion_model_creation(self):

        self.assert_trend_emotion_attributes(self.trend_emotion)

    # 'negative_emotion' field

    def test_correct_trend_emotion_creation_min_value_negative_emotion(self):

        trend_emotion = self.create_trend_emotion(
            0, 1, 0.2, 0.3, 0.2, 0.1, 0.1, 0.1, 'test')
        self.assertEqual(trend_emotion.negative_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_negative_emotion(self):

        trend_emotion = self.create_trend_emotion(
            1, 0, 0.2, 0.3, 0.2, 0.1, 0.1, 0.1, 'test')
        self.assertEqual(trend_emotion.negative_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_negative_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(
                -1, 1, 0.2, 0.3, 0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_negative_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(1.1, 0, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_negative_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(None, 1, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_negative_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion('test', 1, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    # 'positive_emotion' field

    def test_correct_trend_emotion_creation_min_value_positive_emotion(self):
        trend_emotion = self.create_trend_emotion(1, 0, 0.2, 0.3,
                                                  0.2, 0.1, 0.1, 0.1, 'test')
        self.assertEqual(trend_emotion.positive_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_positive_emotion(self):

        trend_emotion = self.create_trend_emotion(0, 1, 0.2, 0.3,
                                                  0.2, 0.1, 0.1, 0.1, 'test')
        self.assertEqual(trend_emotion.positive_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_positive_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0, -1, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_positive_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0, 1.1, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_positive_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(1, None, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_positive_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(1, 'test', 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    # 'sadness_emotion' field

    def test_correct_trend_emotion_creation_min_value_sadness_emotion(self):

        trend_emotion = self.create_trend_emotion(0.5, 0.5, 0, 0.5,
                                                  0.2, 0.1, 0.1, 0.1, 'test')
        self.assertEqual(trend_emotion.sadness_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_sadness_emotion(self):

        trend_emotion = self.create_trend_emotion(0, 1, 1, 0,
                                                  0, 0, 0, 0, 'test')
        self.assertEqual(trend_emotion.sadness_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_sadness_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, -1, 0.5,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_sadness_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 1.1, 0.5,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_sadness_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, None, 0.5,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_sadness_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 'test', 0.5,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    # 'fear_emotion' field

    def test_correct_trend_emotion_creation_min_value_fear_emotion(self):

        trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0,
                                                  0.2, 0.1, 0.1, 0.1, 'test')
        self.assertEqual(trend_emotion.fear_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_fear_emotion(self):

        trend_emotion = self.create_trend_emotion(0, 1, 0.2, 1,
                                                  0.2, 0.1, 0.1, 0.1, 'test')
        self.assertEqual(trend_emotion.fear_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_fear_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, -1,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_fear_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 1.1,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_fear_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, None,
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_fear_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 'test',
                                                      0.2, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    # 'love_emotion' field

    def test_correct_trend_emotion_creation_min_value_love_emotion(self):

        trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                  0, 0.1, 0.1, 0.1, 'test')
        self.assertEqual(trend_emotion.love_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_love_emotion(self):

        trend_emotion = self.create_trend_emotion(0, 1, 0.2, 0.3,
                                                  1, 0.1, 0.1, 0.1, 'test')
        self.assertEqual(trend_emotion.love_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_love_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      -1, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_love_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      1.1, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_love_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      None, 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_love_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      'test', 0.1, 0.1, 0.1, 'test')
            trend_emotion.full_clean()

    # 'surprise_emotion' field

    def test_correct_trend_emotion_creation_min_value_surprise_emotion(self):

        trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                  0.2, 0, 0.1, 0, 'test')
        self.assertEqual(trend_emotion.surprise_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_surprise_emotion(self):

        trend_emotion = self.create_trend_emotion(0, 1, 0.2, 0.3,
                                                  0.2, 1, 0.1, 0.1, 'test')
        self.assertEqual(trend_emotion.surprise_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_surprise_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, -1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_surprise_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 1.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_surprise_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, None, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_surprise_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 'test', 'test')
            trend_emotion.full_clean()

    # 'anger_emotion' field

    def test_correct_trend_emotion_creation_min_value_anger_emotion(self):

        trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                  0.2, 0.1, 0, 0.1, 'test')
        self.assertEqual(trend_emotion.anger_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_anger_emotion(self):

        trend_emotion = self.create_trend_emotion(0, 1, 0.2, 0.3,
                                                  0.2, 0.1, 1, 0.1, 'test')
        self.assertEqual(trend_emotion.anger_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_anger_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, -1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_anger_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 1.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_anger_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, None, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_anger_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 'test', 'test')
            trend_emotion.full_clean()

    # 'joy_emotion' field

    def test_correct_trend_emotion_creation_min_value_joy_emotion(self):

        trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                  0.2, 0.1, 0.1, 0, 'test')
        self.assertEqual(trend_emotion.joy_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_joy_emotion(self):

        trend_emotion = self.create_trend_emotion(0, 1, 0.2, 0.3,
                                                  0.2, 0.1, 0.1, 1, 'test')
        self.assertEqual(trend_emotion.joy_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_joy_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, -1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_joy_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 1.1, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_joy_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, None, 'test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_joy_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 'test', 'test')
            trend_emotion.full_clean()

    # 'word' field

    def test_correct_trend_emotion_creation_max_length_word(self):

        trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                  0.2, 0.1, 0.1, 0.1, 't'*100)
        self.assertEqual(trend_emotion.word, 't' * 100)

    def test_incorrect_trend_emotion_creation_blank_word(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 0.1, '')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_max_length_word(self):

        with self.assertRaises(Exception):
            self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                      0.2, 0.1, 0.1, 0.1, 't'*101)

    # 'video_id' field

    def test_correct_trend_emotion_creation_max_length_video_id(self):

        trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                  0.2, 0.1, 0.1, 0.1, video_id='t'*30)
        self.assertEqual(trend_emotion.video_id, 't' * 30)

    def test_incorrect_trend_emotion_creation_blank_video_id(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 0.1, video_id='')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_max_length_video_id(self):

        with self.assertRaises(Exception):
            trend_emotion = self.create_trend_emotion(0.5, 0.5, 0.2, 0.3,
                                                      0.2, 0.1, 0.1, 0.1, video_id='t'*31)
            trend_emotion.full_clean()

    #######################################
    ### TrendEmotion model update tests ###
    #######################################

    def test_correct_trend_emotion_update(self):

        self.assert_trend_emotion_attributes(self.trend_emotion)

        self.trend_emotion.negative_emotion = 0.3
        self.trend_emotion.positive_emotion = 0.7
        self.trend_emotion.sadness_emotion = 0.1
        self.trend_emotion.fear_emotion = 0.2
        self.trend_emotion.love_emotion = 0.1
        self.trend_emotion.surprise_emotion = 0.2
        self.trend_emotion.anger_emotion = 0.2
        self.trend_emotion.joy_emotion = 0.2
        self.trend_emotion.word = 'test2'
        self.trend_emotion.save()

        self.assertEqual(self.trend_emotion.negative_emotion, 0.3)
        self.assertEqual(self.trend_emotion.positive_emotion, 0.7)
        self.assertEqual(self.trend_emotion.sadness_emotion, 0.1)
        self.assertEqual(self.trend_emotion.fear_emotion, 0.2)
        self.assertEqual(self.trend_emotion.love_emotion, 0.1)
        self.assertEqual(self.trend_emotion.surprise_emotion, 0.2)
        self.assertEqual(self.trend_emotion.anger_emotion, 0.2)
        self.assertEqual(self.trend_emotion.joy_emotion, 0.2)
        self.assertEqual(self.trend_emotion.word, 'test2')
        self.assertTrue(isinstance(self.trend_emotion, TrendEmotion))
        self.assertEqual(self.trend_emotion.__str__(), 'test2' +
                         '-' + str(self.trend_emotion.insertion_datetime))

    # 'negative_emotion' field

    def test_correct_trend_emotion_update_min_value_negative_emotion(self):

        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)
        self.trend_emotion.negative_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.negative_emotion, 0)

    def test_correct_trend_emotion_update_max_value_negative_emotion(self):

        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)
        self.trend_emotion.negative_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.negative_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_negative_emotion(self):

        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)

        with self.assertRaises(Exception):
            self.trend_emotion.negative_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_negative_emotion(self):

        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)

        with self.assertRaises(Exception):
            self.trend_emotion.negative_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_negative_emotion(self):

        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)

        with self.assertRaises(Exception):
            self.trend_emotion.negative_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_negative_emotion(self):

        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)

        with self.assertRaises(Exception):
            self.trend_emotion.negative_emotion = 'test'
            self.trend_emotion.save()

    # 'positive_emotion' field

    def test_correct_trend_emotion_update_min_value_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.5)
        self.trend_emotion.positive_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 0)

    def test_correct_trend_emotion_update_max_value_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.5)
        self.trend_emotion.positive_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.5)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.5)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.5)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.5)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 'test'
            self.trend_emotion.save()

    # 'sadness_emotion' field

    def test_correct_trend_emotion_update_min_value_sadness_emotion(self):

        self.assertEqual(self.trend_emotion.sadness_emotion, 0.2)
        self.trend_emotion.sadness_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.sadness_emotion, 0)

    def test_correct_trend_emotion_update_max_value_sadness_emotion(self):

        self.assertEqual(self.trend_emotion.sadness_emotion, 0.2)
        self.trend_emotion.sadness_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.sadness_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_sadness_emotion(self):

        self.assertEqual(self.trend_emotion.sadness_emotion, 0.2)

        with self.assertRaises(Exception):
            self.trend_emotion.sadness_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_sadness_emotion(self):

        self.assertEqual(self.trend_emotion.sadness_emotion, 0.2)

        with self.assertRaises(Exception):
            self.trend_emotion.sadness_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_sadness_emotion(self):

        self.assertEqual(self.trend_emotion.sadness_emotion, 0.2)

        with self.assertRaises(Exception):
            self.trend_emotion.sadness_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_sadness_emotion(self):

        self.assertEqual(self.trend_emotion.sadness_emotion, 0.2)

        with self.assertRaises(Exception):
            self.trend_emotion.sadness_emotion = 'test'
            self.trend_emotion.save()

    # 'fear_emotion' field

    def test_correct_trend_emotion_update_min_value_fear_emotion(self):

        self.assertEqual(self.trend_emotion.fear_emotion, 0.3)
        self.trend_emotion.fear_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.fear_emotion, 0)

    def test_correct_trend_emotion_update_max_value_fear_emotion(self):

        self.assertEqual(self.trend_emotion.fear_emotion, 0.3)
        self.trend_emotion.fear_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.fear_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_fear_emotion(self):

        self.assertEqual(self.trend_emotion.fear_emotion, 0.3)

        with self.assertRaises(Exception):
            self.trend_emotion.fear_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_fear_emotion(self):

        self.assertEqual(self.trend_emotion.fear_emotion, 0.3)

        with self.assertRaises(Exception):
            self.trend_emotion.fear_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_fear_emotion(self):

        self.assertEqual(self.trend_emotion.fear_emotion, 0.3)

        with self.assertRaises(Exception):
            self.trend_emotion.fear_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_fear_emotion(self):

        self.assertEqual(self.trend_emotion.fear_emotion, 0.3)

        with self.assertRaises(Exception):
            self.trend_emotion.fear_emotion = 'test'
            self.trend_emotion.save()

    # 'love_emotion' field

    def test_correct_trend_emotion_update_min_value_love_emotion(self):

        self.assertEqual(self.trend_emotion.love_emotion, 0.2)
        self.trend_emotion.love_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.love_emotion, 0)

    def test_correct_trend_emotion_update_max_value_love_emotion(self):

        self.assertEqual(self.trend_emotion.love_emotion, 0.2)
        self.trend_emotion.love_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.love_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_love_emotion(self):

        self.assertEqual(self.trend_emotion.love_emotion, 0.2)

        with self.assertRaises(Exception):
            self.trend_emotion.love_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_love_emotion(self):

        self.assertEqual(self.trend_emotion.love_emotion, 0.2)

        with self.assertRaises(Exception):
            self.trend_emotion.love_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_love_emotion(self):

        self.assertEqual(self.trend_emotion.love_emotion, 0.2)

        with self.assertRaises(Exception):
            self.trend_emotion.love_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_love_emotion(self):

        self.assertEqual(self.trend_emotion.love_emotion, 0.2)

        with self.assertRaises(Exception):
            self.trend_emotion.love_emotion = 'test'
            self.trend_emotion.save()

    # 'surprise_emotion' field

    def test_correct_trend_emotion_update_min_value_surprise_emotion(self):

        self.assertEqual(self.trend_emotion.surprise_emotion, 0.1)
        self.trend_emotion.surprise_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.surprise_emotion, 0)

    def test_correct_trend_emotion_update_max_value_surprise_emotion(self):

        self.assertEqual(self.trend_emotion.surprise_emotion, 0.1)
        self.trend_emotion.surprise_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.surprise_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_surprise_emotion(self):

        self.assertEqual(self.trend_emotion.surprise_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.surprise_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_surprise_emotion(self):

        self.assertEqual(self.trend_emotion.surprise_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.surprise_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_surprise_emotion(self):

        self.assertEqual(self.trend_emotion.surprise_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.surprise_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_surprise_emotion(self):

        self.assertEqual(self.trend_emotion.surprise_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.surprise_emotion = 'test'
            self.trend_emotion.save()

    # 'anger_emotion' field

    def test_correct_trend_emotion_update_min_value_anger_emotion(self):

        self.assertEqual(self.trend_emotion.anger_emotion, 0.1)
        self.trend_emotion.anger_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.anger_emotion, 0)

    def test_correct_trend_emotion_update_max_value_anger_emotion(self):

        self.assertEqual(self.trend_emotion.anger_emotion, 0.1)
        self.trend_emotion.anger_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.anger_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_anger_emotion(self):

        self.assertEqual(self.trend_emotion.anger_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.anger_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_anger_emotion(self):

        self.assertEqual(self.trend_emotion.anger_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.anger_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_anger_emotion(self):

        self.assertEqual(self.trend_emotion.anger_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.anger_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_anger_emotion(self):

        self.assertEqual(self.trend_emotion.anger_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.anger_emotion = 'test'
            self.trend_emotion.save()

    # 'joy_emotion' field

    def test_correct_trend_emotion_update_min_value_joy_emotion(self):

        self.assertEqual(self.trend_emotion.joy_emotion, 0.1)
        self.trend_emotion.joy_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.joy_emotion, 0)

    def test_correct_trend_emotion_update_max_value_joy_emotion(self):

        self.assertEqual(self.trend_emotion.joy_emotion, 0.1)
        self.trend_emotion.joy_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.joy_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_joy_emotion(self):

        self.assertEqual(self.trend_emotion.joy_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.joy_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_joy_emotion(self):

        self.assertEqual(self.trend_emotion.joy_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.joy_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_joy_emotion(self):

        self.assertEqual(self.trend_emotion.joy_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.joy_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_joy_emotion(self):

        self.assertEqual(self.trend_emotion.joy_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.joy_emotion = 'test'
            self.trend_emotion.save()

    # 'word' field

    def test_correct_trend_emotion_update_max_length_word(self):

        self.assertEqual(self.trend_emotion.word, 'test')
        self.trend_emotion.word = 't' * 100
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.word, 't' * 100)

    def test_incorrect_trend_emotion_update_blank_word(self):

        self.assertEqual(self.trend_emotion.word, 'test')

        with self.assertRaises(Exception):
            self.trend_emotion.word = ''
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_max_length_word(self):

        self.assertEqual(self.trend_emotion.word, 'test')

        with self.assertRaises(Exception):
            self.trend_emotion.word = 't' * 101
            self.trend_emotion.save()

    # 'video_id' field

    def test_correct_trend_emotion_update_max_length_video_id(self):

        self.assertEqual(self.trend_emotion.video_id, None)
        self.trend_emotion.video_id = 't' * 30
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.video_id, 't' * 30)

    def test_incorrect_trend_emotion_update_blank_video_id(self):

        self.assertEqual(self.trend_emotion.video_id, None)

        with self.assertRaises(Exception):
            self.trend_emotion.video_id = ''
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_max_length_video_id(self):

        self.assertEqual(self.trend_emotion.video_id, None)

        with self.assertRaises(Exception):
            self.trend_emotion.video_id = 't' * 31
            self.trend_emotion.save()

    #######################################
    ### TrendEmotion model delete tests ###
    #######################################

    def test_correct_trend_emotion_model_delete(self):

        self.assertEqual(TrendEmotion.objects.count(), 1)
        self.trend_emotion.delete()
        self.assertEqual(TrendEmotion.objects.count(), 0)
