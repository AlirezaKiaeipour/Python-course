import random
hand = ["✋","🤚"]
user_score = 0
computer1_score = 0
computer2_score = 0
for i in range(5):
    user = input("Please Enter ✋ or 🤚: ")
    computer1 = random.choice(hand)
    computer2 = random.choice(hand)
    if user == computer1 == computer2:
        print(user,computer1,computer2)
        print("Game is draw")
    elif user == "🤚" and computer1 == "✋" and computer2 == "✋":
        user_score +=1
        print("User: ",user_score,"Computer1: ",computer1_score,"Computer2: ",computer2_score)
    elif user == "✋" and computer1 == "🤚" and computer2 == "🤚":
        user_score +=1
        print("User: ",user_score,"Computer1: ",computer1_score,"Computer2: ",computer2_score)
    elif user == "🤚" and computer1 == "✋" and computer2 == "🤚":
        computer1_score +=1
        print("User: ",user_score,"Computer1: ",computer1_score,"Computer2: ",computer2_score)
    elif user == "✋" and computer1 == "🤚" and computer2 == "✋":
        computer1_score +=1
        print("User: ",user_score,"Computer1: ",computer1_score,"Computer2: ",computer2_score)
    elif user == "✋" and computer1 == "✋" and computer2 == "🤚":
        computer2_score +=1
        print("User: ",user_score,"Computer1: ",computer1_score,"Computer2: ",computer2_score)
    elif user == "🤚" and computer1 == "🤚" and computer2 == "✋":
        computer2_score +=1
        print("User: ",user_score,"Computer1: ",computer1_score,"Computer2: ",computer2_score)

if user_score > computer1_score and user_score> computer2_score:
    print("You win")
elif computer1_score > user_score and computer1_score>computer2_score:
    print("Computer1 is Win")
elif computer2_score > user_score and computer2_score>computer1_score:
    print("Computer2 is Win")
elif user_score == computer1_score or user_score == computer2_score or computer2_score==computer1_score:
    print("Game is Draw")