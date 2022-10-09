This is a python script that uses Open Weather maps and Tweepy to tweet the 
weather once per hour. To use this script you will need a twitter developer 
account and an Open Weather Maps account. With the current configuration this 
will only work for locations in the US because OWM only supports zipcodes in 
the US.

You will need to supply environmental variables which include:
"TWITTER_API_KEY", "TWITTER_API_SECRET", "TWITTER_ACCESS_TOKEN", 
"TWITTER_ACCESS_TOKEN_SECRET", "OWM_API_KEY", "ZIP_CODE", "COUNTRY_CODE"
