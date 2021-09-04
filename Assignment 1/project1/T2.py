
a = int(input('Enter frist number:\t'))
b= int(input('Enter secont number:\t'))
c = int(input('Enter third number:\t'))

if a < b + c:
    if b < a + c:
        if c < a + b:
            print('mosalas!')

        else:
            print('not mosalas!')