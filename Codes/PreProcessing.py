#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:58:38 2019

@author: nikhilyadav
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:29:31 2019

@author: nikhilyadav
"""


from tweepy import OAuthHandler
import tweepy
import json
#import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from cltk.stop.classical_hindi.stops import STOPS_LIST
import string
import preprocessor as p
import re
from datetime import datetime,timedelta


CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_TOKEN=""
ACCESS_SECRET=""

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
i = 0
india = ['AmitShah','ArvindKejriwal','narendramodi', 'rajnathsingh', 'sardanarohit']
usa = ['realDonaldTrump','HillaryClinton', 'BernieSanders', 'KamalaHarris', 'SpeakerPelosi']
brazil= ['Debora_D_Diniz', 'delucca', 'dilmabr', 'GuilhermeBoulos', 'MarinaSilva']

stopwords_en = set(stopwords.words('english'))
stopwords_pt = set(stopwords.words('portuguese'))

punctuate_sent = string.punctuation
punctuate_list = []
for i in range(0,len(punctuate_sent)):
    punctuate_list.append(punctuate_sent[i])

punctuate_set = set(punctuate_list)

#jsonFile = open("dilmabr.json",'a')
with open ("tweets6.json",'r') as a: 
     
    
#    y = json.loads(a)
    
         for line in a:

             
            content = json.loads(line)
            x= p.parse(content["text"])
            
            
#--------------------------------- poi name,id--------------------------------------------------------            

            
            if content["in_reply_to_screen_name"] is  None:
                content["poi_name"] = content["user"]["screen_name"]
                content["poi_id"] = content["user"]["id"]
                poiname = content["poi_name"]
                
                
            else:
                content["poi_name"] = content["in_reply_to_screen_name"]
                content["poi_id"] = content["in_reply_to_user_id"]
                poiname = content["poi_name"]
                
            content["verified"] = content["user"]["verified"]
            content["replied_to_tweet_id"] = content["in_reply_to_status_id"]
            content["replied_to_user_id"] = content["in_reply_to_user_id"]
            
            
#--------------------------------- tweet_text--------------------------------------------------------            
            
            def tweettext():
                try:
                    
                    content["tweet_text"] = content["extended_tweet"]["full_text"]
                    
                except:  
                    
                    content["tweet_text"] = content["text"]
    
                content["tweet_lang"] = content["lang"]
                if content["replied_to_tweet_id"] != None:
                    try:
                        content["reply_text"] = content["extended_tweet"]["full_text"]
                    except:    
                        content["reply_text"] = content["text"]
                            
                else:
                    content["reply_text"] = None

#--------------------------------- reply--------------------------------------------------------         


            def reply():
            
                if(content["in_reply_to_user_id"] is None):
                    content["tweet_text"] = content["text"]
                    if "poi_name" not in content:
                        content["poi_name"] = content["user"]["screen_name"]
                        content["poi_id"] = content["user"]["id"]
                    content["replied_to_tweet_id"] = "Null"
                    content["replied_to_user_id"] = "Null"
                #if it's a reply
                else:
                    content["tweet_text"] = content["text"]
                    content["reply_text"] = content["text"]
                    if "poi_name" not in content:
                        content["poi_name"] = content["in_reply_to_screen_name"]
                        content["poi_id"] = content["in_reply_to_user_id"]
                    content["replied_to_tweet_id"] = content["in_reply_to_status_id"] 
                    content["replied_to_user_id"] = content["in_reply_to_user_id"] 

#--------------------------------- country--------------------------------------------------------            
            
            def countries():            
                if poiname in india :
                    content["country"] = "India"
                elif poiname in usa:
                    content["country"] = "USA"
                else:
                    content["country"] = "Brazil"
                
#--------------------------------- mentions--------------------------------------------------------            
            def ment():
            
                men = x.mentions
                
                if men is not None:
                    txt1 = ""
                    for i in range(0,len(men)):
                        y = re.sub("@","",men[i].match)
                        txt1 = re.sub(men[i].match,"",content["text"])
                        txt1 = txt1 + " " + y
           
                    content["mentions"] = txt1
                    
#--------------------------------- hashtags--------------------------------------------------------            
            def hashes():

                hashtag = x.hashtags
    
                txt2 = ""
                if hashtag is not None:
                    txt1=""
                    for k in range(0,len(hashtag)):
                        y = re.sub("#","",hashtag[k].match)
                        txt2 =re.sub(hashtag[k].match,"",content["text"])
                        txt2=txt2+" "+y
                    content["hashtags"] = txt1
                
#--------------------------------- urls--------------------------------------------------------            
            def ur():
                 
                url = x.urls
                
                if url is not None:
                    txt3 = ""
                    for j in range(0,len(url)):
                        d = url[j].match
                        txt3 =re.sub(d,"",content["text"])
                        txt3=txt3+" "+d
                    content["tweet_urls"] = d
                
                
            
            
#--------------------------------- emojis--------------------------------------------------------            
            
            def emoticon():
                emo = x.emojis
                smi = x.smileys
                
                
                if (emo is not None) and (smi is not None):
                    g = ""
                    for i in range(0,len(emo)):
                        h = emo[i].match
                        content["text"] = content["text"].replace(h,"")
                        g = g + " " + h
                    #print(b)
                    txt6 = ""
                    for j in range(0,len(smi)):
                        u = smi[j].match
                        content["text"] = content["text"].replace(u,"")
                        txt6 = txt6 + " " + u
                    content["tweet_emoticons"] = txt6 + " " + u
                    
                
                
                
                elif emo is not None:
                    txt4 = ""
                    for j in range(0, len(emo)):
                        e = emo[j].match
                        content["text"] = content["text"].replace(e,"")
                        txt4 = txt4 + " " + e
                    content["tweet_emoticons"] = e
                
                    
                elif smi is not None:
                    txt5 = ""
                    for i in range(0,len(smi)):
                        f = smi[i].match
                        content["text"] = content["text"].replace(f,"")
                        txt5 = txt5 + " " + f
                    content["tweet_emoticons"] = f

#--------------------------------- text_xx--------------------------------------------------------            

            '''
            try:
                processedtweet = (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",content["extended_tweet"]["full_text"]).split()))
                #print(processedtweet)
            except:
                processedtweet = (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",content["text"]).split()))
                #print(processedtweet)
             
            processedtweet1 = (' '.join(re.sub("(@[A-Za-z0-9]+)|(\w+:\/\/\S+)"," ",content["text"]).split()))
            '''

            def languages():
                
                if content["lang"] == 'en':   
                    try:
                        
                        word_tokens = word_tokenize(content["extended_tweet"]["full_text"])
                        filtered_list = [word for word in word_tokens if not (word in stopwords_en.union(punctuate_set))]
                        filtered_sent = ' '.join(filtered_list)
                        content["text_en"] = filtered_sent
                        
                    except:    
                        word_tokens = word_tokenize(content["text"])
                        filtered_list = [word for word in word_tokens if not (word in stopwords_en.union(punctuate_set))]
                        filtered_sent = ' '.join(filtered_list)
                        content["text_en"] = filtered_sent
                    
                elif content["lang"] == 'hi':
                    #content["tweet_hi"] = content["text"]
                    try:
                        
                        word_tokens = word_tokenize(content["extended_tweet"]["full_text"])
                        filtered_list = [word for word in word_tokens if not (word in set(STOPS_LIST).union(punctuate_set))]
                        filtered_sent = ' '.join(filtered_list)
                        content["text_hi"] = filtered_sent
                      
                        
                    except:    
                        word_tokens = word_tokenize(content["text"])
                        filtered_list = [word for word in word_tokens if not (word in set(STOPS_LIST).union(punctuate_set))]
                        filtered_sent = ' '.join(filtered_list)
                        content["text_hi"] = filtered_sent
    
                    
                elif content["lang"] == 'pt':
                    try:
                        
                        word_tokens = word_tokenize(content["extended_tweet"]["full_text"])
                        filtered_list = [word for word in word_tokens if not (word in stopwords_pt.union(punctuate_set))]
                        filtered_sent = ' '.join(filtered_list)
                        content["text_pt"] = filtered_sent
                        
                        
                    except:    
                        word_tokens = word_tokenize(content["text"])
                        filtered_list = [word for word in word_tokens if not (word in stopwords_pt.union(punctuate_set))]
                        filtered_sent = ' '.join(filtered_list)
                        content["text_pt"] = filtered_sent

#--------------------------------- time--------------------------------------------------------            

            
            def rounder(t):
                if (t.minute > 0 or t.second > 0 or t.microsecond > 0):
                    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)+ timedelta(hours=1))
                else:
                    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour))      
                                
            content["tweet_date"] = rounder(
                    datetime.strptime(content["created_at"], '%a %b %d %H:%M:%S +0000 %Y')).strftime(
                            "%Y-%m-%dT%H:%M:%SZ")
            
            
            
            
            
            with open("tweet6file.json", 'a') as af:
                json.dump(content,af)
                af.write("\n")
                af.close
                        
                  
