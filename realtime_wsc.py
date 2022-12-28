import requests
import re
import datetime
import csv
import time
from bs4 import BeautifulSoup

def CURRENT_DATETIME():
    dt = datetime.datetime.now()
    current_datetime = str(str(dt.year)+"/"+str(dt.month)+"/"+str(dt.day)+" "+str(dt.hour)+":"+str(dt.minute)+":"+str(dt.second))
    return current_datetime

while True:
    trend_list = []
    
    #Yahooリアルタイム検索のURL
    URL = "https://search.yahoo.co.jp/realtime"
    rest = requests.get(URL)
    
    #BeautifulSoupにYahooリアルタイム検索を読み込ませる
    soup = BeautifulSoup(rest.text, "html.parser")
    
    #Yahooリアルタイム検索の見出しとURLの情報を取得して出力する
    for i in range(1,3):
        for j in range(1,11):
            trend_list.append(re.search(r"<h1>(.+)</h1>",str(soup.select("#atkey > section > ol:nth-child("+str(i)+") > li:nth-child("+str(j)+") > a > article > h1"))).group(1))
    
    with open(r"F:\realtime_trend.csv","a",newline="") as f:
        csv_obj = csv.writer(f)
        f.write(CURRENT_DATETIME()+",")
        csv_obj.writerow(trend_list)
    print(".") 
    time.sleep(60*15)
