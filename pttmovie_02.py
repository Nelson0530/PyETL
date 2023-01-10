from bs4 import BeautifulSoup
import requests

url = "https://www.ptt.cc/bbs/movie/index{}.html"      # 加上字串format{}


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
headers = {"User-Agent": user_agent}

page = 9499
for i in range(0, 5):          # 爬5頁的迴圈
    res = requests.get(url.format(page), headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    get_title = soup.select('div[class="title"]')    # 取得所有標題

    for title_tag_obj in get_title:
        if title_tag_obj.select_one('a') == None:
            continue
        title_name = title_tag_obj.select_one('a').text
        article_url = "http://www.ptt.cc" + title_tag_obj.select_one('a')["href"]      # 取得完整網址
        print(title_name)
        print(article_url)

    page -= 1       # 往上一頁做迴圈

