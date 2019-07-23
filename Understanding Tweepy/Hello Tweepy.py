"""
This example will download your home timeline tweets and print each one of their texts to the console.
Twitter requires all requests to use OAuth for authentication.
"""
import tweepy

# Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Connecting to the twitter API i.e Signing In to twitter
api = tweepy.API(auth)

# Obtaining tweets from the home timeline
public_tweets = api.home_timeline()

# Looping through the tweets and printing.
for tweet in public_tweets:
    print(tweet)
