import tweepy 
from credentials import api_key, api_secret_key, access_token, access_token_secret
import json

# A listener handles tweets that are received from the stream
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name} : {tweet.text}")
    
    def on_error(self, status):
        print("Error detected") 

#authenticate to twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

# create API object
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

tweet_listener = MyStreamListener(api)
my_stream = tweepy.Stream(api.auth, tweet_listener)
my_stream.filter(track = ['Python', 'Java', 'Kotlin'], languages = ['en'])
