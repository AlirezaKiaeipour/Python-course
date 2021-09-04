###  gcd(a,b)
a = int(input("Enter frist number: "))
b = int(input("Enter second number:"))

if a==0:
    print("gcd is: ",b)

elif b==0:
    print("gcd is ",a)

for i in range(1,abs(b)):   

    remnant = a % b
    a=b
    b= remnant
    if b==0:
         print("gcd is: ",a)
         break
        


    



