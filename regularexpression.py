import re
s='i am new to regularexpression'
e=re.findall('[0-9]+',s)
print(e)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)