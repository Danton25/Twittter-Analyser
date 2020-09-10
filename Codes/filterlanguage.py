
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

with open ("ArvindKejriwal.json",'r') as a:
    
    alltweets = a.readlines()
    
    for line in alltweets:

             
            content = json.loads(line)
            #x= p.parse(content["text"])
            
            lang = content["lang"]
            
            if lang == "pt" or lang == "hi" or lang == "en":
                
                
                with open("ArvindKejriwalLanguage.json", 'a') as af:
                    
                    json.dump(content,af)
                    af.write("\n")
                    af.close