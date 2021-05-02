import tweepy as tweepy
import urllib.request
# Authentication!
# Set up your twitter developer account and get your app authentiction details here
# Class to set up access to api


class Authenticate:
    """
    A class to represent Authenticate.

    ...

    Attributes
    ----------
    access_token: str
        A valid access_token for a given twitter developer
    access_secret: str
        A valid access_secret for a given twitter developer
    consumer_key: str
        A valid consumer_key for a given twitter developer
    consumer_key: str
        A valid consumer_key for a given twitter developer

    Methods
    -------
    connect_to_twitter_OAuth():
        Returns an api class with methods to access twitter endpoints.
    """

    def __init__(self, access_token, access_secret, consumer_key, consumer_secret):
        self.access_token = access_token
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    def connect_to_twitter_OAuth(self):
        '''
        Returns an api class with methods to access twitter endpoints.

                Parameters:

                Returns:
                        api (class): A class with methods to access twitter endpoints.
        '''
        # Test if user is able to access twitter.com
        try:
            urllib.request.urlopen('https://twitter.com')
        except ConnectionError as e:
            raise Exception(e)

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        api = tweepy.API(auth)
        # if api.verify_credentials() == False:
        #     raise Exception("The user credentials are invalid.")
        return api
