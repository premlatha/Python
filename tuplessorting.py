fname=input('Enter filename:')
if len(fname)<1:fname='mbox-short.txt'
try:
    fh=open(fname)
    hours=dict()
    for line in fh:
        if line.startswith('From') and not line.startswith('From:'):
            words=line.split()
            date=words[5]
            hr=date.split(':')
            hours[hr[0]]=hours.get(hr[0],0)+1
    for k,v in sorted(hours.items()):
        print(k,v)
except:
    print('Cannot open file')
