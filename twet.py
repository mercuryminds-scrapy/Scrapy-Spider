import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
import MySQLdb
import time
 
# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = '2874668814-'
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Database Creation
con=MySQLdb.connect('localhost','root','root','mysql')
cur=con.cursor()

 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
user=api.get_user('mercuryminds')
#user = api.me()


# Sample method, used to update a status
#api.update_status('Feeling Happy')


print('Name: ' + user.name)
print user.created_at
print user.default_profile
print user.default_profile_image
print user.description
print user.entities
print user.id
print user.followers_count
print('Friends: ' + str(user.friends_count))
print user.status
print user.statuses_count
print user.url


# page_list=[]
#
# for page in tweepy.Cursor(api.user_timeline, include_rts=True,count=200).pages(''):
#     page_list.append(page)
#
#
# for page in page_list:
#     for status in page:
#        print status.text


#To get all tweets

for status in tweepy.Cursor(api.user_timeline, id="mercuryminds").items():


    try:
        a= status.retweeted_status.user.name
    except:
        a= status.user.name
    b= status.lang
    c= status.created_at
    x=status.text.encode('ascii','ignore').replace("'","")

    try:
        sql=("insert into tweet(title,time,tweet) values('%s','%s','%s')"%(a,c,x))
        cur.execute(sql)
        con.commit()
    except tweepy.TweepError:
        time.sleep(60 *15)
        continue
    except StopIteration:
        break

con.commit()
cur.close()
con.close()
#
#
#
#

class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''
    def on_data(self, raw_data):
        print raw_data
        return True



    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

if __name__ == '__main__':

   listener = StdOutListener()

   stream = Stream(auth, listener)

#   stream.filter(follow=['2874668814'],track=[])
##   stream.filter(track=['python', 'ruby', 'java'])




