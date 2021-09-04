class Times:
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s

    def Show_menu():
        print("1- Sum Two Time")
        print("2- Sub Two Time")
        print("3- Convert Time To Second")
        print("4- Convert Second To Time")
        print("5- Exit")

    def Sum(self,a):
        res = Times(None,None,None)
        res.s = self.s + a.s
        res.m = self.m + a.m
        res.h = self.h + a.h
        if res.s > 59:
            res.s -=60
            res.m += 1
            if res.m >59:
                res.m -=60
                res.h +=1
        return res

    def Sub(self,a):
        res = Times(None,None,None)
        if a.s > self.s:
            self.m -=1
            self.s +=60
        res.s = self.s - a.s
        if a.m > self.m:
                self.h -=1
                self.m +=60
        res.m = self.m - a.m
        res.h = self.h - a.h
        return res
        
    def Time_to_sec(self):
        res = Times(None,None,None)
        res.s = (self.h * 3600) + (self.m * 60) + self.s
        return res

    def Sec_to_time(self):
        res = Times(None,None,None)
        res.h = self.s // 3600
        res.m = (self.s % 3600) // 60
        res.s = (self.s % 3600) % 60
        return res        

    def Show(self):
        print(self.h,":",self.m,":",self.s)

Time1 = Times(10,0,0)
Time2 = Times(4,55,60)

while True:
    Times.Show_menu()
    choose = input("Enter Number Of Menu: ")
    if choose=="1":
        Time1.Sum(Time2).Show()
    elif choose=="2":
        Time1.Sub(Time2).Show()
    elif choose=="3":
        Time1.Time_to_sec().Show()
    elif choose=="4":
        Time3 = Times(0,0,3602)
        Time3.Sec_to_time().Show()
    elif choose=="5":
        exit()