from typing import Union
import instagram
import twitter
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/instagram/{username}")
def read_instagram_follower(username: str):
    followers_count = instagram.get_followers(username)
    return {"count": followers_count}


@app.get("/twitter/{username}")
def read_twitter_follower(username: str):
    followers_count = twitter.get_followers(username)
    return {"count": followers_count}


