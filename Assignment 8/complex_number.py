def Sum_(a,b):
    res= {}
    res["h"]= a["h"] + b["h"]
    res["m"]= a['m'] + b['m']
    return res

def Sub_(a,b):
    res= {}
    res['h']= a['h'] - b['h']
    res['m']= a['m'] - b['m']
    return res

def Mul_(a,b):
    res= {}
    res['h']= (a['h'] * b['h']) - (a['m'] * b['m'])
    res['m']= (a['m'] * b['h']) + (a['h'] * b['m'])
    return res

c1 = {"h":int(input("h1: ")),"m":int(input("m1: "))}
c2 = {"h":int(input("h2: ")),"m":int(input("m2: "))}
op = input("Please Enter Operation: ")


if op=="+":
    sm = Sum_(c1,c2)
    print(complex(sm['h'],sm['m']))
elif op=="-":
    sb = Sub_(c1,c2)
    print(complex(sb['h'],sb['m']))
elif op=="*":
    mu = Mul_(c1,c2)
    print(complex(mu['h'],mu['m']))
