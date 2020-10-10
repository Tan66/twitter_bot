import tweepy
from credentials import api_key, api_secret_key, access_token, access_token_secret

# Authenticate to twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

trends_result = api.trends_place(1)
# print(trends_result)
for trend in trends_result[0]['trends']:
    print(trend['name'])

