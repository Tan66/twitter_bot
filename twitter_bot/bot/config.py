import tweepy
import os
import logging
from credentials import api_key, api_secret_key, access_token, access_token_secret

logger = logging.getLogger()

def create_api():
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e 
    logger.info("API created")
    return api
