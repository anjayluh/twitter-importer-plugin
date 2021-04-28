
# Standard imports
import requests
# External imports
from nose.tools import assert_true, assert_raises
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


def test_connection():
    # Send a request to the API server and store the response.
    response = requests.get('https://twitter.com')
    # Confirm that the request-response cycle completed successfully.
    assert(response.ok)


def test_connect_to_twitter_OAuth():
    authenticate = Authenticate(config.ACCESS_TOKEN, config.ACCESS_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET)
    # if authentication is successful, I epxect an api object.
    api = authenticate.connect_to_twitter_OAuth()
    assert(api.verify_credentials() == True)

def test_connect_to_twitter_OAuth_invalid_token():
    authenticate = Authenticate(config.ACCESS_TOKEN, config.ACCESS_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET)
    api = authenticate.connect_to_twitter_OAuth()
    # if authentication is successful, I epxect an api object.
    assert(api.verify_credentials() == False)
