import tweepy
import datetime
import tweepy_api

api = tweepy_api.auth()

def gettwitterdata(keyword, tweets_count, dfile):

    #検索キーワード設定 
    q = keyword

    #つぶやきを格納するリスト
    tweets_data =[]

    #カーソルを使用してデータ取得
    for tweet in tweepy.Cursor(api.search, q=q, tweet_mode='extended').items(int(tweets_count)):

        #つぶやき時間がUTCのため、JSTに変換  ※デバック用のコード
        #jsttime = tweet.created_at + datetime.timedelta(hours=9)
        #print(jsttime)

        #つぶやきテキスト(FULL)を取得
        tweets_data.append(tweet.full_text + '\n')

    #出力ファイル名
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #ファイル出力
    with open(fname, "w",encoding="utf-8") as f:
        f.writelines(tweets_data)


if __name__ == '__main__':

    #検索キーワードを入力  ※リツイートを除外する場合 「キーワード -RT 」と入力
    print ('====== Enter Serch KeyWord   =====')
    keyword = input('>  ')
    print(keyword)

    #取得するツイート数を入力
    print ('====== Enter Tweet Count =====')
    tweets_count = input('>  ')
    print(tweets_count)

    #出力ファイル名を入力(相対パス or 絶対パス)
    print ('====== Enter Tweet Data file =====')
    dfile = input('>  ')
    print(dfile)

    gettwitterdata(keyword, tweets_count, dfile)