# Flask Google OAuth 2.0 Template

This is a template project bootstraps a Flask webapp and has user authorization flow with Google accounts.

## Setup

Steps on getting your app to work.

### Local
Setup your development environment (pyenv or virtualenv recommended) and install the requirements.
`pip install -r requirements.txt`

Configure your app in `config_template.py` and save as `config.py`

### Google Developer Portal

Go to [Google's dev console](https://console.developer.google.com) and on the top left nav bar click the drop down and `Create Project`. Go through the flow to create you project, and select it from the drop down.

Next, create your credentials and save the client_secret.json to the root of your project. An excerpt from [Google's dev portal](https://developers.google.com/gmail/api/quickstart/python) is below:
```
Use this wizard to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to credentials.
On the Add credentials to your project page, click the Cancel button.
At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
Select the Credentials tab, click the Create credentials button and select OAuth client ID.
Select the application type Other, enter the name "Gmail API Quickstart", and click the Create button.
Click OK to dismiss the resulting dialog.
Click the file_download (Download JSON) button to the right of the client ID.
Move this file to your working directory and rename it client_secret.json.
```

## Run the App

`python -m run`

## Other Resources

Are you as clueless about oauth2 workflow as I was? Digital Ocean has a great knowledge dump of it. Check it out [here](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2)


