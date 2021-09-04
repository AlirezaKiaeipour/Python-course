import random
length_array = int(input("Enter length array: "))
num = int(input("Enter length of number:"))

if num>= length_array:
    ran = random.sample(range(0,num),length_array)
    print(ran)

else:
    print("length array is small")

