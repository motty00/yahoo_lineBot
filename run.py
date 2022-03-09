import urllib.request as req
import datetime
import schedule
import time
import os
from bs4 import BeautifulSoup
from linebot import LineBotApi
from linebot.models import (
    TextSendMessage
)


def job():
    CHANNEL_ACCESS_TOKEN = os.environ['CHANNEL_ACCESS_TOKEN']
    # USER_ID = os.environ['USER_ID']
    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


    dt = datetime.datetime.now()
    dt_now = dt + datetime.timedelta(hours = 9)
    url = "https://news.yahoo.co.jp/ranking/access/news"
    response = req.urlopen(url)
    parse_html = BeautifulSoup(response,'html.parser')
    title_lists = parse_html.select('.newsFeed_item_title')
    url_lists = parse_html.select('.newsFeed_item_link')
    title_list = []
    url_list = []
    for t in title_lists:
        title_list.append(t.string)
    for i in url_lists:
        url_list.append(i.attrs['href'])
    
    messages = TextSendMessage(text = "おはようございます\n" + str(dt_now.month) + "月" + str(dt_now.day) + "日のニュースはこちら！！")
    line_bot_api.broadcast(messages=messages)
    
    title0 = title_list[0]
    title1 = title_list[1]
    title2 = title_list[2]
    title3 = title_list[3]
    title4 = title_list[4]
    
    message0 = url_list[0]
    message1 = url_list[1]
    message2 = url_list[2]
    message3 = url_list[3]
    message4 = url_list[4]
        # タイトル有り
    messages = TextSendMessage(text="【"+title0+"】"+"\n"+message0+"\n"+"---------------------------------\n【"+title1+"】"+message1+"\n"+"---------------------------------\n【"+title2+"】"+message2+"\n"+"---------------------------------\n【"+title3+"】"+message3+"\n"+"---------------------------------\n【"+title4+"】"+message4)
    line_bot_api.broadcast(messages=messages)
    

schedule.every().day.at("07:00").do(job)



while True:
    schedule.run_pending()
    time.sleep(1)