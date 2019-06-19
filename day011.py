#homework1：定义一个函数
import urllib.request
import urllib.parse
def getHtml(url):
    page = urllib.urlopen(url)
    HTML = page.read()
    return HTML

a = input("Input: ")   
data = urllib.parse.urlencode({'wd':'a'})
print(data)
url = 'http://www.baidu.com/s?'+data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)

#把路由和参数写活
url = "https://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

data = {
    "pw": "123", "un": "456"
}

data = bytes(urllib.parse.urlencode({'pw':'123','un':'456'}),encoding("utf-8")
response = urllib.request.urlopen(url, data=data)
result = response.read().decode('utf8')
print(sesult)