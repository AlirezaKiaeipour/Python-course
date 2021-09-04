### factorial

num = int(input("Enter number: "))
n =0

def factorial(n):
    if n==0 or n==1:
        return 1

    else:
        return n * factorial(n-1)


while True:
    n+=1
    if factorial(n)== num:
        print("is True: ","factorial ",n,"is ",factorial(n))
        break

    if factorial(n)>num:
        print('is False')
        break
    
    









