import tweepy
import datetime

def auth():
    
    #python で Twitter APIを使用するためのConsumerキー、アクセストークン設定
    Consumer_key = 'XXXXXXXXX'
    Consumer_secret = 'XXXXXXXXX'
    Access_token = 'XXXXXXXXX'
    Access_secret = 'XXXXXXXXX'

    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth)

    return api