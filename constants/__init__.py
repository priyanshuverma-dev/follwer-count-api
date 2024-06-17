from datetime import datetime, timedelta
from random import randint
from uuid import uuid4

import orjson


instagram_api_url = "i.instagram.com/api/v1/users/web_profile_info/"


def get_instagram_headers():
    headers = {
        "User-Agent": "Instagram 273.0.0.16.70 (iPad13,8; iOS 16_3; en_US; en-US; "
        "scale=2.00; 2048x2732; 452417278) AppleWebKit/420+",
        "x-ads-opt-out": "1",
        "x-bloks-is-panorama-enabled": "true",
        "x-bloks-version-id": "01507c21540f73e2216b6f62a11a5b5e51aa85491b72475c080da35b1228ddd6",
        "x-fb-client-ip": "True",
        "x-fb-connection-type": "wifi",
        "x-fb-http-engine": "Liger",
        "x-fb-server-cluster": "True",
        "x-fb": "1",
        "x-ig-abr-connection-speed-kbps": "2",
        "x-ig-app-id": "124024574287414",
        "x-ig-app-locale": "en-US",
        "x-ig-app-startup-country": "US",
        "x-ig-bandwidth-speed-kbps": "0.000",
        "x-ig-capabilities": "36r/F/8=",
        "x-ig-connection-speed": "{}kbps".format(randint(1000, 20000)),
        "x-ig-connection-type": "WiFi",
        "x-ig-device-locale": "en-US",
        "x-ig-mapped-locale": "en-US",
        "x-ig-timezone-offset": str(
            (datetime.now().astimezone().utcoffset() or timedelta(seconds=0)).seconds
        ),
        "x-ig-www-claim": "0",
        "x-pigeon-session-id": str(uuid4()),
        "x-tigon-is-retry": "False",
        "x-whatsapp": "0",
    }
    return headers


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.20",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Safari/605.1.15",
]

default_features = {
    # new
    "c9s_tweet_anatomy_moderator_badge_enabled": True,
    "responsive_web_home_pinned_timelines_enabled": True,
    "blue_business_profile_image_shape_enabled": True,
    "creator_subscriptions_tweet_preview_api_enabled": True,
    "freedom_of_speech_not_reach_fetch_enabled": True,
    "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
    "graphql_timeline_v2_bookmark_timeline": True,
    "hidden_profile_likes_enabled": True,
    "highlights_tweets_tab_ui_enabled": True,
    "interactive_text_enabled": True,
    "longform_notetweets_consumption_enabled": True,
    "longform_notetweets_inline_media_enabled": True,
    "longform_notetweets_rich_text_read_enabled": True,
    "longform_notetweets_richtext_consumption_enabled": True,
    "profile_foundations_tweet_stats_enabled": True,
    "profile_foundations_tweet_stats_tweet_frequency": True,
    "responsive_web_birdwatch_note_limit_enabled": True,
    "responsive_web_edit_tweet_api_enabled": True,
    "responsive_web_enhance_cards_enabled": False,
    "responsive_web_graphql_exclude_directive_enabled": True,
    "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
    "responsive_web_graphql_timeline_navigation_enabled": True,
    "responsive_web_media_download_video_enabled": False,
    "responsive_web_text_conversations_enabled": False,
    "responsive_web_twitter_article_data_v2_enabled": True,
    "responsive_web_twitter_article_tweet_consumption_enabled": False,
    "responsive_web_twitter_blue_verified_badge_is_enabled": True,
    "rweb_lists_timeline_redesign_enabled": True,
    "spaces_2022_h2_clipping": True,
    "spaces_2022_h2_spaces_communities": True,
    "standardized_nudges_misinfo": True,
    "subscriptions_verification_info_verified_since_enabled": True,
    "tweet_awards_web_tipping_enabled": False,
    "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
    "tweetypie_unmention_optimization_enabled": True,
    "verified_phone_label_enabled": False,
    "vibe_api_enabled": True,
    "view_counts_everywhere_api_enabled": True,
}


def build_params(params: dict) -> dict:
    return {k: orjson.dumps(v).decode() for k, v in params.items()}
