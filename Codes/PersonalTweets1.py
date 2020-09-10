#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:50:59 2019

@author: nikhilyadav
"""

from tweepy import OAuthHandler
import tweepy
import json
CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_TOKEN=""
ACCESS_SECRET=""

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
i = 0

jsonFile = open("ArvindPersonal.json",'a')
for status in tweepy.Cursor(api.user_timeline,id='ArvindKejrival').items():
        
    if 'RT @'not in status.text:
    
        
        jsonFile.write(json.dumps(status._json))
        i=i+1
        print(i)
        
