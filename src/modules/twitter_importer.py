# This is the twitter import data plugin!
import tweepy as tweepy


class TwitterImporter:
    def __init__(self, api, user_handle):
        self.api = api
        self.user_handle = user_handle

    def import_followers(self, limit=None):
        max_limit = limit if limit and limit > 100 and limit <= 1000 else 200
        followers = tweepy.Cursor(
            self.api.followers, self.user_handle).items(max_limit)
        return followers

    def import_followings(self, limit=None):
        max_limit = limit if limit and limit > 100 and limit <= 1000 else 200
        followings = tweepy.Cursor(
            self.api.friends, self.user_handle).items(max_limit)
        return followings

    def import_user_tweets(self, limit=None):
        max_limit = limit if limit and limit > 100 and limit <= 1000 else 200
        user_tweets = tweepy.Cursor(
            self.api.user_timeline, tweet_mode='extended').items(max_limit)
        return user_tweets
