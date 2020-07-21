#Program that gets the Gross Income by asking the user to input the hours worked and the rate using a function
def usr_npt(data) :
    if data == 'h' :
        d = input ('Enter Hours:')
    else :
        d = input ('Enter Rate:')
    return d

def convert (val) :
    v = float (val)
    return v

def computepay(h,r) :
    if h > 40:
        extra_hour = h - 40
        extra_rate = r * 0.5
        extra_pay = extra_hour * extra_rate
        pay = (h * r) + extra_pay
    else :
        pay = h * r
    return pay

hrs = usr_npt('h')
rt = usr_npt('ra')
r = convert(rt)
hr = convert(hrs)
p = computepay(hr, r)
print ('Pay:', p)
