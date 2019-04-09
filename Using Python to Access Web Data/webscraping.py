import urllib
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


url=input('Enter Url -')
data=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(data,'html.parser')

spans=soup('span')
sum=0
for span in spans:
#    print('span:',span)
#    print('Contents:',span.contents[0])
#    print('Attr:',span.attrs)
    sum+=int(span.contents[0])
print('Sum=',sum)