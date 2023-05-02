from django.test import TestCase
from main.models import TrendEmotion

# Tests of the TrendEmotion model


class TrendEmotionModelTestCase(TestCase):

    def assert_trend_emotion_attributes(self, trend_emotion):
        self.assertEqual(TrendEmotion.objects.count(), 1)
        self.assertEqual(self.trend_emotion.negative_emotion, 0.5)
        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)
        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
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

    def setUp(self):

        self.trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                         neutral_emotion=0.4,
                                                         positive_emotion=0.1,
                                                         sadness_emotion=0.2,
                                                         fear_emotion=0.3,
                                                         love_emotion=0.2,
                                                         surprise_emotion=0.1,
                                                         anger_emotion=0.1,
                                                         joy_emotion=0.1,
                                                         word='test')

    #########################################
    ### TrendEmotion model creation tests ###
    #########################################

    def test_correct_trend_emotion_model_creation(self):

        self.assert_trend_emotion_attributes(self.trend_emotion)

    # 'negative_emotion' field

    def test_correct_trend_emotion_creation_min_value_negative_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0,
                                                    neutral_emotion=0.4,
                                                    positive_emotion=0.6,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.negative_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_negative_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=1,
                                                    neutral_emotion=0,
                                                    positive_emotion=0,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.negative_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_negative_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=-1,
                                                        neutral_emotion=0.4,
                                                        positive_emotion=0.6,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_negative_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=1.1,
                                                        neutral_emotion=0.4,
                                                        positive_emotion=0.6,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_negative_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=None,
                                                        neutral_emotion=0.4,
                                                        positive_emotion=0.6,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_negative_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion='test',
                                                        neutral_emotion=0.4,
                                                        positive_emotion=0.6,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    # 'neutral_emotion' field

    def test_correct_trend_emotion_creation_min_value_neutral_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                    neutral_emotion=0,
                                                    positive_emotion=0.5,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.neutral_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_neutral_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0,
                                                    neutral_emotion=1,
                                                    positive_emotion=0,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.neutral_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_neutral_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=-1,
                                                        positive_emotion=0.5,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_neutral_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=1.1,
                                                        positive_emotion=0.5,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_neutral_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=None,
                                                        positive_emotion=0.5,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_neutral_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion='test',
                                                        positive_emotion=0.5,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    # 'positive_emotion' field

    def test_correct_trend_emotion_creation_min_value_positive_emotion(self):
        trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                    neutral_emotion=0.5,
                                                    positive_emotion=0,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.positive_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_positive_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0,
                                                    neutral_emotion=0,
                                                    positive_emotion=1,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.positive_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_positive_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=-1,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_positive_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=1.1,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_positive_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=None,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_positive_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion='test',
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    # 'sadness_emotion' field

    def test_correct_trend_emotion_creation_min_value_sadness_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                    neutral_emotion=0.5,
                                                    positive_emotion=0,
                                                    sadness_emotion=0,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.sadness_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_sadness_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0,
                                                    neutral_emotion=0,
                                                    positive_emotion=1,
                                                    sadness_emotion=1,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.sadness_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_sadness_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=-1,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_sadness_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=1.1,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_sadness_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=None,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_sadness_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion='test',
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    # 'fear_emotion' field

    def test_correct_trend_emotion_creation_min_value_fear_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                    neutral_emotion=0.5,
                                                    positive_emotion=0,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.fear_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_fear_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0,
                                                    neutral_emotion=0,
                                                    positive_emotion=1,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=1,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.fear_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_fear_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=-1,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_fear_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=1.1,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_fear_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=None,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_fear_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion='test',
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    # 'love_emotion' field

    def test_correct_trend_emotion_creation_min_value_love_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                    neutral_emotion=0.5,
                                                    positive_emotion=0,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.love_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_love_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0,
                                                    neutral_emotion=0,
                                                    positive_emotion=1,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=1,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.love_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_love_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=-1,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_love_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=1.1,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_love_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=None,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_love_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion='test',
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    # 'surprise_emotion' field

    def test_correct_trend_emotion_creation_min_value_surprise_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                    neutral_emotion=0.5,
                                                    positive_emotion=0,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.surprise_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_surprise_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0,
                                                    neutral_emotion=0,
                                                    positive_emotion=1,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.surprise_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_surprise_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=-1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_surprise_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=1.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_surprise_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=None,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_surprise_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion='test',
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    # 'anger_emotion' field

    def test_correct_trend_emotion_creation_min_value_anger_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                    neutral_emotion=0.5,
                                                    positive_emotion=0,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.anger_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_anger_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0,
                                                    neutral_emotion=0,
                                                    positive_emotion=1,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=1,
                                                    joy_emotion=0.1,
                                                    word='test')
        self.assertEqual(trend_emotion.anger_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_anger_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=-1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_anger_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=1.1,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_anger_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=None,
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_anger_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion='test',
                                                        joy_emotion=0.1,
                                                        word='test')
            trend_emotion.full_clean()

    # 'joy_emotion' field

    def test_correct_trend_emotion_creation_min_value_joy_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                    neutral_emotion=0.5,
                                                    positive_emotion=0,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0,
                                                    word='test')
        self.assertEqual(trend_emotion.joy_emotion, 0)

    def test_correct_trend_emotion_creation_max_value_joy_emotion(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0,
                                                    neutral_emotion=0,
                                                    positive_emotion=1,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=1,
                                                    word='test')
        self.assertEqual(trend_emotion.joy_emotion, 1)

    def test_incorrect_trend_emotion_creation_negative_joy_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=-1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_greater_than_one_joy_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=1.1,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_without_joy_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=None,
                                                        word='test')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_not_float_joy_emotion(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion='test',
                                                        word='test')
            trend_emotion.full_clean()

    # 'word' field

    def test_correct_trend_emotion_creation_max_length_word(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                    neutral_emotion=0.5,
                                                    positive_emotion=0,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    word='t'*100)
        self.assertEqual(trend_emotion.word, 't' * 100)

    def test_incorrect_trend_emotion_creation_blank_word(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        word='')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_max_length_word(self):

        with self.assertRaises(Exception):
            TrendEmotion.objects.create(negative_emotion=0.5,
                                        neutral_emotion=0.5,
                                        positive_emotion=0,
                                        sadness_emotion=0.2,
                                        fear_emotion=0.3,
                                        love_emotion=0.2,
                                        surprise_emotion=0.1,
                                        anger_emotion=0.1,
                                        joy_emotion=0.1,
                                        word='t'*101)

    # 'video_id' field

    def test_correct_trend_emotion_creation_max_length_video_id(self):

        trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                    neutral_emotion=0.5,
                                                    positive_emotion=0,
                                                    sadness_emotion=0.2,
                                                    fear_emotion=0.3,
                                                    love_emotion=0.2,
                                                    surprise_emotion=0.1,
                                                    anger_emotion=0.1,
                                                    joy_emotion=0.1,
                                                    video_id='t'*30)
        self.assertEqual(trend_emotion.video_id, 't' * 30)

    def test_incorrect_trend_emotion_creation_blank_video_id(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        video_id='')
            trend_emotion.full_clean()

    def test_incorrect_trend_emotion_creation_max_length_video_id(self):

        with self.assertRaises(Exception):
            trend_emotion = TrendEmotion.objects.create(negative_emotion=0.5,
                                                        neutral_emotion=0.5,
                                                        positive_emotion=0,
                                                        sadness_emotion=0.2,
                                                        fear_emotion=0.3,
                                                        love_emotion=0.2,
                                                        surprise_emotion=0.1,
                                                        anger_emotion=0.1,
                                                        joy_emotion=0.1,
                                                        video_id='t'*31)
            trend_emotion.full_clean()

    #######################################
    ### TrendEmotion model update tests ###
    #######################################

    def test_correct_trend_emotion_update(self):

        self.assert_trend_emotion_attributes(self.trend_emotion)

        self.trend_emotion.negative_emotion = 0.3
        self.trend_emotion.neutral_emotion = 0.6
        self.trend_emotion.positive_emotion = 0.1
        self.trend_emotion.sadness_emotion = 0.1
        self.trend_emotion.fear_emotion = 0.2
        self.trend_emotion.love_emotion = 0.1
        self.trend_emotion.surprise_emotion = 0.2
        self.trend_emotion.anger_emotion = 0.2
        self.trend_emotion.joy_emotion = 0.2
        self.trend_emotion.word = 'test2'
        self.trend_emotion.save()

        self.assertEqual(self.trend_emotion.negative_emotion, 0.3)
        self.assertEqual(self.trend_emotion.neutral_emotion, 0.6)
        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
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

    # 'neutral_emotion' field

    def test_correct_trend_emotion_update_min_value_neutral_emotion(self):

        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)
        self.trend_emotion.neutral_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.neutral_emotion, 0)

    def test_correct_trend_emotion_update_max_value_neutral_emotion(self):

        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)
        self.trend_emotion.neutral_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.neutral_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_neutral_emotion(self):

        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)

        with self.assertRaises(Exception):
            self.trend_emotion.neutral_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_neutral_emotion(self):

        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)

        with self.assertRaises(Exception):
            self.trend_emotion.neutral_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_neutral_emotion(self):

        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)

        with self.assertRaises(Exception):
            self.trend_emotion.neutral_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_neutral_emotion(self):

        self.assertEqual(self.trend_emotion.neutral_emotion, 0.4)

        with self.assertRaises(Exception):
            self.trend_emotion.neutral_emotion = 'test'
            self.trend_emotion.save()

    # 'positive_emotion' field

    def test_correct_trend_emotion_update_min_value_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 0)

    def test_correct_trend_emotion_update_max_value_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_positive_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 'test'
            self.trend_emotion.save()

    # 'sadness_emotion' field

    def test_correct_trend_emotion_update_min_value_sadness_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 0)

    def test_correct_trend_emotion_update_max_value_sadness_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_sadness_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_sadness_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_sadness_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_sadness_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 'test'
            self.trend_emotion.save()

    # 'fear_emotion' field

    def test_correct_trend_emotion_update_min_value_fear_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 0)

    def test_correct_trend_emotion_update_max_value_fear_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_fear_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_fear_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_fear_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_fear_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 'test'
            self.trend_emotion.save()

    # 'love_emotion' field

    def test_correct_trend_emotion_update_min_value_love_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 0)

    def test_correct_trend_emotion_update_max_value_love_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_love_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_love_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_love_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_love_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 'test'
            self.trend_emotion.save()

    # 'surprise_emotion' field

    def test_correct_trend_emotion_update_min_value_surprise_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 0)

    def test_correct_trend_emotion_update_max_value_surprise_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_surprise_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_surprise_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_surprise_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_surprise_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 'test'
            self.trend_emotion.save()

    # 'anger_emotion' field

    def test_correct_trend_emotion_update_min_value_anger_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 0)

    def test_correct_trend_emotion_update_max_value_anger_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_anger_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_anger_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_anger_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_anger_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 'test'
            self.trend_emotion.save()

    # 'joy_emotion' field

    def test_correct_trend_emotion_update_min_value_joy_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 0
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 0)

    def test_correct_trend_emotion_update_max_value_joy_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)
        self.trend_emotion.positive_emotion = 1
        self.trend_emotion.save()
        self.assertEqual(self.trend_emotion.positive_emotion, 1)

    def test_incorrect_trend_emotion_update_negative_joy_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = -0.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_greater_than_one_joy_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 1.1
            self.trend_emotion.full_clean()

    def test_incorrect_trend_emotion_update_without_joy_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = None
            self.trend_emotion.save()

    def test_incorrect_trend_emotion_update_not_float_joy_emotion(self):

        self.assertEqual(self.trend_emotion.positive_emotion, 0.1)

        with self.assertRaises(Exception):
            self.trend_emotion.positive_emotion = 'test'
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
