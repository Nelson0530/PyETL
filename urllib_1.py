from urllib import request
url = "https://5278-13-231-145-110.ngrok.io/hello_get?name=Allen"

res = request.urlopen(url=url)
print(res.read().decode("utf-8"))

