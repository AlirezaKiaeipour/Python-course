def show_menu():
    print('1- Sum Two Time')
    print('2- Sub Two Time')
    print('3- Convert Second To Time')
    print('4- Convert Time To Second')

def Sum(a,b):
    res ={}
    res['s']= a['s'] + b['s']
    res['m']= a['m'] + b['m']
    res['h']= a['h'] + b['h']
    res['d']= a['d']
    if res['s']>59:
        res['s']-=60
        res['m']+=1
        if res['m']>59:
            res['m']-=60
            res['h']+=1
            if res['h']>=24:
                res['h']-=24
                res['d']+=1
    return res

def Sub(a,b):
    res={}
    if b['s']>a['s']:
        a['m']-=1
        a['s']+=60
        if b['m']>a['m']:
            a['h']-=1
            a['m']+=60
    res["s"]= a['s'] - b['s']
    res["m"]= a['m'] - b['m']
    res["h"]= a['h'] - b['h']
    return res

def Sec(a):
    res={}
    res['h']= a['s']//3600
    h_mod = a['s'] %3600
    res['m']= h_mod//60
    res['s']= h_mod%60
    return res

def Time(a):
    res= {}
    res['sec']= a['s'] + (a['m'] * 60) + (a['h'] * 3600)
    return res

show_menu()
op = input("Please Enter Operation: ")

if op=="1":
    t1 = {'h':int(input("Please Enter Hour: ")),'m':int(input("Please Enter minute: ")),"s":int(input("Please Enter second: ")),"d":0}
    t2 = {'h':int(input("Please Enter Hour: ")),'m':int(input("Please Enter minute: ")),"s":int(input("Please Enter second: ")),"d":0}
    sm= Sum(t1,t2)
    print("Time is ",sm['d'],":",sm['h'],":",sm['m'],":",sm['s'])
elif op=="2":
    t1 = {'h':int(input("Please Enter Hour: ")),'m':int(input("Please Enter minute: ")),"s":int(input("Please Enter second: "))}
    t2 = {'h':int(input("Please Enter Hour: ")),'m':int(input("Please Enter minute: ")),"s":int(input("Please Enter second: "))}
    sb=Sub(t1,t2)
    print("Time is: ",sb['h'],":",sb['m'],":",sb['s'])
elif op=="3":
    S= {'s':int(input("Please Enter Second: "))}
    se= Sec(S)
    print("Time is: ",se['h'],":",se['m'],":",se['s'])
elif op=="4":
    T = {"h":int(input("Enter Hour: ")),"m":int(input("Enter Minute: ")),"s":int(input("Enter Second: "))}
    ti= Time(T)
    print("Second is: ",ti['sec'])