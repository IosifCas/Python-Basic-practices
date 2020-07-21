#Program that gets the Gross Income by asking the user to input the hours worked and the rate
hrs = input("Enter Hours:")
rt = input('Enter Rate:')
rate = float(rt)
hour = float(hrs)
if hour > 40:
    extra_hour = hour - 40
    extra_rate = rate / 2
    extra_pay = extra_hour * extra_rate
    g_pay = (hour * rate) + extra_pay
else :
    g_pay = hour * rate
print('Pay:', g_pay)
