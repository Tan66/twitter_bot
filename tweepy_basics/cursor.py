import tweepy 
from credentials import api_key, api_secret_key, access_token, access_token_secret

# Authenticate to twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.home_timeline).items(50):
    print(f"{tweet.user.name} said: {tweet.text}")
