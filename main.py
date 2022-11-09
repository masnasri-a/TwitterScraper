from dotenv import dotenv_values
import tweepy, json

sample = {"created_at": "Wed Nov 09 08:48:56 +0000 2022", "id": 1590265169342771200, "id_str": "1590265169342771200", "full_text": "RT @FoxyDev42: A year ago we moved to SOL due gas. I had no idea how to do develop on SOL but ended up with a custom CM for our mint. It wa\u2026", "truncated": False, "display_text_range": [0, 140], "entities": {"hashtags": [], "symbols": [], "user_mentions": [{"screen_name": "FoxyDev42", "name": "F\ud83d\udfe0xyDev", "id": 1406894233248624647, "id_str": "1406894233248624647", "indices": [3, 13]}], "urls": []}, "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>", "in_reply_to_status_id": null, "in_reply_to_status_id_str": null, "in_reply_to_user_id": null, "in_reply_to_user_id_str": null, "in_reply_to_screen_name": null, "user": {"id": 1433121559057559555, "id_str": "1433121559057559555", "name": "Magic Eden \ud83e\ude84", "screen_name": "MagicEden", "location": "Metaverse", "description": "Pushing boundaries on SOL & ETH. Bae: @coralcubenft Son: @TheMagicDAO", "url": "https://t.co/TM8CKG6WUp", "entities": {"url": {"urls": [{"url": "https://t.co/TM8CKG6WUp", "expanded_url": "http://magiceden.io", "display_url": "magiceden.io", "indices": [0, 23]}]}, "description": {"urls": []}}, "protected": False, "followers_count": 353604, "friends_count": 1713, "listed_count": 1762, "created_at": "Wed Sep 01 17:36:40 +0000 2021", "favourites_count": 49697, "utc_offset": null, "time_zone": null, "geo_enabled": True, "verified": True, "statuses_count": 19094, "lang": null, "contributors_enabled": False, "is_translator": False, "is_translation_enabled": False, "profile_background_color": "F5F8FA", "profile_background_image_url": null, "profile_background_image_url_https": null, "profile_background_tile": False, "profile_image_url": "http://pbs.twimg.com/profile_images/1589735345335181312/aHlPiOCj_normal.jpg", "profile_image_url_https": "https://pbs.twimg.com/profile_images/1589735345335181312/aHlPiOCj_normal.jpg", "profile_banner_url": "https://pbs.twimg.com/profile_banners/1433121559057559555/1667259490", "profile_link_color": "1DA1F2", "profile_sidebar_border_color": "C0DEED", "profile_sidebar_fill_color": "DDEEF6", "profile_text_color": "333333", "profile_use_background_image": True, "has_extended_profile": True, "default_profile": True, "default_profile_image": False, "following": False, "follow_request_sent": False, "notifications": False, "translator_type": "none", "withheld_in_countries": []}, "geo": null, "coordinates": null, "place": null, "contributors": null, "retweeted_status": {"created_at": "Wed Nov 09 03:56:34 +0000 2022", "id": 1590191591091994625, "id_str": "1590191591091994625", "full_text": "A year ago we moved to SOL due gas. I had no idea how to do develop on SOL but ended up with a custom CM for our mint. It was so fun that I quit my job next day to create one of the first NFT staking on SOL. \nI still learn and create new stuff daily. That is what keeps SOL going.", "truncated": False, "display_text_range": [0, 280], "entities": {"hashtags": [], "symbols": [], "user_mentions": [], "urls": []}, "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", "in_reply_to_status_id": null, "in_reply_to_status_id_str": null, "in_reply_to_user_id": null, "in_reply_to_user_id_str": null, "in_reply_to_screen_name": null, "user": {"id": 1406894233248624647, "id_str": "1406894233248624647", "name": "F\ud83d\udfe0xyDev", "screen_name": "FoxyDev42", "location": "BronkySwamp", "description": "Does something something at @FamousFoxFed | Ex BronkDAO head", "url": "https://t.co/F3gGjkOFyq", "entities": {"url": {"urls": [{"url": "https://t.co/F3gGjkOFyq", "expanded_url": "https://famousfoxes.com", "display_url": "famousfoxes.com", "indices": [0, 23]}]}, "description": {"urls": []}}, "protected": False, "followers_count": 8733, "friends_count": 105, "listed_count": 46, "created_at": "Mon Jun 21 08:38:58 +0000 2021", "favourites_count": 2957, "utc_offset": null, "time_zone": null, "geo_enabled": False, "verified": False, "statuses_count": 1711, "lang": null, "contributors_enabled": False, "is_translator": False, "is_translation_enabled": False, "profile_background_color": "F5F8FA", "profile_background_image_url": null, "profile_background_image_url_https": null, "profile_background_tile": False, "profile_image_url": "http://pbs.twimg.com/profile_images/1568856384460193794/7A5cmhE__normal.jpg", "profile_image_url_https": "https://pbs.twimg.com/profile_images/1568856384460193794/7A5cmhE__normal.jpg", "profile_banner_url": "https://pbs.twimg.com/profile_banners/1406894233248624647/1647282576", "profile_link_color": "1DA1F2", "profile_sidebar_border_color": "C0DEED", "profile_sidebar_fill_color": "DDEEF6", "profile_text_color": "333333", "profile_use_background_image": True, "has_extended_profile": True, "default_profile": True, "default_profile_image": False, "following": False, "follow_request_sent": False, "notifications": False, "translator_type": "none", "withheld_in_countries": []}, "geo": null, "coordinates": null, "place": null, "contributors": null, "is_quote_status": False, "retweet_count": 173, "favorite_count": 984, "favorited": False, "retweeted": False, "lang": "en"}, "is_quote_status": False, "retweet_count": 173, "favorite_count": 0, "favorited": False, "retweeted": False, "lang": "en"}

config = dotenv_values('.env')

API_KEY = config.get('API_KEY')
API_SECRET_KEY = config.get('API_SECRET_KEY')

ACCESS_TOKEN = config.get('ACCESS_TOKEN')
ACCESS_SECRET_TOKEN = config.get('ACCESS_SECRET_TOKEN')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)

def mapping(data):
    mappper = {
        "created_at":"",
        "author":"",
        "type":"",
        "post":"",
        "link":""
    }

if __name__ == "__main__":
    # user = api.user_timeline(id='1433121559057559555', count=2,include_rts=True, tweet_mode="extended")
    # for detail in user:
        # _id = (detail._json)
        # print(json.dumps(_id))
        # status = api.get_status(_id, tweet_mode="extended")
        # print(json.dumps(status._json))
        # print("==================")