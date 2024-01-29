import tweepy

# Replace with your actual Bearer Token


client = tweepy.Client(bearer_token=bearer_token)

# Replace 'twitterdev' with the username you want to get tweets from
username = 'realDonaldTrump'

# Fetch the user ID
user = client.get_user(username=username)
user_id = user.data.id

# Fetch recent tweets from the user
tweets = client.get_users_tweets(id=user_id, max_results=5)

for tweet in tweets.data:
    print(tweet.text)