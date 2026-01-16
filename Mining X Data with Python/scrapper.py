import tweepy

client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAIow7AEAAAAAhjrRoXZE%2FY9YTS5c3mlg1%2Bpuecg%3DpqnAaUoWa7vOLXnLwvX1tMcQcRJlItMrP4q8yfj4TgdHYlTh0l")

# Get your user ID first
user = client.get_user(username="thales_ke")  # Replace with your Twitter handle
user_id = user.data.id

# Fetch tweets from your home timeline (v2 equivalent)
tweets = client.get_users_tweets(
    id=user_id,
    max_results=10
)

for tweet in tweets.data:
    print(tweet.text)
