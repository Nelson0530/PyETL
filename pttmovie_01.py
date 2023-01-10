from bs4 import BeautifulSoup
import requests

url = "https://www.ptt.cc/bbs/movie/index.html"


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
headers = {"User-Agent": user_agent}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

get_title = soup.select('div[class="title"]')    # 取的所有標題

for title_tag_obj in get_title:
    if title_tag_obj.select_one('a') == None:
        continue
    title_name = title_tag_obj.select_one('a').text
    article_url = "http://www.ptt.cc" + title_tag_obj.select_one('a')["href"]      # 取得完整網址
    print(title_name)
    print(article_url)
