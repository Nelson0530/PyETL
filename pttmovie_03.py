from bs4 import BeautifulSoup
import requests

url = "https://www.ptt.cc/bbs/movie/index.html"


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
headers = {"User-Agent": user_agent}

for i in range(0, 5):

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    new_url = "http://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]['href']
    print(new_url)
    url = new_url

