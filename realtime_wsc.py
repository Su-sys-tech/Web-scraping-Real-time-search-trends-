import requests
from bs4 import BeautifulSoup
import re
import datetime

dt_now = datetime.datetime.now()
#Yahooリアルタイム検索のURL
URL = "https://search.yahoo.co.jp/realtime"
rest = requests.get(URL)

# BeautifulSoupにYahooリアルタイム検索を読み込ませる
soup = BeautifulSoup(rest.text, "html.parser")

# Yahooリアルタイム検索の見出しとURLの情報を取得して出力する

print(dt_now)
for i in range(1,3):
    for j in range(1,11):
        elems = str(soup.select("#atkey > section > ol:nth-child("+str(i)+") > li:nth-child("+str(j)+") > a > article > h1"))
        new_str = re.search(r"<h1>(.+)</h1>",elems).group(1)
        print(new_str)
            
