import requests

url = "https://5278-13-231-145-110.ngrok.io/hello_post"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
headers = {"User-Agent": user_agent}

data = {"username":"nelaon"}

res = requests.post(url, headers=headers, data=data)
print(res.text)
