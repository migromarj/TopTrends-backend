from TopTrends.schema import Query
from django.test.testcases import TestCase
import graphene

class CountriesTestCase(TestCase):

    def test_correct_all_countries(self):

        query = """
            query{
                allCountries{
                    id,
                    name,
                    nativeName,
                    acronym,
                    flag,
                    woeid,
                    pn,
                    lat,
                    lng
                } 
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['allCountries']), 250)

    def test_correct_specific_country(self):

        query = """
            query{
                allCountries(acronym: "ES"){
                    id,
                    name,
                    nativeName,
                    acronym,
                    flag,
                    woeid,
                    pn,
                    lat,
                    lng
                } 
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data['allCountries'][0]['name'], 'Spain') 

    def test_correct_specific_country_not_found(self):

        query = """
            query{
                allCountries(acronym: "AA"){
                    id,
                    name,
                    nativeName,
                    acronym,
                    flag,
                    woeid,
                    pn,
                    lat,
                    lng
                } 
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['allCountries']), 0)

class TwitterTrendsTestCase(TestCase):

    def test_correct_country_defined_trends_number(self):

        query = """
            query{
                countryTwitterTrends(country: "Spain", trendsNumber:10){
                    id,
                    name,
                    url,
                    tweetVolume
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryTwitterTrends']), 10)

        # Make the same query when the result is found in the database

        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryTwitterTrends']), 10)

    def test_correct_country_undefined_trends_number(self):

        query = """
            query{
                countryTwitterTrends(country: "Spain"){
                    id,
                    name,
                    url,
                    tweetVolume
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryTwitterTrends']), 5)

    def test_correct_country_big_trends_number(self):

        query = """
            query{
                countryTwitterTrends(country: "Spain", trendsNumber:500){
                    id,
                    name,
                    url,
                    tweetVolume
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryTwitterTrends']), 25)

    def test_unknown_country(self):

        query = """
            query{
                countryTwitterTrends(country: "Not country"){
                    id,
                    name,
                    url,
                    tweetVolume
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryTwitterTrends']), 0)

class GoogleTrendsTestCase(TestCase):

    def test_correct_country_defined_trends_number(self):

        query = """
            query{
                countryGoogleTrends(country:"United States of America", trendsNumber:10){
                    id,
                    name
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryGoogleTrends']), 10)

        # Make the same query when the result is found in the database

        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryGoogleTrends']), 10)

    def test_correct_country_undefined_trends_number(self):

        query = """
            query{
                countryGoogleTrends(country:"United States of America"){
                    id,
                    name
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryGoogleTrends']), 5)

    def test_correct_country_big_trends_number(self):

        query = """
            query{
                countryGoogleTrends(country:"United States of America", trendsNumber:500){
                    id,
                    name
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryGoogleTrends']), 20)

    def test_unknown_country(self):

        query = """
            query{
                countryGoogleTrends(country:"Not country"){
                    id,
                    name
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryGoogleTrends']), 0)

class WordGoogleTrendsTestCase(TestCase):

    def test_correct_country_daily_period(self):

        query = """
            query{
                wordGoogleTrends(word:"Mercadona", country:"Spain", periodType:"daily"){
                    id,
                    trendDatetime,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)

        # Make the same query when the result is found in the database

        result = schema.execute(query)
        self.assertIsNone(result.errors)

    def test_correct_country_weekly_period(self):

        query = """
            query{
                wordGoogleTrends(word:"Mercadona", country:"Spain", periodType:"weekly"){
                    id,
                    trendDatetime,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)

    def test_correct_country_monthly_period(self):

        query = """
            query{
                wordGoogleTrends(word:"Mercadona", country:"Spain", periodType:"monthly"){
                    id,
                    trendDatetime,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        if not result.errors: # If the error is 429, the test is passed
            self.assertIsNone(result.errors)

    def test_unknow_country(self):

        query = """
            query{
                wordGoogleTrends(word:"Mercadona", country:"Not country", periodType:"daily"){
                    id,
                    trendDatetime,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordGoogleTrends']), 0)

    def test_unknow_period_type(self):
            
            query = """
                query{
                    wordGoogleTrends(word:"Mercadona", country:"Spain", periodType:"Not period type"){
                        id,
                        trendDatetime,
                        value
                    }
                }
            """
    
            schema = graphene.Schema(query=Query)
            result = schema.execute(query)
            self.assertIsNone(result.errors)
            self.assertEqual(len(result.data['wordGoogleTrends']), 0)

class WordRelatedTopicsTestCase(TestCase):

    def test_correct_country_daily_period(self):

        query = """
            {
                wordRelatedTopics(word:"Mercadona", country:"Spain", periodType:"daily", topicsNumber:5){
                    id,
                    topicTitle,
                    topicType,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordRelatedTopics']), 5)

        # Make the same query when the result is found in the database

        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordRelatedTopics']), 5)

    def test_correct_country_weekly_period(self):

        query = """
            {
                wordRelatedTopics(word:"Mercadona", country:"Spain", periodType:"weekly", topicsNumber:5){
                    id,
                    topicTitle,
                    topicType,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordRelatedTopics']), 5)

    def test_correct_country_monthly_period(self):

        query = """
            {
                wordRelatedTopics(word:"Mercadona", country:"Spain", periodType:"monthly", topicsNumber:5){
                    id,
                    topicTitle,
                    topicType,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        if not result.errors: # If the error is 429, the test is passed
            self.assertIsNone(result.errors)
            self.assertEqual(len(result.data['wordRelatedTopics']), 5)

    def test_unknow_country(self):

        query = """
            {
                wordRelatedTopics(word:"Mercadona", country:"Not country", periodType:"daily", topicsNumber:5){
                    id,
                    topicTitle,
                    topicType,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordRelatedTopics']), 0)

    def test_unknow_period_type(self):

        query = """
            {
                wordRelatedTopics(word:"Mercadona", country:"Spain", periodType:"Not period type", topicsNumber:5){
                    id,
                    topicTitle,
                    topicType,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['wordRelatedTopics']), 0)

    def test_unknow_topics_number(self):

        query = """
            {
                wordRelatedTopics(word:"Mercadona", country:"Spain", periodType:"daily"){
                    id,
                    topicTitle,
                    topicType,
                    value
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertLessEqual(len(result.data['wordRelatedTopics']), 10)

class YouTubeTrendsTestCase(TestCase):

    def test_correct_specific_you_tube_video(self):

        query = """
            query{
                countryYouTubeTrends(country:"Spain", trendType:"Default", trendsNumber:5){
                    id,
                    videoId,
                    title
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)
        video_id = result.data['countryYouTubeTrends'][0]['videoId']

        query = f"""
            {{
                youTubeVideo(videoId:"{video_id}"){{
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }}
            }}        
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data['youTubeVideo']['videoId'], video_id)

        # Make the same query when the result is found in the database
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data['youTubeVideo']['videoId'], video_id)

    def test_correct_not_specific_you_tube_video(self):

        query = """
            query{
                youTubeVideo(videoId:"Not video id"){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }        
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data['youTubeVideo'], None)
    
    def test_correct_country_defined_trends_number_default_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Default", trendsNumber:5){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)

        # Make the same query when the result is found in the database

        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)
    
    def test_correct_country_defined_trends_number_film_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Film & Animation", trendsNumber:5){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)
    
    def test_correct_country_defined_trends_number_music_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Music", trendsNumber:5){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)
    
    def test_correct_country_defined_trends_number_sports_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Sports", trendsNumber:5){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)
    
    def test_correct_country_defined_trends_number_gaming_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Gaming", trendsNumber:5){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)

    def test_correct_country_defined_trends_number_entertainment_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Entertainment", trendsNumber:5){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)

    def test_correct_country_defined_trends_number_news_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"News & Politics", trendsNumber:5){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)

    def test_correct_country_defined_trends_number_science_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Science & Technology", trendsNumber:5){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)

    def test_correct_country_big_trends_number(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Default", trendsNumber:500){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 10)

    def test_correct_country_undefined_trends_number(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Default"){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 5)

    def test_unknown_country(self):

        query = """
            query{
                countryYouTubeTrends(country:"Not coutry", trendType:"Default", trendsNumber:50){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 0)
    
    def test_unknown_trend_type(self):

        query = """
            query{
                countryYouTubeTrends(country:"United States of America", trendType:"Not trend type", trendsNumber:5){
                    id,
                    videoId,
                    title,
                    publishedAt,
                    thumbnail,
                    viewCount,
                    likeCount,
                    commentCount,
                    channelTitle
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['countryYouTubeTrends']), 0)

class EmotionsTestCase(TestCase):

    def test_correct_word_trend_emotions(self):

        query = """
            query{
                trendEmotions(word: "Messi"){
                    id,
                    negativeEmotion,
                    neutralEmotion,
                    positiveEmotion,
                    sadnessEmotion,
                    joyEmotion,
                    fearEmotion,
                    loveEmotion,
                    angerEmotion,
                    surpriseEmotion,
                    insertionDatetime,
                    word,
                    videoId
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data['trendEmotions'][0]['word'], 'Messi')
        self.assertEqual(result.data['trendEmotions'][0]['videoId'], None)

        # Make the same query when the result is found in the database

        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data['trendEmotions'][0]['word'], 'Messi')
        self.assertEqual(result.data['trendEmotions'][0]['videoId'], None)

    def test_correct_trend_emotions_word_not_found(self):

        query = """
            query{
                trendEmotions(word: "ABCHJKGJFYDGFHCBHJJ"){
                    id,
                    negativeEmotion,
                    neutralEmotion,
                    positiveEmotion,
                    sadnessEmotion,
                    joyEmotion,
                    fearEmotion,
                    loveEmotion,
                    angerEmotion,
                    surpriseEmotion,
                    insertionDatetime,
                    word
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['trendEmotions']), 0)
        self.assertEqual(result.data['trendEmotions'], [])

    def test_correct_video_id_trend_emotions(self):

        query = """
            query{
                trendEmotions(videoId: "WoE6sG2JBrg"){
                    id,
                    negativeEmotion,
                    neutralEmotion,
                    positiveEmotion,
                    sadnessEmotion,
                    joyEmotion,
                    fearEmotion,
                    loveEmotion,
                    angerEmotion,
                    surpriseEmotion,
                    insertionDatetime,
                    videoId,
                    word
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data['trendEmotions'][0]['videoId'], 'WoE6sG2JBrg')
        self.assertEqual(result.data['trendEmotions'][0]['word'], None)

        # Make the same query when the result is found in the database

        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data['trendEmotions'][0]['videoId'], 'WoE6sG2JBrg')
        self.assertEqual(result.data['trendEmotions'][0]['word'], None)

    def test_correct_trend_emotions_video_id_not_found(self):

        query = """
            query{
                trendEmotions(videoId: "ABCHJKGJFYDGFHCBHJJ"){
                    id,
                    negativeEmotion,
                    neutralEmotion,
                    positiveEmotion,
                    sadnessEmotion,
                    joyEmotion,
                    fearEmotion,
                    loveEmotion,
                    angerEmotion,
                    surpriseEmotion,
                    insertionDatetime,
                    videoId
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['trendEmotions']), 0)
        self.assertEqual(result.data['trendEmotions'], [])

    def test_correct_trend_emotions_word_and_video_id(self):

        query = """
            query{
                trendEmotions(word: "Messi", videoId: "WoE6sG2JBrg"){
                    id,
                    negativeEmotion,
                    neutralEmotion,
                    positiveEmotion,
                    sadnessEmotion,
                    joyEmotion,
                    fearEmotion,
                    loveEmotion,
                    angerEmotion,
                    surpriseEmotion,
                    insertionDatetime,
                    videoId,
                    word
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data['trendEmotions']), 0)
        self.assertEqual(result.data['trendEmotions'], [])