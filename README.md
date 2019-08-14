# DJANGO JUKEBOX APP USING SLACK AND YOUTUBE

### What is this repository for? ###

* Backend code for Jukebox.
* Version 0.1
* Python 3.6.9
* Django 2.2.2

### How do I get set up? ###

Make sure to use a
[virtualenv] for development.


You'll need to install `python3.6`  from the system package
manager.


All Python package dependencies are specified in `requirements.txt`.
You can install those using:

pip install -r requirements.txt

####  Database Configuration Steps ####


*You'll also need to install `postgres-server`.

   sudo apt-get install postgresql-9.6

*And Create databases `jukebox` in postgresql

#### How to run the local server ####

python manage.py runserver


#### Applying migrations ####

python manage.py migrate	

#### Generating a new migrate script  ####

python manage.py makemigrations



####  Slack Account Configuration Steps ####


* Find a bot from slack app ("BOTS") or create an app

* Find the Bot User OAuth Access Token It will be used in the coming steps.

* Install the app to your workspace.

* Add the bot to the channel in which you wish to have your youtube links extracted from.

#### DJANGO CONFIGURATION Steps ####


* Open jukebox/slackvideoapp/management/commands/connect.py and replace "Access token here " with
your Bot User OAuth Access Token (eg xoxb-00000000000-11111111111-hubvdfgfdOzA0En1TQgWPY )
 save file and quit.

#### Post video to App ####

python manage.py connect 

* At same time post youtube video links into the channel which your bot is added .

* Open the HOME PAGE of the app --->  /slackvideo/jukebox/


