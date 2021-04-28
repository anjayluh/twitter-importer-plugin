
import authenticate_developer
import requests
from nose.tools import assert_true
import os
import sys
sys.path.append(os.path.abspath('../modules'))


def test_connection():
    # Send a request to the API server and store the response.
    response = requests.get('https://twitter.com')

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)


def test_connect_to_twitter_OAuth():
    authenticate = authenticate_developer.Authenticate(
        ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    # if authentication is successful, I epxect an api object.
    assert_is_not_none(authenticate)


def test_connect_to_twitter_OAuth():
    authenticate = authenticate_developer.Authenticate(
        ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    api = authenticate.connect_to_twitter_OAuth()
    # if authentication is successful, I epxect an api object.
    assert_is_not_none(api)
