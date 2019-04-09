import re

file=open('regex.txt')
sum=0
count=0
for line in file:
    ch=re.findall('[0-9]+',line)
    if len(ch)>0:
        count+=len(ch)
        for each in ch:
            sum+=int(each)
print(sum)
