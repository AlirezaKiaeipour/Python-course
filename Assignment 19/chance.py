import random
boys = []
girls = []
number = int(input("Please enter number of boys and girls: "))
for boy in range(number):
    boys.append(input(f"Please enter name of boy {boy}: "))

for girl in range(number):
    girls.append(input(f"Please enter name of girl {girl}: "))

print(random.sample(list(zip(boys,girls)),number))
