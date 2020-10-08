import tweepy 
from credentials import api_key, api_secret_key, access_token, access_token_secret

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.update_status("Tweepy")