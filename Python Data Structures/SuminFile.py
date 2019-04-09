fname=input('Enter filename:')
try:
    print(fname)
    with open(fname) as fh:
        avg=0.0
        count=0
        for line in fh:
            if line.startswith('X-DSPAM-Confidence:'):
                cpos=line.find(':')
                lvalue=line[cpos+1:].lstrip().rstrip()
                avg=avg+float(lvalue)
                count+=1
    print('Average spam confidence:',avg/count)
except:
    print('file not found')
    quit()