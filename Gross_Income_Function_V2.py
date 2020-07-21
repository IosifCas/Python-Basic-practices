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

def hourly (h, r) :
    if h > 40:
        extra_hour = h - 40
        extra_rate = r * 0.5
        extra_pay = extra_hour * extra_rate
        pay = computepay (h, r, extra_pay)
    else :
        pay = computepay (h, r, 0)
    return(pay)

def computepay(h, r, x_p) :
    p = (h * r) + x_p
    return p

hrs = usr_npt('h')
hr = convert(hrs)
rt = usr_npt('ra')
r = convert(rt)
pay = hourly (hr, r)
print ('Pay:', pay)
