def ComputePay(h,r):
    if h<=40:
        pay=h*r
    else:
        exth=h-40
        pay=(40*r)+(exth*(1.5*r))
    return pay

hr=float(input('Enter hours :'))
rate=float(input('Enter rate :'))
p=ComputePay(hr,rate)
print(p)
