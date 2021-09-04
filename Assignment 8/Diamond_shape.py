num = int(input("Please Enter Length: "))
for i in range(num):
    print((num-i)*" ",(i*2-1)*"*",end="")
    print()

for j in range(num,0,-1):
    print((num-j)*" ",(j*2-1)*"*",end="")
    print()
    