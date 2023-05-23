import requests
from decouple import config
from datetime import datetime
from pytz import timezone
from django.core.exceptions import ObjectDoesNotExist

from main.models import Country, YouTubeTrend, YouTubeTrendType, YouTubeCountryTrend
from utils.apis.twitter import clean_text


def get_country_trends(country_name, trend_type):

    youtube_api_key = config('YOUTUBE_API_KEY')

    try:
        country = Country.objects.get(name=country_name)
        acronym = country.acronym

        if YouTubeTrendType.objects.filter(name=trend_type).exists():
            if trend_type != 'Default':
                category_id = YouTubeTrendType.objects.get(
                    name=trend_type).category_id
                url = ("https://www.googleapis.com/youtube/v3/videos" +
                       "?part=snippet&chart=mostPopular&regionCode=" + acronym +
                       "&videoCategoryId=" + str(category_id) + "&key=" + youtube_api_key)
            else:
                url = ("https://www.googleapis.com/youtube/v3/videos" +
                       "?part=snippet&chart=mostPopular&regionCode=" + acronym +
                       "&key=" + youtube_api_key)

            response = requests.get(url)
            return get_country_trends_aux(response, url, [], 0)
        return []
    except ObjectDoesNotExist:
        return []


def get_country_trends_aux(response, url, res, trends_number):

    res_aux = res.copy()

    if response.status_code == 200 and trends_number < 10:
        data = response.json()
        videos = data['items']

        for video in videos:
            video_id = video['id']
            title = video['snippet']['title'] if 'title' in video['snippet'].keys(
            ) else ''
            published_at = video['snippet']['publishedAt'] if 'publishedAt' in video['snippet'].keys(
            ) else ''
            thumbnail = get_thumbnail_url(
                video) if 'thumbnails' in video['snippet'].keys() else ''
            channel_title = video['snippet']['channelTitle'] if 'channelTitle' in video['snippet'].keys(
            ) else ''
            statistics = get_video_statistics(
                video_id) if 'id' in video.keys() else (None, None, None)
            aux = [video_id, title, published_at,
                   thumbnail, channel_title, statistics]
            res_aux.append(aux)

        if 'nextPageToken' in data.keys():
            page_token = data['nextPageToken']
            url = url.split("&pageToken=")[0] + "&pageToken=" + page_token
            response = requests.get(url)

            return get_country_trends_aux(response, url, res_aux, trends_number + 5)
        else:
            return res
    else:
        return res


def get_thumbnail_url(video):

    thumbnails = video['snippet']['thumbnails']
    thumbnails_keys = video['snippet']['thumbnails'].keys()

    if 'maxres' in thumbnails_keys:
        return thumbnails['maxres']['url']
    if 'standard' in thumbnails_keys:
        return thumbnails['standard']['url']
    elif 'high' in thumbnails_keys:
        return thumbnails['high']['url']
    elif 'medium' in thumbnails_keys:
        return thumbnails['medium']['url']
    elif 'default' in thumbnails_keys:
        return thumbnails['default']['url']
    else:
        return ""


def get_video_statistics(video_id):

    youtube_api_key = config('YOUTUBE_API_KEY')

    url = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id=" + \
        video_id + "&key=" + youtube_api_key
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        views = data['items'][0]['statistics']['viewCount'] if 'viewCount' in data['items'][0]['statistics'].keys(
        ) else None
        likes = data['items'][0]['statistics']['likeCount'] if 'likeCount' in data['items'][0]['statistics'].keys(
        ) else None
        comments = data['items'][0]['statistics']['commentCount'] if 'commentCount' in data['items'][0]['statistics'].keys(
        ) else None

        if views != None:
            views = int(views)
        if likes != None:
            likes = int(likes)
        if comments != None:
            comments = int(comments)

        return views, likes, comments

    else:
        return None, None, None


def load_trending_types():

    if YouTubeTrendType.objects.count() == 0:

        trending_types = {
            "Default": 0,
            "Film & Animation": 1,
            "Music": 10,
            "Sports": 17,
            "Gaming": 20,
            "Entertainment": 24,
            "News & Politics": 25,
            "Science & Technology": 28
        }

        for t in trending_types:
            yt = YouTubeTrendType(name=t, category_id=trending_types[t])
            yt.save()


def load_country_trends(country_name, trend_type):

    load_trending_types()
    trends = get_country_trends(country_name, trend_type)

    if len(trends) > 0:

        country = Country.objects.get(name=country_name)

        if YouTubeTrendType.objects.filter(name=trend_type).exists():
            yt = YouTubeTrendType.objects.get(name=trend_type)

            if YouTubeCountryTrend.objects.filter(country=country, trend_type=yt).exists():
                YouTubeCountryTrend.objects.filter(
                    country=country, trend_type=yt).delete()

            yct = YouTubeCountryTrend(country=country, trend_type=yt)
            yct.save()

            for t in trends:
                yt = YouTubeTrend(video_id=t[0], title=t[1], published_at=timezone("UTC").localize(datetime.strptime(
                    t[2], "%Y-%m-%dT%H:%M:%SZ")), thumbnail=t[3], channel_title=t[4], view_count=t[5][0], like_count=t[5][1], comment_count=t[5][2], country_trend=yct)
                yt.save()

def get_relevant_comments(video_id, number_of_comments, comments_ls, next_page_token=None):

    youtube_api_key = config('YOUTUBE_API_KEY')

    url = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=" + \
        video_id + "&key=" + youtube_api_key
    if next_page_token != None:
        url += "&pageToken=" + next_page_token

    response = requests.get(url)

    if response.status_code == 200:
        if len(comments_ls) >= 50 or (len(comments_ls) > 0 and next_page_token == None):
            
            comments_ls.sort(key=lambda x: x[1], reverse=True)
            return [c for c, l in comments_ls[:number_of_comments]]
        else:
            data = response.json()
            comments = data['items']

            for comment in comments:
                if 'snippet' in comment.keys():
                    comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
                    clean_comment = clean_text(comment_text)
                    if clean_comment != '':
                        comment_likes = comment['snippet']['topLevelComment']['snippet']['likeCount']
                        comments_ls.append((clean_comment, comment_likes))

            return get_relevant_comments(video_id, number_of_comments, comments_ls, data['nextPageToken'] if 'nextPageToken' in data.keys() else None)
    else:
        return comments_ls
