import tweepy
from credentials import api_key, api_secret_key, access_token, access_token_secret

# Authenticate to twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    # api.create_friendship("elonmusk") # follow the user
    api.destroy_friendship("elonmusk") # unfollow the user
    print("Success")
except:
    print("Failed to follow")
