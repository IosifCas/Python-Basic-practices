#New attempt to get the gross income from a function
def computepay(h,r) :
    if h < 40 :
        pay = h * r
    elif h > 40 :
        x_hr = h - 40
        x_rt = r * 0.5
        x_pay = x_hr * x_rt
        pay = (h * r) + x_pay
    return pay

hour = input ('Enter Hours:')
hr = float(hour)
rate= input ('Enter Rate:')
rt = float(rate)
p = computepay(hr,rt)
print('Pay',p)    
