# minimal-django-heroku-skeleton

 A lightweight Django server ready for deployment on Heroku.

## Getting Started

Clone this repository: `git clone https://github.com/iSuperMostafa/facebook-messenger-bot-skeleton.git`

## Setup the environment

1. Create virtualenv: `virtualenv env`
2. Activate env: `source env/bin/activate`
3. Install pipenv: `pip install pipenv`
4. Install requirements: `pipenv install`

## Run the application locally

Run the server: `gunicorn app.wsgi`

## Start with Heroku

Signup to Heroku [here](https://signup.heroku.com/).

## Install Heroku-CLI

```bash
sudo apt-get update
sudo apt-get install ruby-full
sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install heroku
heroku login
```

## Deploy to Heroku

```bash
heroku create --buildpack heroku/python
heroku config:set DISABLE_COLLECTSTATIC=1
git push heroku master
heroku config:add VERIFY_TOKEN=your_verification_token_here
heroku config:add PAGE_ACCESS_TOKEN=your_page_token_here
heroku logs
```

## Create Facebook Messenger App

1. Create Facebook App [here](https://developers.facebook.com/quickstarts/).
2. Generate a Page Access Token.
3. Setup Webhook
    - Callback URL - The Heroku (or other) URL that we setup earlier.
    - Verification Token - A random secret value that will be sent to your bot.
    - Subscription Fields - This tells Facebook what messaging events you care about and want it to notify. your webhook about. If you're not sure, just start with "messages," as you can change this later.
    then you need to subscribe to the specific page you want to receive message notifications for.
4. Upload a privacy policy.
5. Go to the Facebook Page you created and click on “Message” button, and Start Chatting with Your Bot.