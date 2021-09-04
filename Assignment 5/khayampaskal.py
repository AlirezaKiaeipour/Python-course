
num = int(input("Enter number for Triangle: "))

array=[[1 for i in range(num)]
         for j in range(num)]

for i in range(num):
    for j in range(1,i):
        array[i][j] = array[i-1][j] + array[i-1][j-1]

for i in range(num):
    for j in range(i+1):
        print(array[i][j],end="\t")
    print()
    