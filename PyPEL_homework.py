import requests
from bs4 import BeautifulSoup
import json


url = "https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007001000&expansionType=area,spec,com,job,wf,wktm&area=6001005008,6001002023&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"

# res = requests.get(url)
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
headerstr = {"User-Agent": useragent}

res = requests.get(url, headers=headerstr)

soup = BeautifulSoup(res.text, "html.parser")

# print(soup.text)

get_title = soup.select('h2[class="b-tit"]')
print(get_title)

get = get_title[0]('a')

print(get)


#
# for title_tag_obj in get_title:
    # if title_tag_obj.soup.select_one('article') == None:
    #     continue
    # title_name = title_tag_obj.select_one('article').text
    # article_url = "https://www.104.com.tw/" + title_tag_obj.select_one('article')["href"]  # 取得完整網址
    # print(title_name)
    # print(article_url)

# print(res.text)
