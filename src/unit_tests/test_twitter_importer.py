
# Standard library imports...
import requests
# Third-party imports...
import pytest
# from nose.tools import assert_is_not_none, assert_raises, assert_true, assert_is_none
# Local imports
import os,sys,inspect
sys.path.append(os.path.abspath('../modules'))
sys.path.append(os.path.abspath('../'))
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import config
from modules.twitter_importer import TwitterImporter
from modules.authenticate_developer import Authenticate


""" 
fetch followers for existing handle
fetch followers for none existent handle
fetch friends for existing handle
fetch friends for non existing handle
fetch user timeline for exisitng handle
fetch user timeline for none existing handle
 """

authenticate = Authenticate(
    config.ACCESS_TOKEN, config.ACCESS_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET)

api = authenticate.connect_to_twitter_OAuth()


def test_getting_followers_with_existing_handle():
    twitter_importer = TwitterImporter(api, 'realdonaldtrump')
    followers = twitter_importer.import_followers()
    assert(followers) is not None

def test_getting_followers_with_non_existing_handle():
    twitter_importer = TwitterImporter(api, 'no handle')
    followers = twitter_importer.import_followers()
    assert(followers) is not None

def test_getting_followings_with():
    twitter_importer = TwitterImporter(api, 'realdonaldtrump')
    friends = twitter_importer.import_followings()
    assert(friends) is not None

def test_getting_followings_with_non_existing_handle():
    twitter_importer = TwitterImporter(api, 'no handle')
    followings = twitter_importer.import_followings()
    assert(followings)

def test_getting_user_tweets_with():
    twitter_importer = TwitterImporter(api, 'realdonaldtrump')
    user_tweets = twitter_importer.import_user_tweets()
    assert(user_tweets) is not None

def test_getting_user_tweets_with_non_existing_handle():
    twitter_importer = TwitterImporter(api, 'no handle')
    user_tweets = twitter_importer.import_user_tweets()
    assert(user_tweets) is not None


if __name__ == "__main__":
	unittest.main()