# Flask Google OAuth 2.0 Template

This is a template project bootstraps a Flask webapp and has user authorization flow with Google accounts.

## Setup

Steps on getting your app to work.

### Local
Setup your development environment (pyenv or virtualenv recommended) and install the requirements.

```pip install -r requirements.txt```

Configure your app in `config_template.py` and save as `config.py`

### Google Developer Portal

Go to [Google's dev console](https://console.developer.google.com) and on the top left nav bar click the drop down and `Create Project`. Go through the flow to create you project, and select it from the drop down.

Click `API & Auth > Credentials` on the left sidebar menu, click the `OAuth consent screen` and fill out the info.

Click `Credentials` Tab and add + select `OAuth 2.0 Client ID` credentials. Select `Web application` as the type, name the app anything you want. Set the javascript origins to `http://localhost:5000` and the Authorized redirect URIs to `http://localhost:5000/gCallback` for now. You can create a new set of credentials when you are ready to run on different environments.

After you complete those steps and click `create`, you will have the option to download the json file of the client secrets. Save this file in your root directory as `client_secrets.json`

## Run the App

`python -m run`

## Other Resources

Are you as clueless about oauth2 workflow as I was? Digital Ocean has a great knowledge dump of it. Check it out [here](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2)


