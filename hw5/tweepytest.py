from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import os
import flask

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

target = sys.argv[1]

print("Getting data for " + target)
item = auth_api.get_user(target)
print("name: " + item.name)
print("screen_name: " + item.screen_name)


tweetlist = []
end_date = datetime.utcnow() - timedelta(days=30)

for status in Cursor(auth_api.user_timeline, id=target).items():
    tweetlist.append(status.text + " Tweeted at: " + str(status.created_at))
    if status.created_at < end_date:
        break
app = flask.Flask(__name__)
@app.route('/')

def index():
    return flask.render_template("index.html", target = target, len = len(tweetlist), tweetlist = tweetlist)
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
    )