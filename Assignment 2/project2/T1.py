
sum = 0

while True:
    num = input('enter number or exit: ')

    if num == 'exit':
        break

    sum = sum + int(num)

print(sum)