#Grading system with try and except to validate
score = input('Enter score: ')
try :
     iscore = float(score)
except :
    iscore = -1
    quit ()
if iscore >= 0.9 :
    print('A')
elif iscore >= 0.8 :
    print('B')
elif iscore >= 0.7 :
    print('C')
elif iscore >= 0.6 :
    print ('D')
elif iscore < 0.6 :
    print ('F')
else :
    print('Invalid score')
