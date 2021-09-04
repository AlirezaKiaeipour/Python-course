
from pyfiglet import Figlet
from termcolor import colored
user = "admin"
pas = "admin"
f=Figlet(font='standard')
print(colored(f.renderText("Translate"),'yellow'))

mylist=[]

try:

    file = open('translate.txt','r')
    data=file.read().lower().split("\n")
    for i in range(len(data)):
        if i%2==0:
            dic={}
            dic["english"]=data[i]
        else: 
            dic["persian"]=data[i]
            mylist.append(dic)

except: print("Path Database Is Not Currect")
###########################################################################        Add Function
def Add():
    while True:
        add_req = input('Do You Want Add Word?   y/n: ')
        if add_req=="y":
            english = input('Please Enter English Word: ')
            persian = input('Please Enter Persian Word: ')
            mylist.append({'english':english,'persian':persian})
            print('Word Added')
        else:break
##########################################################################        to persian function
english=[]
def to_persaian():
    while True:
        word_en = input('Please Enter Your Text: ')
        en=word_en.lower().split(".")
        for k in range(len(en)):
            eng = en[k].split(" ")
            for j in range(len(eng)):
                for i in range(len(mylist)):
                    if mylist[i]["english"]==eng[j]:
                        english.append(mylist[i]["persian"])
                        break  
                    elif mylist[i]['english']==".":
                        len(mylist)-1
                        english.append("\b.")
        print(" ".join(map(str,english)))
        english.clear()
        to_persaian_req = input("Do You Want Translate Agane?   y/n:")
        if to_persaian_req=="y":continue
        elif to_persaian_req=="n":break    
##################################################################      to english function
persian=[]
def to_english():
    while True:
        word_pe = input('Please Enter Persian Text: ')
        pe= word_pe.lower().split(".")
        for k in range(len(pe)):
            per=pe[k].split(" ")
            for j in range(len(per)):
                for i in range(len(mylist)):
                    if mylist[i]["persian"]==per[j]:
                        persian.append(mylist[i]["english"])
                        break
                    elif mylist[i]["persian"]==".":
                        persian.append("\b.")
        print(" ".join(map(str,persian)))
        persian.clear()
        to_english_req = input('Do You Want Translate Agane?   y/n: ')
        if to_english_req=="y":continue
        elif to_english_req=="n":break
#####################################################################         save function
def Save():
    write_file = open("translate.txt",'w')
    for i in range(len(mylist)):
        data_save = mylist[i]["english"] + "\n" + mylist[i]["persian"]
        write_file.write(str(data_save))
        if i < len(mylist)-1:
            write_file.write("\n")
    write_file.close()
    
############################################################################   show menu function
def show_menu():
    print(colored("***MENU***\n",'red'))
    print(colored('1- Translate To Persian','green'))
    print(colored('2- Translate To English','yellow'))
    print(colored('3- Setting','magenta'))
    print(colored('4- Exit','cyan'))
########################################################################   show menu setting function
def Show_setting_menu():
    print(colored('1- Show Database','red'))
    print(colored('2- Add New Word','blue'))
    print(colored('3- Back To Menu','cyan'))
    print(colored('4- Save & Exit','magenta'))
###############################################################################
while True:
    show_menu()
    choice_menu= input('Please Choice Of Menu: ')
    if choice_menu=="1":
        to_persaian()
    elif choice_menu=="2":
        to_english()
    elif choice_menu=="3":
        admin= input(colored("Are You Administrator?   y/n ",'green'))
        if admin=="y":
            username = input(colored('Please Enter Username: ','yellow'))
            password = input(colored('Please Enter Password: ','yellow'))
            if username=="admin" and password=="admin":
                while True:
                    Show_setting_menu()
                    input_setting = input('Please Choice Of Setting: ')
                    if input_setting =="1":
                        print(mylist)
                    elif input_setting=="2":
                        Add()
                    elif input_setting=="3":
                        break
                    elif input_setting=="4":
                        Save()
                        break
            else:print('Username Or Password Is Not Curect')
        elif admin=="n":pass
    elif choice_menu=="4":
        exit()