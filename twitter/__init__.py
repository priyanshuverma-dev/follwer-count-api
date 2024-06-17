import requests
import random
from constants import build_params, USER_AGENTS, default_features


def get_followers(username: str) -> int:
    try:

        headers = {
            "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
            "user-agent": random.choice(USER_AGENTS),
        }

        h = requests.post(
            "https://api.twitter.com/1.1/guest/activate.json", headers=headers
        ).json()

        headers.update(
            {
                "content-type": "application/json",
                "x-guest-token": h["guest_token"],
                "x-twitter-active-user": "yes",
                "referer": "https://twitter.com/",
                "x-csrf-token": "",
                "x-twitter-auth-type": "",
                "x-twitter-client-language": "en",
            }
        )

        params = {
            "variables": {"screen_name": username},
            "features": default_features,
        }

        user = requests.get(
            "https://twitter.com/i/api/graphql/sLVLhk0bGj3MVFEKTdax1w/UserByScreenName",
            params=build_params(params),
            headers=headers,
        ).json()
        count = user["data"]["user"]["result"]["legacy"]["followers_count"]
        return count
    except:
        return -1
