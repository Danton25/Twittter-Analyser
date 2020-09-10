#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:29:31 2019

@author: nikhilyadav
"""


from tweepy import OAuthHandler
import tweepy
import json
import preprocessor as p

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
tweet=[]
hashlist = ""
menlist = ""
urllist = ""
emolist = ""
emolist1 = ""
#jsonFile = open("dilmabr.json",'a')
with open ("ArvindKejriwal.json",'r') as a: 
     
    
#    y = json.loads(a)

         for line in a:
            
            content = json.loads(line)
            x= p.parse(content["text"])
            
            if content["in_reply_to_screen_name"] !=  "null":
                content["poi_name"] = content["user"]["screen_name"]
                content["poi_id"] = content["user"]["id"]
                poiname = content["poi_name"]
                
                
                
                
            else:
                content["poi_name"] = content["in_reply_to_screen_name"]
                content["poi_id"] = content["in_reply_to_user_id"]
                poiname = content["poi_name"]
                
                
            hashtags = content["entities"]["hashtags"]
            content["verified"] = True
            #content["country"] = 
            content["replied_to_tweet_id"] = content["in_reply_to_status_id"]
            content["replied_to_user_id"] = content["in_reply_to_user_id"]
            
            
            
            try:
                
                
                content["tweet_text"] = content["extended_tweet"]["full_text"]
                #print(content["extended_tweet"]["full_text"])
            except:    
                content["tweet_text"] = content["text"]
                #print(content["text"])
            
            
            #content["tweet_text"] = content["text"]
            content["tweet_lang"] = content["lang"]
            #content["mentions"]= ["entities"]["user_mentions"]["screen_name"]
            #tweet.append(json.loads(line))
            #print(content["extended_tweet"]["full_text"])
            if content["replied_to_tweet_id"] != None:
                
                
                try:
                    content["reply_text"] = content["extended_tweet"]["full_text"]
                except:    
                    content["reply_text"] = content["text"]
                    print(content["text"])
                
                   
            else:
                content["reply_text"] = None
            
            
            
            
            a = x.mentions
           
            #print(content["text"])
            try:
                for men in range (0,len(a)):
                    #print(a[men].match)
                #print (x)
                    #content["mentions"] = (a[men].match)
                    #mentionlist= (a[men].match)
                    menlist= (a[men].match)+ ' '+menlist
                    menlist = menlist.replace("@", "")
                    menlist = menlist.rstrip()
                menlist = menlist.replace(" ", ", ")
                #print(menlist)
                content["mentions"] = menlist
                    #print(mentionlist)
            except:
                content["mentions"] = None
            
            
            if poiname in india :
                content["country"] = "India"
            elif poiname in usa:
                content["country"] = "USA"
            else:
                content["country"] = "Brazil"
            
            #print(type(x.hashtags))
            #content["hashtags"]=",".join(x for x in x.hashtags if  x.hashtags else None
            #content["hashtags"]=",".join(item for item in x.hashtags if item)
            #content["hashtags"] = ",".join(hashtag["text"] for hashtag in hashtags) if len(hashtags) != 0 else None
            hashtag = x.hashtags
            #print (hashtag)
        
            try:
                for k in range(0,len(hashtag)):
                    
                    hashlist= (hashtag[k].match) +  " " +hashlist
                    hashlist = hashlist.replace("#", "")
                    hashlist = hashlist.rstrip()
                hashlist = hashlist.replace(" ", ", ")
                #print(hashlist)
                    
                content["hashtags"] = hashlist
            except:
                content["hashtags"] = None
                
                
            url = x.urls
                
            try:
                for u in range(0,len(url)):
                    
                    
                    urllist= (url[u].match) +  " " +urllist
                    urllist = urllist.replace("#", "")
                    urllist = urllist.rstrip()
                urllist = urllist.replace(" ", ", ")
                #print(urllist)
                content["tweet_urls"] = urllist
            except:
                content["tweet_urls"] = None
                
            
            emo = x.emojis
            smi = x.smileys
            try:
                for e in range(0,len(emo)):
                    
                    
                    emolist= (emo[e].match) +  " " +emolist
                    #emolist = emolist.replace("#", "")
                    #emolist = emolist.rstrip()
                #emolist = emolist.replace(" ", ", ")
                #print(emolist)
                #content["tweet_emoticons"] = emolist
            except:
                #content["tweet_emoticons"] = None
                print()
            
            try:
                for s in range(0,len(smi)):
                    
                    
                    emolist1= (smi[s].match) +  " " +emolist1
                    #emolist1 = emolist1.replace("#", "")
                    #emolist1 = emolist1.rstrip()
                #emolist1 = emolist1.replace(" ", ", ")
                #print(emolist1)
            except:
                print()
        
            try:    
            
                finalemos = emolist + emolist1
                content["tweet_emoticons"] = finalemos
                print (finalemos)
            except:
                content["tweet_emoticons"] = None
            
            
            if content["lang"] == 'en':
                
                try: 
                    content["tweet_en"] = content["extended_tweet"]["full_text"]
                    #print(content["extended_tweet"]["full_text"])
                except:    
                    content["tweet_en"] = content["text"]
                    #print(content["text"])
                
                #content["tweet_en"] = content["text"]
            elif content["lang"] == 'hi':
                #content["tweet_hi"] = content["text"]
                try: 
                    content["tweet_hi"] = content["extended_tweet"]["full_text"]
                    #print(content["extended_tweet"]["full_text"])
                except:    
                    content["tweet_hi"] = content["text"]
                
                
            elif content["lang"] == 'pt':
                #content["tweet_pt"] = content["text"]
                try: 
                    content["tweet_pt"] = content["extended_tweet"]["full_text"]
                    #print(content["extended_tweet"]["full_text"])
                except:    
                    content["tweet_pt"] = content["text"]
            
            
            with open("newnewfile.json", 'a') as af:
                json.dump(content,af)
                af.write("\n")
            
      
s