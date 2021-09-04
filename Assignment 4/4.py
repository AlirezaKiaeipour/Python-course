
def count_text(text):

    count = 1
    for i in text:
        if i==" ":
            count +=1
    return count

print(count_text(input("Enter text:\n")))
