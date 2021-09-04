import math
a = int(input('Enter frist number:\t'))
op = input('Enter operator:\t')


if op == 'sin' or op == 'cos' or op == 'tan' or op =='radical' or op == 'factorial':
    if op == 'radical':
        res = math.sqrt(a)
    
    elif op == 'sin':
     res = math.sin(math.radians(a))
    
    elif op == 'cos':
        res = math.cos(math.radians(a))
   
    elif op == 'tan':
     res = math.tan(math.radians(a))
   
    elif op == 'factorial':
        res = math.factorial(a)
else:
   
    b = int(input('Enter second number:\t'))

    if op == '+':
        res = a +b
    elif op == '-':
        res = a-b

    elif op == '*':
        res = a*b

    elif op =='/':
        if b !=0:
            res = a/b
        else:
            res="can't divide by zero"   
print(res)


 