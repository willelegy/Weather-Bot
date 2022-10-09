# Weather\ Bot/config.py
# This is the config file for the weather bot in this directory.
import tweepy
import requests
import logging
import os


logger = logging.getLogger()

def create_tweepy_api():
    # Use os.getenv to get definitions that were 
    # exported in the terminal.
    twitter_api_key = os.getenv("TWITTER_API_KEY")
    twitter_api_secret = os.getenv("TWITTER_API_SECRET")
    twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    twitter_access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
    # Authenticate to the twitter API.
    auth.set_access_token(twitter_access_token, twitter_access_token_secret)
    # Create the object that will be used to make calls to 
    # the Twitter API.
    tweepy_api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        # Verify the twitter credentials.
        tweepy_api.verify_credentials()
    except Exception as e:
        # Let the user know that the Twitter credentials failed
        # to verify.
        logger.error("Error creating Tweepy API", exc_info=True)
        raise e

    logger.info("Tweepy API created")
    return tweepy_api

def create_owm_data():
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # Use os.getenv to get definitions that were
    # exported in the terminal
    owm_api_key = os.getenv("OWM_API_KEY")
    zip_code = os.getenv("ZIP_CODE")
    country_code = os.getenv("COUNTRY_CODE")
    # Create the URL used for OWM API calls.
    complete_url = (f"{base_url}appid={owm_api_key}&zip={zip_code},"
                    f"{country_code}&units=imperial")
    # Create object containing data from the most recent 
    # OWM API call.
    response = requests.get(complete_url)
    # Create a json object of the most recent OWM API call.
    owm_data = response.json()
    return owm_data
