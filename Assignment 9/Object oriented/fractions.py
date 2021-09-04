#fractions with class
class Fractions:
    def __init__(self,s,m):
        self.s = s
        self.m = m

    def Show_menu():
        print("***MENU***\n")
        print("1- Sum Tow Fractions")
        print("2- Sub Tow Fractions")
        print("3- Mul Tow Fractions")
        print("4- Div Tow Fractions")
        print("5- Exit")

    def Sum(self,a):
        res = Fractions(None,None)
        res.s = (self.s * a.m) + (a.s * self.m)
        res.m = self.m * a.m
        return res

    def Sub(self,a):
        res = Fractions(None,None)
        res.s = (self.s * a.m) - (a.s * self.m)
        res.m = self.m * a.m
        return res

    def Mul(self,a):
        res= Fractions(None,None)
        res.s = self.s * a.s
        res.m = self.m * a.m
        return res

    def Div(self,a):
        res= Fractions(None,None)
        res.s = self.s * a.m
        res.m = self.m * a.s
        return res

    def Show(self):
        print(self.s,"/",self.m)


Fraction1 = Fractions(int(input("s1: ")),int(input("m1: ")))
Fraction2 = Fractions(int(input("s1: ")),int(input("m2: ")))
while True:
    Fractions.Show_menu()
    choose = input("Please Enter Number Of Menu: ")
    if choose=="1":
        a = Fraction1.Sum(Fraction2)
        a.Show()
    elif choose=="2":
        b = Fraction1.Sub(Fraction2)
        b.Show()
    elif choose=="3":
        c= Fraction1.Mul(Fraction2)
        c.Show()
    elif choose=="4":
        d = Fraction1.Div(Fraction2)
        d.Show()
    elif choose=="5":
        exit()
            