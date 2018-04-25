# minimal-django-heroku-skeleton

 A lightweight Django server ready for deployment on Heroku.

## Getting Started

Clone this repository: `git clone https://github.com/iSuperMostafa/minimal-django-heroku-skeleton.git`

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
heroku logs
```
