import tweepy
import datetime
import tweepy_api

api = tweepy_api.auth()

def gettwitterdata(user_name, tweets_count, out_file):

    #つぶやきを格納するリスト
    tweets_data =[]

    #特定ユーザのツイートを取得
    [tweets_data.append(tweet.text + '\n')
    for tweet in tweepy.Cursor(api.user_timeline, id=user_name).items(int(tweets_count)) if (list(tweet.text)[:2]!=['R','T']) & (list(tweet.text)[0]!='@')]

    #出力ファイル名
    fname = r"'"+ out_file + "'"
    fname = fname.replace("'","")

    #ファイル出力
    with open(fname, "w",encoding="utf-8") as f:
        f.writelines(tweets_data)

if __name__ == '__main__':
    #ツイートを取得するユーザ名を入力
    print ('====== Enter User Name =====')
    user_name = input('>  ')
    print(user_name)

    #取得するツイート数を入力
    print ('====== Enter Tweet Count =====')
    tweets_count = input('>  ')
    print(tweets_count)

    #出力ファイル名を入力(相対パス or 絶対パス)
    print ('====== Enter Tweet Data file =====')
    out_file = input('>  ')
    print(out_file)

    gettwitterdata(user_name, tweets_count, out_file)