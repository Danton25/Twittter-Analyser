#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:58:48 2019

@author: nikhilyadav
"""
import json

counter = dict()
original=[]

with open ("tweets6.json",'r') as a:
    
    alltweets = a.readlines()
    
    for line in alltweets:

             
            content = json.loads(line)
            #x= p.parse(content["text"])
            
            screenname = content["user"]["screen_name"]
            
            if screenname == "narendramodi":
                
                original.append(content["id"])
                with open("NarendraModiReplies.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
                    
    n  = len(original)                
    print(original, " Length :", n)      
    
    for i in range (0,n):
        counter[original[i]] = 0
        
    for line in alltweets:
        content = json.loads(line)
        if(content["in_reply_to_user_id"] == 18839785):
            for i in range (0, n):
                if(content["in_reply_to_status_id"] == original[i]):
                    counter[original[i]] = counter[original[i]] + 1
                    
    print (counter," length:   ", len(counter))
    
    totalcount = 0
    for i in range(0 ,n):
        totalcount = totalcount + counter[original[i]]
    print(totalcount)
            
    
    
    for line in alltweets:
        content = json.loads(line)
        
        reply_id = content["in_reply_to_status_id"]
        for i in range(0,n):
            if (counter[original[i]] >= 20):
                rep = original[i]
                
                if(reply_id == rep):
                    with open ("NarendraModiReplies.json",'a') as ab:
                        
                        
                        json.dump(content,ab)
                        ab.write("\n")
                        ab.close
                        
                        
                        
        a.close


        
                    
                    
                    
                    
                    
    '''             
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            elif screenname == "AmitShah":
                
                
                with open("AMITSHAH.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
            
            elif screenname == "ArvindKejriwal":
                
                
                with open("ARRVINDKEJRIWAL.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
            
            elif screenname == "BernieSanders":
                
                
                with open("BERNIESANDERS.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
                    
            elif screenname == "Debora_D_Diniz":
                
                
                with open("DEBORADDINIZ.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
            
            elif screenname == "delucca":
                
                
                with open("DELUCCA.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
                    
            elif screenname == "dilmabr":
                
                
                with open("DILMABR.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
                    
                    
                    
            elif screenname == "GuilhermeBoulos":
                
                
                with open("GUILHEEMEBOULOS.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
            
            elif screenname == "HillaryClinton":
                
                
                with open("HILLARYCLINTON.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
            
            
            elif screenname == "KamalaHarris":
                
                
                with open("KAMALAHARRIS.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
            
            
            elif screenname == "MarinaSilva":
                
                
                with open("MARINASILVA.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
            
            
            elif screenname == "rajnathsingh":
                
                
                with open("RAJNATHSINGH.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
            
            
            if screenname == "realDonaldTrump":
                
                
                with open("REALDONALDTRUMP.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
            
            
            elif screenname == "sardanarohit":
                
                
                with open("SARDANAROHIT.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
                    
                    
                    
            elif screenname == "SpeakerPelosi":
                
                
                with open("SPEAKERPELOCI.json", 'a') as af:
                    json.dump(content,af)
                    af.write("\n")
                    af.close
        '''