import json
from collections import Counter
import re
   
twitter = []
for line in open ('twitter.json'):
    twitter.append (json.loads (line))

##question 1:
#### how many tweets in the set?
   
number_of_tweets = len (twitter)
   
#### answer:
   
print ('there are', number_of_tweets, 'tweets in the set\n')


### question 2:
#### percentage of deleted tweets
   
# creating two lists
   
published = []
deleted = []
   
# find the right tweets with the key=delete
#add them to the according list
   
for i in range (len (twitter)):
    if 'delete' in twitter[i].keys ():
        deleted.append (twitter[i])
    else:
        published.append (twitter[i])
   
#### answer:
   
print ('percentage of deleted tweets is ', (sum ('delete' in t for t in twitter)/number_of_tweets)*100, '\n')
   
### question 3:
#### the most popular tweets languages
   
# create a list, add all the languages, find the most popular ones
   
language = []
for i in range (len (published)):
    language.append (published[i]['lang'])
    list_of_languages = Counter (language)
   
#### answer:
   
for i in list_of_languages.most_common (20):
        print (i[0], '-', i[1])

print('')
### question 4:
#### are there any tweets from the same publisher? if so, how many publishers like that are? 
   
humans = []
for i in range (len (published)):
    humans.append (published[i]['user']['screen_name'])
list_of_users = Counter (humans)
   
dictionary_of_users = {}
dictionary_of_users.update (list_of_users)
quantity = 0
for user in dictionary_of_users:
    if dictionary_of_users [user] > 1:
        quantity += 1 
   
#### answer:
   
print (quantity)
print('')
### question 5:
#### top-10 hashtags
   
hashtags = []
for i in range (len (published)):
    hashtag = published[i]['entities']['hashtags']
    if len (hashtag) != 0:
        for j in range (len (hashtag)):
            hashtags.append (hashtag[j]['text'])
list_of_hashtags = Counter (hashtags)
   
#### answer:
   
for hasht in list_of_hashtags.most_common (10):
    print (hasht[0], '-', hasht[1])
   
print('')
### question 6:
#### frequency dictionary
   
own = []
for i in range (len (published)):
    if 'retweeted_status' not in published[i] and published[i]['lang'] == 'en':
        own.append (published[i]['text'])
   
own1 = ''.join (own)
own1 = re.sub(r'[^\w\s]', '', own1)
own1 = own1.lower ().split ()
list_of_words = Counter (own1)
   
#### answer
   
for word in list_of_words.most_common (15):
    print (word[0], '-', word[1])
   
print('')
### question 7:
#### how many followers do the tweets authors have? top-10 authors
   
followers_names = []
for i in range (len (published)):
    followers_names.append (published[i]['user']['name'])
followers_qus = []
for i in range (len (published)):
    followers_qus.append (published[i]['user']['followers_count'])


