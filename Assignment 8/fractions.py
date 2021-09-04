def Sum(a,b):
    res={}
    if a['m']== b['m']:
        res['s']= a['s'] + b['s']
        res['m']= a['m']
    else:
        res["m"]=a['m'] * b['m']
        res["s"] = (a['s'] * b['m']) + (a['m'] * b['s'])
    return res

def Sub(a,b):
    res={}
    if a['m']== b['m']:
        res['s']= a['s'] - b['s']
        res['m']= a['m']
    else:
        res["m"]=a['m'] * b['m']
        res["s"] = (a['s'] * b['m']) - (a['m'] * b['s'])
    return res

def Mul(a,b):
    res ={}
    res['s']= a['s'] * b['s']
    res['m']= a['m'] * b['m']
    return res

def Div(a,b):
    res ={}
    res['s']= a['s'] * b['m']
    res['m']= a['m'] * b['s']
    return res

k1 = {"s":int(input('Enter S1: ')),"m":int(input('Enter M1: '))}
k2 = {"s":int(input("Enter S2: ")),"m":int(input("Enter M2: "))}
op = input("Please Enter Operation: ")

if op=="+":
   sm = Sum(k1,k2)
   print(sm['s'],'/',sm['m'])
elif op=="-":
    sb= Sub(k1,k2)
    print(sb['s'],'/',sb['m'])
elif op=="*":
    mu = Mul(k1,k2)
    print(mu['s'],'/',mu['m'])
elif op=="/":
    di= Div(k1,k2)
    if k2['s']!=0 and k2['m']!=0:
       print(di['s'],'/',di['m'])
    else: print("No Answer")
