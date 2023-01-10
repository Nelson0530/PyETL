import requests

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
headers = {"User-Agent": user_agent}

cookies = {"over18": "1"}

res = requests.get(url, headers=headers, cookies=cookies)

print(res.text)
