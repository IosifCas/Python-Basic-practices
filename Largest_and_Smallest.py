#Program to print the largest and smallest numbers
largest = None
smallest = None
while True :
    num = input('Enter a number:')
    if num == 'done' :
        break
    try:
        nmbr = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None :
        largest = nmbr
    elif largest < nmbr :
        largest = nmbr
    if smallest is None :
        smallest = nmbr
    elif smallest > nmbr :
        smallest = nmbr
print ('Maximum is', largest)
print ('Minimum is', smallest)
