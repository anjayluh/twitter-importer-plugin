
# Standard imports
import requests
# External imports
from nose.tools import assert_true, assert_raises
# External imports
import os
import sys
sys.path.append(os.path.abspath('../modules'))
import authenticate_developer
import settings


def test_connection():
    # Send a request to the API server and store the response.
    response = requests.get('https://twitter.com')

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)


def test_connect_to_twitter_OAuth():
    authenticate = authenticate_developer.Authenticate(
        ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    # if authentication is successful, I epxect an api object.
    api = authenticate.connect_to_twitter_OAuth()
    assert_true(api.verify_credentials() == True)

def test_connect_to_twitter_OAuth_invalid_token():
    authenticate = authenticate_developer.Authenticate(
        ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    # if authentication is successful, I epxect an api object.
    assert_true(api.verify_credentials() == False)
