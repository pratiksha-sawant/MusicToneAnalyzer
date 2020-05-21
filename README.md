# Song Mood Analyzer (Sentiment Analysis)
*****************************************
A web application (REST API) built in Flask to take input of song lyrics and classify it’s mood by identifying lyrics as happy/sad with supervised machine learning model.

# Web App
*******************************
https://songmoodanalyzer.herokuapp.com/

## Dataset
************************************************
https://raw.githubusercontent.com/rasbt/musicmood/master/dataset/training/train_lyrics_1000.csv

https://github.com/rasbt/musicmood/blob/master/dataset/validation/valid_lyrics_200.csv

## Models evaluated
****************************************************
•	Logistic Regression

•	Naive Bayes

•	Random Forest

# Installation
****************************************
•	pip install pandas

•	pip install numpy

•	pip install matplotlib

•	pip install seaborn

•	pip install sklearn

•	pip install nltk

•	pip install regex

•	pip install joblib

•	pip install wordcloud

•	pip install googletrans

# Heroku deployment
****************************************
• pip install gunicorn

### Steps

•	create a Procfile which consists of web: gunicorn api.<filename>:<main webapp function>

•	create a requirements.txt i.e. list of all the packages which needs to be installed

•	*note for nltk create a separate file name 'nltk.txt' and list all the nltk packages used in the webapp*

•	create a application on heroku and link it with the git repository

•	select autobuild and autodeploy option while creating the app

•	wait for the program to build on heroku on successful build it the log file show 'Procfile declares types -> web' at the end
  with a link for you application domain





