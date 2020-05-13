#!/usr/bin/env python
# coding: utf-8

# In[33]:


# - *- coding: utf- 8 - *-
from flask import Flask, render_template, redirect, url_for, request
import requests as rq
from flask_wtf import Form
from wtforms import RadioField
from wtforms import validators, ValidationError
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from nltk.corpus import stopwords
# from google.cloud import translate
from googletrans import Translator
import nltk
import os
import re


# #### Functions defined for web page

# In[35]:


porter_stemmer = nltk.stem.porter.PorterStemmer()

#spilts the sentences into words
def porter_tokenizer(text, stemmer=porter_stemmer):
    lower_txt = text.lower()
    tokens = nltk.wordpunct_tokenize(lower_txt)
    stems = [porter_stemmer.stem(t) for t in tokens]
    no_punct = [s for s in stems if re.match('^[a-zA-Z]+$', s) is not None]
    return no_punct

stop_words = set(stopwords.words('english')) 

#vectorize the data
def vectorizer():
    # Load the model from the file 
    vect = joblib.load(os.getcwd()+'//data//vectorizer.pkl')
    return vect

#with the machine learning model
def classifier():
    # Load the model from the file 
    model_from_joblib = joblib.load(os.getcwd()+'//data//classifier.pkl')
    return model_from_joblib

#for translating a non-english into english
def translate_text(text,target='en'):
    translator = Translator()
#     translate_client = translate.Client()
#     data = translate_client.translate(text,target_language=target)
    result = translator.translate(text, dest = target)
#     result = data['translatedText']
    print(result.text)
    return result.text


# #### Web Application

# In[ ]:


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

#to handle the behavior of an english song
@app.route('/english',methods=['GET','POST']) 
def bynontranslating():
    if request.method =='GET':
        methods='GET'
        return render_template('english.html',methods=methods)
    elif request.method =='POST':
        methods='POST'
        song = request.form['lyrics']
        data = [song]
        vector = vectorizer()
        cleanedtxt = vector.transform(data).toarray()
        model = classifier()
        my_prediction = model.predict(cleanedtxt)
        val = model.predict_proba(cleanedtxt)
        if (val[:,0] > val[:,1]):
            prob = val[:,0]
            prob = round(prob[0]*100,2)
        else:
            prob = val[:,1]
            prob = round(prob[0]*100,2)
        return render_template('english.html', methods=methods,prediction = my_prediction,lyrics=song, probability=prob)

#to handle the behavior of a non-english song
@app.route('/translator',methods=['GET','POST']) 
def bytranslating():
    if request.method =='GET':
        methods='GET'
        return render_template('translator.html',methods=methods)
    elif request.method =='POST':
        methods='POST'
        song = request.form['lyrics']
        transsong = translate_text(song)
        data = [transsong]
#         print(data)
        vector = vectorizer()
#         print(vector)
        cleanedtxt = vector.transform(data).todense()
#         print(cleanedtxt)
        model = classifier()
        my_prediction = model.predict(cleanedtxt)
        val = model.predict_proba(cleanedtxt)
        if (val[:,0] > val[:,1]):
            prob = val[:,0]
            prob = round(prob[0]*100,2)
        else:
            prob = val[:,1]
            prob = round(prob[0]*100,2)
        return render_template('translator.html', methods=methods,prediction = my_prediction,lyrics=song, probability=prob)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
#host='0.0.0.0'

