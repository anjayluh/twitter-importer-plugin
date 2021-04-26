import tweepy as tweepy
# Authentication!
# Set up your twitter developer account and get your app authentiction details here
# Class to set up access to api


class Authenticate:
    def __init__(self, access_token, access_secret, consumer_key, consumer_secret):
        self.access_token = access_token
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    def connect_to_twitter_OAuth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        api = tweepy.API(auth)
        if api.verify_credentials() == False:
            raise Exception("The user credentials are invalid.")
        return api
