import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


serviceurl = input('Enter XML url -')
uh = urllib.request.urlopen(serviceurl)
data = uh.read()
tree = ET.fromstring(data)

sum=0
for result in tree.findall('.//count'):
    sum+=int(result.text)
    
print(sum)