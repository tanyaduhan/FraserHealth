from dataclasses import field
import tweepy
import config
import pandas as pd
import csv
import collections


auth = tweepy.OAuthHandler(config.api_key, config.api_key_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)


new_search = "(virtual healthcare OR fraserhealth OR virtual care OR stroke OR heartrate) -country_code:CA" 
#new_search = "(fraserhealth ) -place_country:CA" 

tweets = tweepy.Cursor(api.search_tweets,
                   q=new_search,                   
                   lang="en",
                   since_id='2022-10-14').items(20000)



users_locs = [[tweet.text, tweet.user.location, tweet.created_at, tweet.source] for tweet in tweets]
count = 0, 
#tweet.entities
#Canada = [[range(3)]]

#for n in range(0, len(users_locs)):
#    if "Canada" in users_locs[n][1]:
#        Canada[n] = users_locs[n]

#print (users_locs)
#print(users_locs[5][1])
tweet_df = pd.DataFrame(users_locs, columns=['text', 'user loc', 'tweet date', 'source'])
print(tweet_df)


'''
with open('output1.csv', 'w', newline = '') as csvfile:

    fieldnames = ['text', 'user loc', 'tweet date', 'source']

    thewriter = csv. DictWriter(csvfile, fieldnames= fieldnames)

    thewriter.writeheader()

    for tweet in tweets:
        count +=1
        thewriter.writerow({'text' : tweet.text, 'user loc': tweet.user.location,  'tweet date': tweet.created_at, 'source': tweet.source })

 '''
