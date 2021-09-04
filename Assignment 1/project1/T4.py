name = input('Enter your first name:\t')
last = input('Enter your last name:\t')

a = int(input('Enter your dars1:\t'))
b = int(input('Enter your dars2:\t'))
c = int(input('Enter your dars3:\t'))

avg = (a+b+c)/3

if avg >= 17:
    print(name , last, ': your average is',avg ,'.\n your status is Great')

elif avg > 17 and avg <= 12:
    print(name,last,': your average is',avg ,'.\n your status Normal') 

else:
    print(name,last,': your average is',avg ,'.\n your status is Fail')