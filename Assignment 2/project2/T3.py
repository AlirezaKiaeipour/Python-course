second = int(input('Enter second: '))

h = second // 3600
h_mod = second % 3600
m = h_mod // 60
s = h_mod % 60


print('time is:\t',h,':',m,':',s)
