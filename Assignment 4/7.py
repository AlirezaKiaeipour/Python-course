### Lcm(a,b)
a= int(input("Enter frist number :"))
b = int(input("Enter second number: "))
copy_a=a
copy_b=b

if a==0:
    print("lcm is: 0")

elif b==0:
    print("lcm is: 0")

for i in range(1,abs(b)):
    remnant = a % b
    a=b
    b=remnant
    if b==0:
        print(abs(copy_a*copy_b)//a)
        break
        