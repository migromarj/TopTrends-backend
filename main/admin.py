from django.contrib import admin
from main.models import Country, TwitterTrend, TwitterCountryTrend, GoogleTrend, GoogleCountryTrend, GoogleWordTrendPeriod, GoogleWordTrend, GoogleTopic, GoogleRelatedTopic, YouTubeTrend, YouTubeCountryTrend, TrendEmotion

# Register your models here.

admin.site.register(Country)
admin.site.register(TwitterTrend)
admin.site.register(TwitterCountryTrend)
admin.site.register(GoogleTrend)
admin.site.register(GoogleCountryTrend)
admin.site.register(GoogleWordTrendPeriod)
admin.site.register(GoogleWordTrend)
admin.site.register(GoogleTopic)
admin.site.register(GoogleRelatedTopic)
admin.site.register(YouTubeTrend)
admin.site.register(YouTubeCountryTrend)
admin.site.register(TrendEmotion)
