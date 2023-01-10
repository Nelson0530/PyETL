import requests
from bs4 import BeautifulSoup

url = "https://testselect.uuboyscy.repl.co/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
headers = {"User-Agent": user_agent}

data = {}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

input_tag_list = soup.select('input[type="hidden"]')
print(input_tag_list)

for tag in input_tag_list:
    data[tag['name']] = tag['value']

print(data)
data['2A'] = 'dog'

print(requests.post("https://www.w3schools.com/action_page.php", headers=headers, data=data).text)

