import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from main.models import Country, TwitterTrend, TwitterCountryTrend, GoogleTrend, GoogleCountryTrend, GoogleWordTrendPeriod, GoogleWordTrend, GoogleTopic, GoogleRelatedTopic, YouTubeTrend, YouTubeCountryTrend, TrendEmotion

from utils.scraping.twitter import load_country_trends as load_twitter_country_trends
from utils.apis.google_trends import load_country_trends as load_google_country_trends
from utils.apis.google_trends import load_google_word_trend, load_related_topics
from utils.apis.youtube import load_country_trends as load_youtube_country_trends
from utils.aux_functions import setup_countries, setup_words, remove_cache, load_countries
from utils.ai.neural_network import load_trend_emotions


class CountryType(DjangoObjectType):
    class Meta:
        model = Country


class TwitterTrendType(DjangoObjectType):
    class Meta:
        model = TwitterTrend


class GoogleTrendType(DjangoObjectType):
    class Meta:
        model = GoogleTrend


class GoogleWordTrendType(DjangoObjectType):
    class Meta:
        model = GoogleWordTrendPeriod


class RelatedTopic(DjangoObjectType):
    class Meta:
        model = GoogleTopic


class YouTubeTrendType(DjangoObjectType):
    class Meta:
        model = YouTubeTrend


class TrendEmotionType(DjangoObjectType):
    class Meta:
        model = TrendEmotion


class Query(ObjectType):

    all_countries = graphene.List(CountryType, acronym=graphene.String())

    def resolve_all_countries(self, info, **kwargs):

        load_countries()

        acronym = kwargs.get('acronym', None)

        if acronym:
            return Country.objects.filter(acronym=acronym.upper())

        if Country.objects.count() != 66:
            Country.objects.all().delete()
            load_countries()

        return Country.objects.all()

    country_twitter_trends = graphene.List(
        TwitterTrendType, country=graphene.String(), trends_number=graphene.Int())

    def resolve_country_twitter_trends(self, info, **kwargs):

        name, trends_number, filtered_country = setup_countries(kwargs)

        if filtered_country.exists() and Country.objects.get(name=name).woeid != None:

            if TwitterCountryTrend.objects.filter(country__name=name).exists():

                twitter_country_trends = TwitterCountryTrend.objects.get(
                    country__name=name)

                cond_1 = remove_cache(twitter_country_trends)

                if cond_1:
                    load_twitter_country_trends(name)

            else:
                load_twitter_country_trends(name)

            return TwitterTrend.objects.filter(country_trend__country__name=name)[:trends_number]

        return []

    country_google_trends = graphene.List(
        GoogleTrendType, country=graphene.String(), trends_number=graphene.Int())

    def resolve_country_google_trends(self, info, **kwargs):

        name, trends_number, filtered_country = setup_countries(kwargs)

        if filtered_country.exists() and Country.objects.get(name=name).pn != None:

            if GoogleCountryTrend.objects.filter(country__name=name).exists():

                google_country_trends = GoogleCountryTrend.objects.get(
                    country__name=name)

                cond_1 = remove_cache(google_country_trends)

                if cond_1:
                    load_google_country_trends(name)

            else:
                load_google_country_trends(name)

            return GoogleTrend.objects.filter(country_trend__country__name=name)[:trends_number]

        return []

    word_google_trends = graphene.List(GoogleWordTrendType, word=graphene.String(
    ), country=graphene.String(), period_type=graphene.String())

    def resolve_word_google_trends(self, info, **kwargs):

        word, period_type, country_name, filtered_country = setup_words(kwargs)

        if filtered_country.exists():

            if GoogleWordTrend.objects.filter(country__name=country_name, word=word, period_type=period_type).exists():

                google_word_trends = GoogleWordTrend.objects.get(
                    country__name=country_name, word=word, period_type=period_type)

                cond_1 = remove_cache(google_word_trends)

                if cond_1:
                    load_google_word_trend(word, country_name, period_type)

            else:
                load_google_word_trend(word, country_name, period_type)

            aux = GoogleWordTrendPeriod.objects.filter(
                word_trend__country__name=country_name, word_trend__word=word, word_trend__period_type=period_type)

            return sorted(aux, key=lambda x: x.id)

        return []

    word_related_topics = graphene.List(RelatedTopic, word=graphene.String(
    ), country=graphene.String(), period_type=graphene.String(), topics_number=graphene.Int())

    def resolve_word_related_topics(self, info, **kwargs):

        word, period_type, country_name, filtered_country = setup_words(kwargs)
        topics_number = kwargs.get('topics_number', 10)

        if filtered_country.exists():

            if GoogleRelatedTopic.objects.filter(country__name=country_name, word=word, period_type=period_type).exists():

                google_related_topics = GoogleRelatedTopic.objects.get(
                    country__name=country_name, word=word, period_type=period_type)

                cond_1 = remove_cache(google_related_topics)

                if cond_1:
                    load_related_topics(word, country_name, period_type)

            else:
                load_related_topics(word, country_name, period_type)

            return GoogleTopic.objects.filter(main_topic__word=word, main_topic__period_type=period_type, main_topic__country__name=country_name)[:topics_number]

        return []

    you_tube_video = graphene.Field(
        YouTubeTrendType, video_id=graphene.String())

    def resolve_you_tube_video(self, info, **kwargs):

        video_id = kwargs.get('video_id')

        if YouTubeTrend.objects.filter(video_id=video_id).exists():

            return YouTubeTrend.objects.get(video_id=video_id)

        return None

    country_you_tube_trends = graphene.List(YouTubeTrendType, country=graphene.String(
    ), trend_type=graphene.String(), trends_number=graphene.Int())

    def resolve_country_you_tube_trends(self, info, **kwargs):

        name, trends_number, filtered_country = setup_countries(kwargs)
        trend_type = kwargs.get('trend_type')

        if filtered_country.exists():

            if YouTubeCountryTrend.objects.filter(country__name=name, trend_type__name=trend_type).exists():

                youtube_country_trends = YouTubeCountryTrend.objects.get(
                    country__name=name, trend_type__name=trend_type)

                cond_1 = remove_cache(youtube_country_trends)

                if cond_1:
                    load_youtube_country_trends(name, trend_type)

            else:
                load_youtube_country_trends(name, trend_type)

            return YouTubeTrend.objects.filter(country_trend__country__name=name, country_trend__trend_type__name=trend_type)[:trends_number]

        return []

    trend_emotions = graphene.List(
        TrendEmotionType, word=graphene.String(), video_id=graphene.String())

    def resolve_trend_emotions(self, info, **kwargs):

        word = kwargs.get('word')
        video_id = kwargs.get('video_id')

        if word and not video_id:

            if TrendEmotion.objects.filter(word=word).exists():

                trend_emotions = TrendEmotion.objects.get(word=word)
                cond_1 = remove_cache(trend_emotions)

                if cond_1:
                    load_trend_emotions(word, None)

            else:
                load_trend_emotions(word, None)

            return TrendEmotion.objects.filter(word=word)

        elif not word and video_id:

            if TrendEmotion.objects.filter(video_id=video_id).exists():

                trend_emotions = TrendEmotion.objects.get(video_id=video_id)
                cond_1 = remove_cache(trend_emotions)

                if cond_1:
                    load_trend_emotions(None, video_id)

            else:
                load_trend_emotions(None, video_id)

            return TrendEmotion.objects.filter(video_id=video_id)

        return []


schema = graphene.Schema(query=Query)
