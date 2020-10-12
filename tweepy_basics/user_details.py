import tweepy 
from credentials import api_key, api_secret_key, access_token, access_token_secret

# Authentication
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Getting user details

user = api.get_user("twitter")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 10 followers")
for follower in user.followers(count=10):
    print(follower.name)
