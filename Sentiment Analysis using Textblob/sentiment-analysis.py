from textblob import TextBlob
import tweepy

# Twitter app Credentials
# Consumer API Keys
consumer_key = " "
consumer_secret = ""

# Access token and secret
access_token = " "
access_token_secret = " "

# Complete authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Connecting to the twitter API i.e Signing In to twitter
api = tweepy.API(auth)

# Search for all the tweets containing the word Jollof rice
public_tweets = api.search("Trump")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

