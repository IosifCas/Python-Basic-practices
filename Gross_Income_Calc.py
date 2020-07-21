#Program that gets the Gross Income by asking the user to input the hours worked and the rate 
hrs = input("Enter Hours:")
rt = input('Enter Rate:')
rate = float(rt)
hour = float(hrs)
g_pay = hour * rate
print('Pay:', g_pay)
