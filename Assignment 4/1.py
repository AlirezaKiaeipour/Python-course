
def Checkered_page(m,n):
    
    for i in range(1,m):
        for j in range(1,n):
            if (i+j)%2==0:
                print("*",end=" ")
            else:
                print("#",end=" ")
        print("")
                     


Checkered_page(int(input("Enter frist parameter: ")),int(input("Enter second parameter: ")))

