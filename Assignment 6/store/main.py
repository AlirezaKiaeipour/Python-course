from pyfiglet import Figlet
import qrcode
from termcolor import colored

f= Figlet(font="standard")
print(f.renderText("KIA STORE"))
########################################################
my_list=[]
myfile = open("database.txt","r")
data = myfile.read().lower().split("\n")
for i in range(len(data)):
    products = data[i].split(",")
    dic = {}
    dic["id"]= products[0]
    dic["name"]= products[1]
    dic["price"]= products[2]
    dic["count"]= products[3]
    my_list.append(dic)
#######################################################                                   ADD Function
def Add():
    while True:
        dic_add={}
        Add_Reques = input(colored("Do You Want Add Product to Database?  y/n: ","blue"))
        if Add_Reques == "y":
            dic_add["id"]= input(colored("Please Enter Id Of Product: ","blue"))
            dic_add["name"]= input(colored("please Enter Name Of Product: ","blue"))
            dic_add["price"]= input(colored("Please Enter Price Of Product: ","blue"))
            dic_add["count"]= input(colored("Please Enter Count Of Product: ","blue"))
            print("New Product Added!")
            my_list.append(dic_add)
        elif Add_Reques == "n":break
########################################################                                 Delete Function           
def Delete():
    while True:
        Delete_Reques = input("Do You Want Delete Product to Database?  y/n ")
        if Delete_Reques=="y":
            choice_Delete = input("Please Enter Id You Want Delete: ")
            for i in range(len(my_list)):
                if my_list[i]["id"]==choice_Delete:
                    my_list.pop(i)
                    print("Product Deleted")
                    break 
        elif Delete_Reques=="n": break
#######################################################                                   Edit Function
def Edit():
    while True:
        Edit_Reques = input("Do You Want Edit Product?   y/n: ")
        if Edit_Reques=="y":
            print(colored("1- Edit Id product","blue"))
            print(colored("2- Edit Name product","red"))
            print(colored("3- Edit Price product","green"))
            print(colored("4- Edit Count product","yellow"))

            choice_Edit_Menu = input("Please Enter Number Of Edit Menu: ")
            id_edit=input("Please Enter Product Id: ")
            for i in range(len(my_list)):
                if my_list[i]["id"]==id_edit:
                    if choice_Edit_Menu=="1":
                        my_list[i]["id"]=input("Please Enter Id: ")
                    elif choice_Edit_Menu=="2":
                        my_list[i]["name"]=input("Please Enter Name: ")
                    elif choice_Edit_Menu=="3":
                        my_list[i]["price"]=input("Please Enter Price: ")
                    elif choice_Edit_Menu=="4":
                        my_list[i]["count"]=input("Please Enter count: ")
                    else:print("Id Not Exist")
                    break
        elif Edit_Reques=="n":break
##############################################################################                     Search Function
def Search():
    while True:
        Search_Reques = input("Do You Want Search Product?   y/n: ")
        if Search_Reques=="y":
            name_search = input("Please Enter Word For Search: ")
            for i in range(len(my_list)):
                if my_list[i]["name"]==name_search:
                    print("Product Founded")
                    print({"id":my_list[i]["id"],"name":my_list[i]["name"],"price":my_list[i]["price"],"count":my_list[i]["count"]})
                    
                    break
            else:print("Product Not Found")
        elif Search_Reques=="n":break
##############################################################################
def buy():
    sum_price=0
    sum_count=0
    factor=[]
    while True:
        
        Buy_Reques = input("Do You Want Buy Product?   y/n: ")
        if Buy_Reques=="y":
            print(my_list)

            Id_buy = input("Please Enter Id of List: ")
            for i in range(len(my_list)):
                if my_list[i]["id"]==Id_buy:
                    print("Product Exist\n")
                    count_buy = int(input("Please Enter Count Of List: "))
                    if count_buy> int(my_list[i]["count"]):
                        print("not count exist")

                    else:           
                        my_list[i]["count"] = str(int(my_list[i]["count"]) - count_buy)
                        sum_price  =sum_price + (int(my_list[i]["price"]) * count_buy)
                        sum_count = sum_count + count_buy

                        print("***FACTOR***\n")
                        fact={"price":my_list[i]["price"],"sum_price":str(sum_price),"sum_count":str(sum_count)}
                        factor.append(fact)
                        print(factor)

                    break
                else: print("Product Not Exist")
        else:break
##############################################################################
def qr():
    print(my_list)
    while True:
        qr_Reques = input(colored("Do You Want QR CODE Product?   y/n: ","cyan"))
        if qr_Reques=="y":
            Id_qr = input(colored("Enter Id Of List: ","cyan"))
            for i in range(len(my_list)):
                if my_list[i]["id"]== Id_qr:
                    qrfile = {"id":my_list[i]["id"],"name":my_list[i]["name"],"price":my_list[i]["price"],"count":my_list[i]["count"]}
                    image = qrcode.make(qrfile)
                    image.save("mystore.png")
                    print("QR code Created")
                    break
            else: print("Id is not exist")
        elif qr_Reques=="n":break
###################################################################################
def save():
    while True:
        Save_Reques = input("Do You Want Exit&Save  OR  Exit  OR Save?  save/exit: ")
        if Save_Reques=="save":
           
            file = open("database.txt","w")
            for i in range(len(my_list)):
                save_file = my_list[i]["id"]+","+ my_list[i]["name"]+","+ my_list[i]["price"] +","+ my_list[i]["count"]
                file.write(str(save_file))
                if i < len(my_list)-1:
                    file.write("\n")
            file.close()           
            exit()
            break

        elif Save_Reques=="exit":
            exit()
#################################################################################3
def show_menu():
    print(colored("    ***Menu***\n\n","yellow"))
    print(colored("1- Show product","red"))
    print(colored("2- Add product","blue"))
    print(colored("3- Edit products","yellow"))
    print(colored("4- Delete product","green"))
    print(colored("5- Buy product","magenta"))
    print(colored("6- Search Product","grey"))
    print(colored("7- Qr product","cyan"))
    print("8- Save & Exit")
##########################################################################
while True:

    show_menu()

    choice = input(colored("\nPlease Enter Number Of Menu: ","magenta"))

    if choice =="1":
        print(my_list)
        print(len(my_list))

    elif choice =="2":
        Add()

    elif choice =="3":
        Edit()

    elif choice =="4":
        Delete()

    elif choice == "5":
        buy()

    elif choice =="6":
        Search()

    elif choice =="7":
        qr()

    elif choice=="8":
       save()

