
mylist = []
num = int(input('Enter number: '))

for i in range(num):
    if i <= 1:
        mylist.append(1)

    else:
        mylist.append(mylist[i-1]+mylist[i-2])

print(mylist)