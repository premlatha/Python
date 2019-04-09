import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Print url-')
count=int(input('Enter count-'))
position=int(input('Enter position-'))
while count:
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')
    anchors=soup('a')
    url=anchors[position-1].get('href',None)
    print('anchor:',url)
    print('name:',anchors[position-1].contents[0])
    count-=1