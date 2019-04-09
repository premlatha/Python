import json
import urllib.request

url=input('Enter url-')
data=urllib.request.urlopen(url)
jsondata=json.load(data)
sum=0
for info in jsondata['comments']:
    print(info['count'])
    sum+=info['count']
print(sum)