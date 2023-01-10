import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/photo/index.html"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
headers = {"User-Agent": user_agent}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")       # 指定使用"html.parser"這個轉換器

title_tag_list = soup.select('div[class="title"]')
print(title_tag_list)
print(title_tag_list[0])         # 取得標籤物件

# title_detail_tag = title_tag_list[0].select_one('a')           # 可混用，同義
title_detail_tag = title_tag_list[0].find('a')              # 可混用，同義
print(title_detail_tag)

print(type(title_tag_list[0]))
print(type(soup))                    # 注意回傳值是什麼屬性

