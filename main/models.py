from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator,  MaxValueValidator

# Create your models here.

class Country(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    native_name = models.CharField(max_length=60)
    acronym = models.CharField(validators=[MinLengthValidator(2)], max_length=2)
    flag = models.URLField(max_length=100)
    woeid = models.IntegerField(null=True)
    pn = models.CharField(max_length=30, null=True)
    lat = models.FloatField(null=True, validators=[MinValueValidator(-90), MaxValueValidator(90)])
    lng = models.FloatField(null=True, validators=[MinValueValidator(-180), MaxValueValidator(180)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'id']
        verbose_name_plural = "Countries"

class TwitterTrend(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    tweet_volume = models.IntegerField(null=True)
    country_trend = models.ForeignKey('TwitterCountryTrend', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class TwitterCountryTrend(models.Model):

    id = models.AutoField(primary_key=True)
    insertion_datetime = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.country.name

    class Meta:
        ordering = ['country', 'id']

class GoogleTrend(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country_trend = models.ForeignKey('GoogleCountryTrend', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class GoogleCountryTrend(models.Model):

    id = models.AutoField(primary_key=True)
    insertion_datetime = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.country.name

    class Meta:
        ordering = ['country', 'id']

class GoogleWordTrendPeriod(models.Model):
    
    id = models.AutoField(primary_key=True)
    trend_datetime = models.DateTimeField()
    value = models.SmallIntegerField()
    word_trend = models.ForeignKey('GoogleWordTrend', on_delete=models.CASCADE)

    def __str__(self):
        return self.word_trend.country.name + ' - ' + self.word_trend.word + ' - ' + str(self.trend_datetime)

    class Meta:
        ordering = ['-value', 'id']

class GoogleWordTrend(models.Model):

    id = models.AutoField(primary_key=True)
    insertion_datetime = models.DateTimeField(auto_now_add=True)
    word = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    period_type = models.CharField(max_length=10)

    def __str__(self):
        return self.country.name + ' - ' + self.word

    class Meta:
        ordering = ['country', 'word', 'id']

class GoogleTopic(models.Model):

    id = models.AutoField(primary_key=True)
    topic_title = models.CharField(max_length=100)
    topic_type = models.CharField(max_length=100)
    value = models.SmallIntegerField()
    main_topic = models.ForeignKey('GoogleRelatedTopic', on_delete=models.CASCADE)

    def __str__(self):
        return self.main_topic.word + ' - ' + self.topic_title

    class Meta:
        ordering = ['-value', 'id']

class GoogleRelatedTopic(models.Model):
    
    id = models.AutoField(primary_key=True)
    insertion_datetime = models.DateTimeField(auto_now_add=True)
    word = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    period_type = models.CharField(max_length=10)

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['id']

class YouTubeTrend(models.Model):
    
    id = models.AutoField(primary_key=True)
    video_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    published_at = models.DateTimeField()
    thumbnail = models.URLField(max_length=100)
    view_count = models.BigIntegerField(null=True)
    like_count = models.IntegerField(null=True)
    comment_count = models.IntegerField(null=True)
    channel_title = models.CharField(max_length=100)
    country_trend = models.ForeignKey('YoutubeCountryTrend', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']

class YouTubeTrendType(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category_id = models.SmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class YouTubeCountryTrend(models.Model):

    id = models.AutoField(primary_key=True)
    insertion_datetime = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    trend_type = models.ForeignKey(YouTubeTrendType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.country.name

    class Meta:
        ordering = ['country', 'id']

class TrendEmotion(models.Model):

    id = models.AutoField(primary_key=True)
    negative_emotion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    neutral_emotion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    positive_emotion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    sadness_emotion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    fear_emotion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    love_emotion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    surprise_emotion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    anger_emotion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    joy_emotion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    insertion_datetime = models.DateTimeField(auto_now_add=True)
    word = models.CharField(max_length=100, null=True)
    video_id = models.CharField(max_length=30, null=True)

    def __str__(self):
        if self.video_id:
            return self.video_id + '-' + str(self.insertion_datetime)
        return self.word + '-' + str(self.insertion_datetime)

    class Meta:
        ordering = ['word', 'insertion_datetime', 'id']