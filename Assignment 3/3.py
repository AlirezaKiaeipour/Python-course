mylist = []
while True:
    num = input("Enter number or exit: ")
    if num =="exit":
        break
    mylist.append(int(num))

mylist_copy = mylist.copy()
mylist_copy.sort()

if (mylist == mylist_copy):
    print("This Array is sort!!!")
    print(mylist)

else:
    print("This Array is not sort")
    mylist.sort()
    print("sort Array is: " , mylist)
