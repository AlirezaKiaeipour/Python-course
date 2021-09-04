import random

words = ["book" ,"bag","python","clock","orange","apple"]
word = random.choice(words)

char_list =[]
for i in range(len(word)):
    char_list.append("-")



heal = 10
while heal>0:
    

    print(" ".join(char_list))
    if ("".join(char_list))==word:
        print("you are won!")
        break

    input_char = input("Please Enter Character for *GAME*: ").lower()

    if input_char in word:
        for i in range(len(word)):
            if (word[i]== input_char):
                char_list[i] = input_char
                

    else:
        heal = heal -1
        print("Try Agane!!\n your heal is: " ,heal)

            






