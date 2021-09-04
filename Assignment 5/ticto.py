import random
from typing import AnyStr
import time
from colorama import Fore
from termcolor import colored


def cheak():
    
    for i in range(3):
        if table_board[i][0]==colored("x","red") and table_board[i][1]==colored("x","red") and table_board[i][2]==colored("x","red"):
            print("player 1 is won")
            print("Time out is: ", time.time() - start_time)
            exit()
        elif table_board[i][0]==colored("o","blue") and table_board[i][1]==colored("o","blue") and table_board[i][2]==colored("o","blue"):
            print("player 2 is won")
            print("Time out is: ", time.time() - start_time)
            exit()
    for i in range(3):
        if table_board[0][i]==colored("x","red") and table_board[1][i]==colored("x","red") and table_board[2][i]==colored("x","red"):
            print("player 1 is won")
            print("Time out is: ", time.time() - start_time)
            exit()
        elif table_board[0][i]==colored("o","blue") and table_board[1][i]==colored("o","blue") and table_board[2][i]==colored("o","blue"):
            print("player 2 is won")
            print("Time out is: ", time.time() - start_time)
            exit()


    if  table_board[0][0]==colored("x","red") and table_board[1][1]==colored("x","red") and table_board[2][2]==colored("x","red"):
            print("player 1 is won")
            print("Time out is: ", time.time() - start_time)
            exit()
    elif table_board[0][0]==colored("o","blue") and table_board[1][1]==colored("o","blue") and table_board[2][2]==colored("o","blue"):
            print("player 2 is won")
            print("Time out is: ", time.time() - start_time)
            exit()
    elif table_board[0][2]==colored("x","red") and table_board[1][1]==colored("x","red") and table_board[2][0]==colored("x","red"):
            print("player 1 is won")
            print("Time out is: ", time.time() - start_time)
            exit()
    elif table_board[0][2]==colored("o","blue") and table_board[1][1]==colored("o","blue") and table_board[2][0]==colored("o","blue"):
            print("player 2 is won")
            print("Time out is: ", time.time() - start_time)
            exit()

    elif table_board[0][0]!="_" and table_board[0][1]!="_" and table_board[0][2]!="_" and table_board[1][0]!="_" and table_board[1][1]!="_" and table_board[1][2]!="_" and table_board[2][0]!="_" and table_board[2][1]!="_" and table_board[2][2]!="_":
        print("Game is draw")
        print("Time out is: ", time.time() - start_time)
        exit()

    
def mytable():
    for i in range(3):
        for j in range(3):
            print(table_board[i][j], end=" ")
        print()


def player():
    while True:
            print("Player 1: ")
            i= int(input("Enter frist number: "))
            j= int(input("Enter second number: "))
            if 0<=i<=2 and 0<=j<=2:
                if table_board[i][j]=="_":
                    table_board[i][j]= colored("x","red")
                    mytable()  
                    break
                else:
                    print("is not empty")
            else: print("Try agane")
    cheak()

start_time=time.time()
table_board = [["_","_","_"]
              ,["_","_","_"]
              ,["_","_","_"]]


choice = input("choose player vs pc? ")
if choice == "player":


    mytable()
    while True:
        player()
        
        while True:
            print("Player 2: ")
            i= int(input("Enter frist number: "))
            j= int(input("Enter second number: "))
            if 0<=i<=2 and 0<=j<=2:
                if table_board[i][j]=="_":
                    table_board[i][j]=colored("o","blue")
                    mytable() 
                    break
                else:
                    print("is not empty")
            else:
                print("Try agane")
        cheak()

 
elif choice =="pc":


       
        mytable()
        while True:
            player()

            while True:
                    print("Player 2: ")
                    i= random.randint(0,2)
                    j= random.randint(0,2)
                    if 0<=i<=2 and 0<=j<=2:
                        if table_board[i][j]=="_":
                            table_board[i][j]= colored("o","blue")
                            mytable() 
                            break
                        else:
                            print("is not empty")
                    else:
                        print("Try agane")
            cheak()