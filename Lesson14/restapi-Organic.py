# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from twython import Twython
import json
import datetime

import geocoder


##codes to access twitter API. 
APP_KEY = "e0txaoDvxNKrLqDkTq9GUPiRZ"
APP_SECRET = "9WaTGbbgADMT2l3h87smKtwgI2MNPu3kGCqbKGu7FNgY9DKYYr" 
OAUTH_TOKEN = "824536473898737665-Vd8Xx0xXwYFxUfWy4LbG0v6wznOM8yj"
OAUTH_TOKEN_SECRET = "6hgUi8iTnMMzmjiL6MCAClwGiapqUS22it9QHQzj6do6X"

##initiating Twython object 
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

##TODO:  This should work as an alternative but it doesn't. Need to find out why
#twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
#ACCESS_TOKEN = twitter.obtain_access_token()
#print ACCESS_TOKEN
#twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)


search_results = twitter.search(q="#organic+OR+#biologishc+OR+#organico+OR+#organico+OR+#bio+OR+#raw+OR+#vegan+OR+#vegetarian+OR+#fairtrade", count=2000)

#search_results = twitter.search(q="#amsterdam", count=50)




for result in search_results['statuses']:
    print result
    

##parsing out 
for tweet in search_results["statuses"]:
    username =  tweet['user']['screen_name']
    followers_count =  tweet['user']['followers_count']
    tweettext = tweet['text'].encode('utf-8').replace("'","''").replace(';','')
 
  
    if tweet['place'] != None:
        full_place_name = tweet['place']['full_name'].encode('utf-8')
        place_type =  tweet['place']['place_type'].encode('utf-8')
        
        g = geocoder.google(full_place_name)
        Plat= g.lat
        Plng= g.lng
        
        
        output_file = 'resultOrganic6place.csv' 
        target = open(output_file, 'a')
        target.write(username)
        target.write(str(","))
        target.write(str(followers_count))
        target.write(str(","))
        target.write(tweettext)
        target.write(str(","))
        target.write(full_place_name)
        target.write(str(","))
        target.write(place_type)
        target.write(str(","))
        target.write(str(Plat))
        target.write(str(","))
        target.write(str(Plng))
        target.write('\n') #produce a tab delimited file
        target.close()
            
            
        print username
        print followers_count
        print tweettext
        print place_type
        print full_place_name
        
    coordinates = tweet['coordinates']
    if coordinates != None:
        coordDeep=coordinates['coordinates']
        lat=coordDeep[0]
        longi=coordDeep[1]
        
        output_file = 'resultOrganic5coord.csv' 
    
        target = open(output_file, 'a')
        target.write(username)
        target.write(str(","))
        target.write(str(followers_count))
        target.write(str(","))
        target.write(tweettext)
        target.write(str(","))
        target.write(str(lat))
        target.write(str(","))
        target.write(str(longi))
        target.write(str(","))
        target.write('\n') #produce a tab delimited file
        target.close()
            
        print username
        print followers_count
        print tweettext
        print lat
        print longi
        
       

   


    
    