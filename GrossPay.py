hour=float(input("Enter hour :"))
rate=float(input('Enter rate per hour :'))
if hour<=40:
    pay=hour*rate
else:
    extrahr=hour-40
    pay=(40*rate)+(extrahr*(1.5 * rate))
print(pay)
