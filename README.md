# Twitter importer plugin

This is a a plugin to import user data from their twitter account using their handle

## How to run project

Clone this repository
Install jupyter notebooks
Download [Anaconda](https://www.continuum.io/downloads). This project is using anaconda 3.5.
Install the version of Anaconda which you downloaded, following the instructions on the download page.

To run the notebook. cd into the project directory and run **jupyter notebook**

### To run the importer plugin

First, you need to create an account with twitter developer [here](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)

Once you have a developer account, get your api credentials listed below

- ACCESS_TOKEN
- ACCESS_SECRET
- CONSUMER_KEY
- CONSUMER_SECRET

#### Note that these maybe named differently depending on the version of the api

Use this to guide you on the naming

##### Client credentials:

    App Key === API Key === Consumer API Key === Consumer Key === Customer Key === oauth_consumer_key
    App Key Secret === API Secret Key === Consumer Secret === Consumer Key === Customer Key === oauth_consumer_secret
    Callback URL === oauth_callback

##### Token credentials:

    Access token === Token === resulting oauth_token
    Access token secret === Token Secret === resulting oauth_token_secret

Open main.ipynb and fill in the above attained API credentials
Run the connect to twitter notebook.
If the above step runs successfully, you are set set to try out the different import functions from the importer class
