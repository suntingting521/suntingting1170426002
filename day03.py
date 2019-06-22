import requests
url = 'http://www.baidu.com/s?'
def baidu(wds):
    count = 1
    for wd in wds:
        res = requests.get(url,params={'wd':wd})
        path = 'res%d.txt'%count
        with open(path,'w',encoding='utf8') as f:
           f.write(res.text)
        count +=1

if __name__ == "__main__":
    wds =('Joker','美女','丑女')  
    baidu(wds)


if 'http' in res1 or 'https' in res1:
    res4 = res1.spilt('(')
    for i in res4:
        if 'http' in res4 or 'https' in res4:
            res5 = res4.spilt('):')
            print(res5)






import requests
URLS = []
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML = response.text
lines = HTML.split('\n')
for line in lines:
    if 'jpg' in url:
        URLS.append(url)
    


for url in URLS:
    response = requests.get(url)
    content = response.content
    name = url.split('/')
    with open(name,'wb') as f:
        f.write(content)           
   
    
    









