score=input('Enter score :')
try:
    fscore=float(score)
    if fscore>=0.9:
        print('Your Grade:','A')
    elif fscore>=0.8:
        print('Your Grade:','B')
    elif fscore>=0.7:
        print('Your Grade:','C')
    elif fscore>=0.6:
        print('Your Grade:','D')
    else:
        print('Your Grade:','F')
except:
    print('Error! Enter score between 0.0 and 0.1')