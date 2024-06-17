import requests
import json
from constants import get_instagram_headers, instagram_api_url


def get_followers(username: str) -> int:
    try:
        url = f"https://{instagram_api_url}?username={username}"
        res = requests.get(url, headers=get_instagram_headers())
        metadata = json.loads(res.content)
        node = metadata["data"]["user"]["edge_followed_by"]["count"]
        return node

    except:
        return -1
