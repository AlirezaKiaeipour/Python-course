import random
hand = ["✋","🤚"]
user_score = 0
computer1_score = 0
computer2_score = 0
for i in range(5):
    user = input("Please Enter ✋ or 🤚: ")
    computer1 = random.choice(hand)
    computer2 = random.choice(hand)
    if user == "✋" and computer1 == "✋" and computer2 == "✋":
        print(user,computer1,computer2)
        print("Game is draw")
    elif user == "🤚" and computer1 == "✋" and computer2 == "✋":
        user_score +=1
        print("User: ",user_score," Computer 1: ",computer1_score," Computer 2: ",computer2_score)
    elif user == "✋" and computer1 == "🤚" and computer2 == "🤚":
        user_score +=1
        print("User: ",user_score," Computer 1: ",computer1_score," Computer 2: ",computer2_score)
    elif user == "🤚" and computer1 == "✋" and computer2 == "🤚":
        computer1_score +=1
        print("User: ",user_score," Computer 1: ",computer1_score," Computer 2: ",computer2_score)
    elif user == "✋" and computer1 == "🤚" and computer2 == "✋":
        computer1_score +=1
        print("User: ",user_score," Computer 1: ",computer1_score," Computer 2: ",computer2_score)
    elif user == "✋" and computer1 == "✋" and computer2 == "🤚":
        computer2_score +=1
        print("User: ",user_score," Computer 1: ",computer1_score," Computer 2: ",computer2_score)
    elif user == "🤚" and computer1 == "🤚" and computer2 == "✋":
        computer2_score +=1
        print("User: ",user_score," Computer 1: ",computer1_score," Computer 2: ",computer2_score)
    elif user == "🤚" and computer1 == "🤚" and computer2 == "🤚":
        print("Game is draw")
        print("User: ",user_score," Computer 1: ",computer1_score," Computer 2: ",computer2_score)

if user_score > computer1_score and computer2_score:
    print("Yes. You Win")
elif computer1_score > user_score and computer2_score:
    print("Computer 1 is Win")
elif computer2_score > user_score and computer1_score:
    print("Computer 2 is Win")
else:
    print("Game is Draw")