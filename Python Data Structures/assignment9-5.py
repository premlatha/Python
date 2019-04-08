fname=input('Enter filename:')
try:
    fh=open(fname)
    emails=dict()
    for line in fh:
        if line.startswith('From') and not line.startswith('From:'):
            name=line.split()
            email=name[1]
            emails[email]=emails.get(email,0)+1
except:
    print('File not found')
maxcountvalue=0
for key,value in emails.items():
    if maxcountvalue==0 or value>maxcountvalue:
        maxcountvalue=emails[key]
        maxcountkey=key
print(maxcountkey,maxcountvalue)