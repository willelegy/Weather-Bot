# Weather\ Bot/config.py
# This is a python script that will tweet the weather once per hour.
import tweepy
import requests
import logging
import os
import time
from config import create_tweepy_api
from config import create_owm_data


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def new_tweet(owm_data, tweepy_api):
    if owm_data["cod"] != "404":
        x = owm_data["main"]
        # Get the current temperature.
        current_temperature = x["temp"]
        y = owm_data["weather"]
        # Get the current weather conditions.
        weather_description = y[0]["description"]

        logger.info("Creating tweet with the latest weather info")
        # Create a tweet stating the current temperature
        # and weather conditions.
        tweepy_api.update_status(f"The current temperature is "
                          f"{str(current_temperature)} fahrenheit.\n"
                          f"The current conditions are "
                          f"{str(weather_description)}")

    else:
        # Let the user know that the location was not found, per the
        # URL used for the OWM API call.
        logger.info("City Not Found")

def main():
    # Authenticate to Twitter.
    tweepy_api = create_tweepy_api()

    while True:
        # Call the OWM API to get the latest weather data.
        owm_data = create_owm_data()
        # Create a tweet stating the current weather conditions.
        new_tweet(owm_data, tweepy_api)
        logger.info("Waiting")
        # Wait an hour to tweet another weather update.
        time.sleep(3600)

if __name__ == "__main__":
    main()
