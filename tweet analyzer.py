import json
from collections import Counter
import re


class TwitterAnalyzer:
    def __init__(self, twitter_file):
        self.file = twitter_file
        self.published, self.deleted = self.filter_by_deleted_and_published()
        self.topn_languages()

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

        return published, deleted

    def topn_languages(self, topn=20):
        language = []
        lang_dic = {}
        for i in range(len(self.published)):
            language.append(self.published[i]['lang'])
        languages_total = Counter(language)
        top_languages = languages_total.most_common(topn)
        for i in range(len(top_languages)):
            lang_dic[top_languages[i][0]] = top_languages[i][1]

        return lang_dic

    def serial_twitters(self):
        humans = []
        for i in range(len(self.published)):
            humans.append(self.published[i]['user']['screen_name'])
        list_of_users = Counter(humans)

        dictionary_of_users = {}
        dictionary_of_users.update(list_of_users)
        quantity = 0
        for user in dictionary_of_users:
            if dictionary_of_users[user] > 1:
                quantity += 1

        return quantity

    def topn_hashtags(self, topn=10):
        hashtags = []
        hashtags_dic = {}
        for i in range(len(self.published)):
            hashtag = self.published[i]['entities']['hashtags']
            if len(hashtag) != 0:
                for j in range(len(hashtag)):
                    hashtags.append(hashtag[j]['text'])
        hashtags_total = Counter(hashtags)
        top_hashtags = hashtags_total.most_common(topn)
        for i in range(len(top_hashtags)):
            hashtags_dic[top_hashtags[i][0]] = top_hashtags[i][1]

        return hashtags_dic

    def frequency_dictionary(self, topn=20):
        personal_tweets = []
        tweets_dic = {}
        for i in range(len(self.published)):
            if 'retweeted_status' not in self.published[i] and self.published[i]['lang'] == 'en':
                personal_tweets.append(self.published[i]['text'])

        cleaned_tweets = ''.join(personal_tweets)
        cleaned_tweets = re.sub(r'[^\w\s]', '', cleaned_tweets)
        cleaned_tweets = cleaned_tweets.lower().split()
        words_total = Counter(cleaned_tweets)
        frequent_words = words_total.most_common(topn)
        for i in range(len(frequent_words)):
            tweets_dic[frequent_words[i][0]] = frequent_words[i][1]
        return tweets_dic


#### how many followers do the tweets authors have? top-10 authors

"""
followers_names = []
for i in range (len (published)):
    followers_names.append (published[i]['user']['name'])
followers_qus = []
for i in range (len (published)):
    followers_qus.append (published[i]['user']['followers_count'])
"""
