mylist = []
length = int(input("Please enter length of list: "))
for i in range(length):
    mylist.append(int(input("Please Enter number: ")))

symmetric_list = len(mylist)//2
if len(mylist) % 2 == 0:
    first_list = mylist[:symmetric_list]
    second_list = mylist[symmetric_list:]
else:
    first_list = mylist[:symmetric_list]
    second_list = mylist[symmetric_list+1:]

second_list.reverse()
if first_list == second_list:
    print("Yes. This is symmetric array")
else:print("No. This is not symmetric array")
