import tweepy

api_key = "***********************************"
api_key_secret = "*******************************************"
access_token = "****************************************************"
access_token_secret = "*******************************************"

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

crypto_coin = "bitcoin"
search_term = f'{crypto_coin} -filter:retweets'

tweet_cursor = tweepy.Cursor(api.search_tweets, q= search_term, lang="en",
tweet_mode="extended").items(100)

tweets = [tweet.full_text for tweet in tweet_cursor]
print(tweets)





