import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/photo/index.html"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
headers = {"User-Agent": user_agent}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text)         # 能run，但會出現警告訊息，因沒有設定轉換器

print(soup)
