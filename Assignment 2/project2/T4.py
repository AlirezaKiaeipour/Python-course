mylist =[]
stu = int(input("Enter number of student: "))

for i in range(stu):
    num = float(input('Enter exam mark: '))
    mylist.append(num)


print('average mark is: ' , sum(mylist) / len(mylist))
print('maximum mark is: ' , max(mylist))
print(' minimum mark is: ' , min(mylist))

