import tweepy
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# Original Tutorial Call 

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_SECRET')


# New Client 

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

# Functional Post

tweet = "API Function Call Test. Alhamdulillah!"
client.create_tweet(text=tweet)
print("Tweet Complete!")

# Output Tweet Confirmation
