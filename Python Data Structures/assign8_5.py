fname=input('Enter file name:')
try:
    fh=open(fname)
    emails=list()
    count=0
    for line in fh:
        if line.startswith('From') and not line.startswith('From:'):
            linelist=line.split()
            address=linelist[1]
            emails.append(address)
            count=count+1
except:
    print('Invalid filename')
for email in emails:
    print(email)
print('There were',count,'lines in the file with From as the first word')