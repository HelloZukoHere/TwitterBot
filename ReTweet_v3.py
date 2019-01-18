#copied and pasted from CSDojo (and later modified)
#https://github.com/ykdojo/twitterbotsample/blob/master/my_twitter_bot.py

#Matthew Lee - January 2019
#Python Learning

import tweepy
import time

from keys import consumerKey, consumerSecret, accessKey, accessSecret

# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/
print('this is my Twot Bot')

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld!')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name +
                    ' Hello, Zuko here!', mention.id)

        elif '#honor' in mention.full_text.lower():
            print('found #honor!')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name +
                ' I must capture the avatar and restore my honor', mention.id)



while True:
    reply_to_tweets()
    time.sleep(15)