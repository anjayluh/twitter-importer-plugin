
# Standard library imports...
from unittest.mock import Mock, patch
import requests
# Third-party imports...
from nose.tools import assert_is_not_none, assert_raises, assert_true, assert_is_none
# Local imports
import os
import sys
sys.path.append(os.path.abspath('../modules'))
sys.path.append(os.path.abspath('../../'))
import settings
import twitter_importer
import authenticate_developer


""" 
fetch followers for existing handle
fetch followers for none existent handle
fetch friends for existing handle
fetch friends for non existing handle
fetch user timeline for exisitng handle
fetch user timeline for none existing handle
 """

authenticate = authenticate_developer.Authenticate(
    settings.ACCESS_TOKEN, settings.ACCESS_SECRET, settings.CONSUMER_KEY, settings.CONSUMER_SECRET)

api = authenticate.connect_to_twitter_OAuth()


def test_getting_followers_with_existing_handle():
    twitter_importer = twitter_importer.TwitterImporter(api, 'realdonaldtrump')
    followers = twitter_importer.import_followers()
    assert_is_not_none(followers)

def test_getting_followers_with_non_existing_handle():
    twitter_importer = twitter_importer.TwitterImporter(api, 'no handle')
    followers = twitter_importer.import_followers()
    assert_is_none(followers)

def test_getting_followings_with():
    twitter_importer = twitter_importer.TwitterImporter(api, 'realdonaldtrump')
    friends = twitter_importer.import_followings()
    assert_is_not_none(followers)

def test_getting_followings_with_non_existing_handle():
    twitter_importer = twitter_importer.TwitterImporter(api, 'no handle')
    followings = twitter_importer.import_followings()
    assert_is_none(followings)

def test_getting_user_tweets_with():
    twitter_importer = twitter_importer.TwitterImporter(api, 'realdonaldtrump')
    friends = twitter_importer.import_friends()
    assert_is_not_none(followers)

def test_getting_user_tweets_with_non_existing_handle():
    twitter_importer = twitter_importer.TwitterImporter(api, 'no handle')
    user_tweets = twitter_importer.import_user_tweets()
    assert_is_none(user_tweets)
