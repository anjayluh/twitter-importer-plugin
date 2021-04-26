# This is the twitter import data plugin!
import tweepy as tweepy


class TwitterImporter:
    """
    A class to represent a TwitterImporter.

    ...

    Attributes
    ----------
    api: class
        A class with methods to access twitter endpoints.
    user_handle: str
        A twitter user handle from which to import data

    Methods
    -------
    import_followers(limit=None):
        Returns the followers of a given user handle.
    import_followings(limit=None):
        Returns the followings of a given user handle.
    import_user_tweets(limit=None):
        Returns the user_tweets of a given user handle.
    """

    def __init__(self, api, user_handle):
        self.api = api
        self.user_handle = user_handle

    def import_followers(self, limit=None):
        '''
        Returns the followers of a given user handle.

                Parameters:
                        limit (int): A integer.

                Returns:
                        followers (str): An object of followers.
        '''
        max_limit = limit if limit and limit > 0 and limit <= 200 else 200
        followers = tweepy.Cursor(
            self.api.followers, self.user_handle).items(max_limit)
        return followers

    def import_followings(self, limit=None):
        '''
        Returns the followings of a given user handle.

                Parameters:
                        limit (int): A integer.

                Returns:
                        followings (str): An object of followers.
        '''
        max_limit = limit if limit and limit > 0 and limit <= 200 else 200
        followings = tweepy.Cursor(
            self.api.friends, self.user_handle).items(max_limit)
        return followings

    def import_user_tweets(self, limit=None):
        '''
        Returns the user_tweets of a given user handle.

                Parameters:
                        limit (int): A integer.

                Returns:
                        user_tweets (str): An object of followers.
        '''
        max_limit = limit if limit and limit > 0 and limit <= 200 else 200
        user_tweets = tweepy.Cursor(
            self.api.user_timeline, tweet_mode='extended').items(max_limit)
        return user_tweets
