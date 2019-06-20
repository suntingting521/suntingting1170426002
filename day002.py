import urllib.request
url = 'http://www.baidu.com'
proxy_handle = {
    'http':'http://119.176.96.134:9999',
    'http':'http://1.198.73.189:9999'
 }
 proxy = urllib.request.ProxyHandler(proxy_handle)
 opener = urllib.request.build_opener(proxy)
 response = opener.open(url)
 print(response.status)





 headers = {
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
 }
 cookie = http.cookiejar.CookieJar()
 cookie = http.cookiejar.MozillaCookieJar()
 handler = urllib.request.HTTPCookieProcessor(cookie)
 opener = urllib.request.build_opener(handler)
 url = 'http://www.baidu.com'
 request = urllib.request.Request(url,headers=headers)
 response = opener.open(request)
 for item in cookie:
     print(item.name,item.value)
     filename = 'Joker.txt'
     cookie.save(filename=filename,ignore_discard=True,ignore_expires=True)
     cookie = http.cookiejar.MozillaCookieJar()
     cookie.load('Joker.txt')
     print(cookie)

