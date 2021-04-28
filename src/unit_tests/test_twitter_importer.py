
import settings
# import twitter_importer
# import authenticate_developer
import requests
from nose.tools import assert_true
import os
import sys
sys.path.append(os.path.abspath('../modules'))
sys.path.append(os.path.abspath('../../'))
""" 
fetch followers for existing handle
fetch followers for none existent handle
fetch friends for existing handle
fetch friends for non existing handle
fetch user timeline for exisitng handle
fetch user timeline for none existing handle
 """

""" authenticate = authenticate_developer.Authenticate(
    settings.ACCESS_TOKEN, settings.ACCESS_SECRET, settings.CONSUMER_KEY, settings.CONSUMER_SECRET)

api = authenticate.connect_to_twitter_OAuth()

"""


""" @patch(twitter_importer.TwitterImporter(api, 'user_handle'))
def test_getting_friends(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)
 """
