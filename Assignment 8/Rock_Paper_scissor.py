import random
def show():
    print("Computer Choice: ",computer)
    print("Player: ",score["player"]," Computer: ",score["computer"])
game= ["Rock","Paper","Scissor"]
score={"player":0,"computer":0}

game_round = int(input("Please Enter Round Of Game: "))
for i in range(game_round):
    computer= random.choice(game)
    player= input("Please Enter Rock OR Paper OR Scissor: ").capitalize()
    if player == "Rock" and computer== "Paper":
        score["computer"]+=1
        show()
    elif player == "Rock" and computer== "Scissor":
        score["player"]+=1
        show()
    elif player == "Paper" and computer=="Rock":
        score["player"]+=1
        show()
    elif player == "Paper" and computer== "Scissor":
        score["computer"]+=1
        show()
    elif player == "Scissor" and computer== "Rock":
        score["computer"]+=1
        show()
    elif player == "Scissor" and computer== "Paper":
        score["player"]+=1
        show()
    elif player==computer:
        print("Round Is Equal")
        show()
        continue

if score["player"]>score["computer"]:
    print("Player Is Won!")
elif score["computer"]>score["player"]:
    print("Computer Is Won!")
else: print("Game Is Equal")
