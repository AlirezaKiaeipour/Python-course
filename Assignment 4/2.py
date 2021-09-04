import math

def second_degree(a,b,c):
    delta = (b**2)-(4*a*c)
    radical = math.sqrt(abs(delta))
    

    if delta > 0:
        print("delta is 2:")
        print(round((-b + radical)/(2*a),1))
        print(round((-b - radical)/(2*a),1))
         

    elif delta==0:
        print("delta is 1:")
        print(round(-b/(2*a),1))
        
    
    else: 
        print("delta is 0 and no answer")

   
second_degree(a=int(input("a: ")),b=int(input("b:")),c=int(input("c: ")))



