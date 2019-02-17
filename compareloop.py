largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        inum=int(num)
    except:
        print('Invalid Input')
    if largest==None or inum > largest:
        largest=inum
    elif smallest==None or inum<smallest:
        smallest=inum  
print("Maximum is", largest)
print("Minimum is", smallest)