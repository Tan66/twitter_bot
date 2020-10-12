import tweepy
from credentials import api_key, api_secret_key, access_token, access_token_secret

# Authenticate to twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in api.search(q="Python", lang="en", count=10):    # recent 10 tweets that contains Python
    print(f"{tweet.user.name}: {tweet.text}")