from pyfiglet import Figlet
from termcolor import colored
from media import Media
from clip import Clip
from doc import Doc
from series import Series
from film import Film
f = Figlet(font='colossal')
print (colored(f.renderText('KIA'),"green"))
print (colored(f.renderText('MEDIA'),"yellow"))  
mylist = []
data = open("data.txt","r")
data = data.read().lower().split("\n")
for i in range(len(data)):
    file = data[i].split(",")
    if file[0]=="film":
        mylist.append(Film(file[0],file[1],file[2],file[3],file[4],file[5],file[6],file[7]))
    elif file[0]=="series":
        mylist.append(Series(file[0],file[1],file[2],file[3],file[4],file[5],file[6],file[7]))
    elif file[0]=="clip":
        mylist.append(Clip(file[0],file[1],file[2],file[3],file[4],file[5],file[6],file[7]))
    elif file[0]=="doc":
        mylist.append(Doc(file[0],file[1],file[2],file[3],file[4],file[5],file[6],file[7]))

def Add():
    choice = input(colored("Please choose For Add   Film/Series/Clip/Doc: ","cyan")).lower()
    if choice == "film":
        mylist.append(Film("film",input("Please Enter Movie Name: "),input("Please Enter Director: "),
        input("Please Enter IMDB: "),input("Please Enter Url: "),input("Please Enter Duration: "),
        input("Please Enter Actor And split With (/): "),input("Please Enter Year: ")))
    elif choice == "series":
        mylist.append(Series("series",input("Please Enter Movie Name: "),input("Please Enter Director: "),
        input("Please Enter IMDB: "),input("Please Enter Url: "),input("Please Enter Duration: "),
        input("Please Enter Actor And split With (/): "),input("Please Enter Season: ")))
    elif choice == "clip":
        mylist.append(Clip("clip",input("Please Enter Movie Name: "),input("Please Enter Director: "),
        input("Please Enter IMDB: "),input("Please Enter Url: "),input("Please Enter Duration: "),
        input("Please Enter Actor And split With (/): "),input("Please Enter about: ")))
    elif choice == "doc":
        mylist.append(Doc("doc",input("Please Enter Movie Name: "),input("Please Enter Director: "),
        input("Please Enter IMDB: "),input("Please Enter Url: "),input("Please Enter Duration: "),
        input("Please Enter Actor And split With (/): "),input("Please Enter Type: ")))
   
def Delete():
    choice = input(colored("Please Enter Name For Delete: ","cyan"))
    for i in mylist:
        if choice == i.name:
            mylist.remove(i)

def Edit():
    choice = input(colored("Please Enter Name For Edit: ","cyan"))
    for i in mylist:
        if choice == i.name:
            if i.group == "film":
                i = i.edit_film()
            elif i.group == "series":
                i = i.edit_series()
            elif i.group == "clip":
                i = i.edit_clip()
            elif i.group == "doc":
                i = i.edit_doc()

def Search_group():
    choice = input(colored("Please Enter Media Group: ","cyan"))
    for i in mylist:
        if i.group == choice:
            i.show_info()

def Search_name():
    choice = input(colored("Please Enter Media Name: ","cyan"))
    for i in mylist:
        if i.name == choice:
            i.show_info()

def Search_duration():
    choice1 = int(input(colored("Please Enter Frist Duration: ","cyan")))
    choice2 = int(input(colored("Please Enter Second Duration: ","cyan")))
    for i in mylist:
        if choice1 <= int(i.duration) <= choice2:
            i.show_info()

def download():
    choice = input(colored("Please Enter Name Media: ","cyan"))
    for i in mylist:
        if choice == i.name:
            i.Download()

def Show_list():
    for i in mylist:
        i.show_info()

def Save():
    file = open("data.txt","w")
    for i in mylist:
        if i.group == "film":
            file.write(i.group + "," + i.name + "," + i.director + "," + i.imdb + "," + i.url + "," + i.duration + "," + i.cast + "," + i.year)
            if i != mylist[-1]:
                file.write("\n")
        elif i.group == "series":
            file.write(i.group + "," + i.name + "," + i.director + "," + i.imdb + "," + i.url + "," + i.duration + "," + i.cast + "," + i.season)
            if i != mylist[-1]:
                file.write("\n")
        elif i.group == "clip":
            file.write(i.group + "," + i.name + "," + i.director + "," + i.imdb + "," + i.url + "," + i.duration + "," + i.cast + "," + i.about)
            if i != mylist[-1]:
                file.write("\n")
        elif i.group == "doc":
            file.write(i.group + "," + i.name + "," + i.director + "," + i.imdb + "," + i.url + "," + i.duration + "," + i.cast + "," + i.type)
            if i != mylist[-1]:
                file.write("\n")
    file.close()
    exit()

def Menu():
    print(colored("*** MENU ***","yellow"))
    print(colored("1- Download Media","green"))
    print(colored("2- Search Media","magenta"))
    print(colored("3- Setting","blue"))
    print(colored("4- Exit","red"))

def Search_menu():
    print(colored("1- Search by Group","cyan"))
    print(colored("2- Search by Name","yellow"))
    print(colored("3- Search by Duration","green"))

def Setting_menu():
    print(colored("1- Show Media","blue"))
    print(colored("2- Add Media","red"))
    print(colored("3- Edit Media","magenta"))
    print(colored("4- Delete Media","green"))
    print(colored("5- Save & Exit","yellow"))
    print(colored("6- Menu","grey"))
    
while True:
    Menu()
    input_menu = input(colored("Please Choice Menu: ","cyan"))
    if input_menu =="1":
        download()
    elif input_menu =="2":
        Search_menu()
        input_search = input(colored("Please Choice Serach Plan: ","cyan"))
        if input_search =="1":
            Search_group()
        elif input_search =="2":
            Search_name()
        elif input_search =="3":
            Search_duration()
    elif input_menu =="3":
        admin = input(colored("Are You Admin?  y/n: ","cyan"))
        if admin == "y":
            username = input(colored("Please Enter Username: ","blue"))
            password = input(colored("Please Enter Password: ","red"))
            if username =="admin" and password =="admin":
                while True:
                    Setting_menu()
                    input_setting = input(colored("Please Choice Setting Menu: ","cyan"))
                    if input_setting =="1":
                        Show_list()
                    elif input_setting =="2":
                        Add()
                    elif input_setting =="3":
                        Edit()
                    elif input_setting =="4":
                        Delete()
                    elif input_setting =="5":
                        Save()
                    elif input_setting =="6":
                        break
            else:
                print(colored("Username OR Password is Not Currect!","red"))
                break
        else:
            print(colored("You Must Be Admin!","red"))
            break
    elif input_menu =="4":
        exit()