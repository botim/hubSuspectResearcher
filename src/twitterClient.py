# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:03:31 2019

@author: Yonatan Vernik
"""

"""
2 major functions:
given handle, retreives the last 3,200 tweets from a user and counts the usage of hateful words

given a list of twitter IDs, write a csv file with the data in the required format

some code copied from the python-twitter example "scrape all tweets"
"""

import json
import sys
import twitter
import csv

def get_tweets(api=None, screen_name=None):
    timeline = api.GetUserTimeline(screen_name=screen_name, count=200)
    earliest_tweet = min(timeline, key=lambda x: x.id).id

    while True:
        tweets = api.GetUserTimeline(
            screen_name=screen_name, max_id=earliest_tweet, count=200
        )
        new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest
            timeline += tweets

    return timeline

"""
count the usage of hateful words by a user over last 200 tweets.
returns dictionary.
"""
ignored = [] #TODO add news sites
stats = {}
def measure_user_hate(api=None, screen_name=None):
    D = {"נאצי":0,
         "בבונים":0,        
         "הומופוב":0,        
        "קסנופוב":0,        
        "אסלאמופוב":0,        
        "סקסיסט":0,        
        "עוכרי ישראל":0,        
        "בוגד":0,        
        "סמול":0,        
        "מסתננים":0,        
        "מוות לערבים":0,        
        "שימותו":0,        
        "ignorability":0
        }
    if screen_name in ignored:
        D["ignorability"] = 100
    stats[screen_name] = D
    timeline = get_tweets(api=api, screen_name=screen_name)
    for tweet in timeline:
        D, tweet_hate = measure_tweet_hate(tweet,D)
        if tweet_hate >= 5:
            D["ignorability"] += 1
    return D

def measure_tweet_hate(tweet, D):
    total_hate = 0
    for keyword in D.keys():
        if keyword in tweet._json["text"]:
            count = tweet._json["text"].count(keyword)
            D[keyword] += count
            total_hate += count

    return D, total_hate

def get_user_params(api, ID):
    user = api.GetUser(ID)._json
    
    date_created = user["created_at"]
    name = user["name"].encode("utf-8")
    handle = user["screen_name"]
    description = user["description"].encode("utf-8")
    language = user["lang"]
    location = user["location"]
    protected = user["protected"]
    verified = user["verified"]
    followers_count = user["followers_count"]
    friends_count = user["friends_count"]
    statuses_count = user["statuses_count"]
    favourites_count = user["favourites_count"]
    listed_count = user["listed_count"]
    
    params = [ID, handle, name, description, date_created, location, language, protected, followers_count, friends_count, favourites_count, statuses_count, listed_count, verified]
    return params

def output_to_csv(params_metalist):
    column_titles = ["ID", "handle", "name", "description", "date_created", "location", "language", "protected", "followers_count", "friends_count", "favourites_count", "statuses_count", "listed_count", "verified"]
    
    with open("test.csv", "w+", newline = '') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerow(column_titles)
        for params in params_metalist:
            wr.writerow(params)
        
def ID_list_to_param_csv(ID_list):
    params_metalist = []
    for ID in ID_list:
        params_metalist.append(get_user_params(api, ID))
    output_to_csv(params_metalist)

if __name__ == "__main__":
    ACCESS_TOKEN_KEY = ""
    ACCESS_TOKEN_SECRET = ""
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    
    api = twitter.Api(
        CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
    )
    ID = 876408437814558724 #yair netanyahu
    
    ID_list = [ID]
    ID_list_to_param_csv(ID_list)    
    
    #handle = "@YairNetanyahu"
    #user = api.GetUser(screen_name = handle)._json
    #print(user["id"])
    #D = measure_user_hate(api=api,screen_name=name)
    #print(stats)