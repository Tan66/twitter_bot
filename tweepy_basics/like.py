import tweepy
from credentials import api_key, api_secret_key, access_token, access_token_secret

# Authenticate to twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = api.home_timeline(count=1)
tweet = tweets[0]

# print(f"liking tweet {tweet.id} of {tweet.author.name}")
# api.create_favorite(tweet.id)

print(f"unliking tweet {tweet.id} of {tweet.author.name}")
api.destroy_favorite(tweet.id)