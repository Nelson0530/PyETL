from bs4 import BeautifulSoup
import os            # 呼應地10行
import requests

url = "https://www.ptt.cc/bbs/movie/index.html"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
headers = {"User-Agent": user_agent}

if not os.path.exists("pttmovie"):
    os.mkdir("pttmovie")          # 創建新資料夾

for i in range(0, 5):          # 爬5頁的迴圈
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    get_title = soup.select('div[class="title"]')    # 取得所有標題

    for title_tag_obj in get_title:
        if title_tag_obj.select_one('a') == None:
            continue
        title_name = title_tag_obj.select_one('a').text
        article_url = "http://www.ptt.cc" + title_tag_obj.select_one('a')["href"]      # 取得完整網址

        article_res = requests.get(article_url, headers=headers)

        article_soup = BeautifulSoup(article_res.text, "html.parser")
        article_tag_obj = article_soup.select_one('div[id="main-content"]')
        article_content = article_tag_obj.text.split("※ 發信站")[0]        # split() 切割文章

        word_list = ['/', '?', '-']
        for w in word_list:
            if w in title_name:
                title_name =title_name.replace(w, '')

        try:
            with open("pttmovie/{}.txt".format(title_name), "w", encoding='utf-8') as f:        # open()對檔案進行操作
                f.write(article_content)                 # 寫入檔案
        except FileNotFoundError:
            # print("pttmovie/{}.txt".format(title_name.replace('/', '-')))
            with open("pttmovie/{}.txt".format(title_name.replace('/', '-')), 'w', encoding='utf-8') as f:
                f.write(article_content)
        except OSError:
            pass

        print(title_name)
        print(article_url)

        new_url = "http://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]['href']
        url = new_url

