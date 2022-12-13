from dataclasses import field
import tweepy
import config
import pandas as pd
import csv
import collections

print('Connecting tweepy')
auth = tweepy.OAuthHandler(config.api_key, config.api_key_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

print('Tweepy connected')
print('Please wait whilst records are being retrieved')
search_words = ["(health care)"]
#date_since = '2021-01-01'
max_number_of_tweets=20000
tweets = tweepy.Cursor(
    api.search_tweets,
    q=search_words,
    geocode="49.2827,-123.1207,20km",
    lang="en",
    since_id='2022-05-01'
    ).items(max_number_of_tweets)

print('Done retrieving tweets. Now writing to CSV file')
csv_header = ['number', 'location', 'Followers Count', 'Name' , 'date', 'source', 'text', 'retweet count']
csv_data = []

count = 0
for tweet in tweets:
    count += 1
    csv_data.append([
        count,
        tweet.user.location,
        tweet.user.followers_count,
        tweet.user.name,
        tweet.created_at,
        tweet.source,
        tweet.text,
        tweet.retweet_count,
    ])
#     print(tweet.created_at)
#     print(tweet.text)
#     print(tweet.user.screen_name)
#     print(tweet.user.location)
#     print(tweet.source)
#     print("\n\n\n")
vancouver = []
surrey = []
abbotsford = []
burnaby = []
chilliwack = []
victoria = []

for i in range(len(csv_data)):
    if 'Vancouver' in csv_data[i][1]:
        vancouver.append(csv_data[i])

for i in range(len(csv_data)):
    if 'Victoria' in csv_data[i][1]:
        victoria.append(csv_data[i])

for i in range(len(csv_data)):
    if 'Chilliwack' in csv_data[i][1]:
        chilliwack.append(csv_data[i])

for i in range(len(csv_data)):
    if 'Surrey' in csv_data[i][1]:
        surrey.append(csv_data[i])


for i in range(len(csv_data)):
    if 'Abbotsford' in csv_data[i][1]:
        abbotsford.append(csv_data[i])


for i in range(len(csv_data)):
    if 'Burnaby' in csv_data[i][1]:
        burnaby.append(csv_data[i])        
        
def createCSV(fileName, csvData, csvHeader):
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csvHeader)
        writer.writerows(csvData)
       
 # creating csv's according to the cities   
createCSV('abbotsford-data.csv', abbotsford, csv_header)
createCSV('burnaby-data.csv', burnaby, csv_header)
createCSV('surrey-data.csv', surrey, csv_header)
createCSV('tweets-new-data.csv', csv_data, csv_header)
createCSV('vancouver-data.csv', vancouver, csv_header) 
createCSV('chilliwack-data.csv', chilliwack, csv_header) 
createCSV('victoria-data.csv', victoria, csv_header) 
   

   
print ("Total tweets found: ", count)