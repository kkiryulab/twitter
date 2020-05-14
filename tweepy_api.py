import tweepy
import datetime

def auth():
    
    #python で Twitter APIを使用するためのConsumerキー、アクセストークン設定
    Consumer_key = 'X9d3yrIISpJ5J0Pil57lefzFT'
    Consumer_secret = 'LYYnk8pLZDx5vB1LAnbQN3Ev5iU2LKoKUO5ABBdHCVOzM2gDVE'
    Access_token = '1153273407846248450-5YyHMl2hNBaaxy1FnCj5jVnvOPLpkf'
    Access_secret = 'B2BQvt137S5pu3f0ShcFcoNPtAEr3ojbgjbuM3pSJ1fWW'

    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth)

    return api