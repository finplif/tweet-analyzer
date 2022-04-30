import json
from collections import Counter
import re


class TwitterAnalyzer:
    def __init__(self, twitter_file):
        self.file = twitter_file
        self.filter_by_deleted_and_published()



    def filter_by_deleted_and_published(self):

        twitter = []
        for line in open(self.file):
            twitter.append(json.loads(line))

        published = []
        deleted = []
        
        for i in range(len(twitter)):
            if 'delete' in twitter[i].keys():
                deleted.append(twitter[i])
            else:
                published.append(twitter[i])
                
        self.published = published
        self.deleted = deleted
   


    def get_top_20_languages(self):

        language = []
        for i in range(len(self.published)):
            language.append(self.published[i]['lang'])
        list_of_languages = Counter(language)
       
        return list_of_languages
    


    def serial_twitters(self):
        humans = []
        for i in range(len(self.published)):
            humans.append(self.published[i]['user']['screen_name'])
        list_of_users = Counter(humans)
       
        dictionary_of_users = {}
        dictionary_of_users.update(list_of_users)
        quantity = 0
        for user in dictionary_of_users:
            if dictionary_of_users [user] > 1:
                quantity += 1
       
        return quantity
    

   
    def top_10_hashtags(self):
        
        hashtags = []
        for i in range(len(self.published)):
            hashtag = self.published[i]['entities']['hashtags']
            if len(hashtag) != 0:
                for j in range(len(hashtag)):
                    hashtags.append(hashtag[j]['text'])
        list_of_hashtags = Counter(hashtags)
       
        return list_of_hashtags



    def frequency_dictionary(self):
       
        own = []
        for i in range(len(self.published)):
            if 'retweeted_status' not in self.published[i] and self.published[i]['lang'] == 'en':
                own.append(self.published[i]['text'])
           
        own1 = ''.join(own)
        own1 = re.sub(r'[^\w\s]', '', own1)
        own1 = own1.lower().split()
        list_of_words = Counter(own1)
       
        return list_of_words
   


analyzer = TwitterAnalyzer('twitter.json')
    
list_of_languages = analyzer.get_top_20_languages()

quantity = analyzer.serial_twitters()

list_of_hashtags = analyzer.top_10_hashtags()

list_of_words = analyzer.frequency_dictionary()
   
print(quantity)


#### how many followers do the tweets authors have? top-10 authors
   
"""
followers_names = []
for i in range (len (published)):
    followers_names.append (published[i]['user']['name'])
followers_qus = []
for i in range (len (published)):
    followers_qus.append (published[i]['user']['followers_count'])
"""

