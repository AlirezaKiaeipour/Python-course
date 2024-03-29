import math
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui",None)
        self.ui.show()
        self.ui.btn0.clicked.connect(self.number0)
        self.ui.btn1.clicked.connect(self.number1)
        self.ui.btn2.clicked.connect(self.number2)
        self.ui.btn3.clicked.connect(self.number3)
        self.ui.btn4.clicked.connect(self.number4)
        self.ui.btn5.clicked.connect(self.number5)
        self.ui.btn6.clicked.connect(self.number6)
        self.ui.btn7.clicked.connect(self.number7)
        self.ui.btn8.clicked.connect(self.number8)
        self.ui.btn9.clicked.connect(self.number9)
        self.ui.btn_ac.clicked.connect(self.ac)
        self.ui.btn_dot.clicked.connect(self.number_dot)
        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_sin.clicked.connect(self.sin)
        self.ui.btn_cos.clicked.connect(self.cos)
        self.ui.btn_tan.clicked.connect(self.tan)
        self.ui.btn_sqrt.clicked.connect(self.sqrt)
        self.ui.btn_log.clicked.connect(self.log)
        self.ui.btn_cot.clicked.connect(self.cot)
        self.ui.btn_sign.clicked.connect(self.sign)
        self.ui.btn_percent.clicked.connect(self.percent)
        self.ui.btn_eq.clicked.connect(self.eq)       

    def number0(self):
        self.ui.textbox.setText(self.ui.textbox.text()+"0")
    def number1(self):
        self.ui.textbox.setText(self.ui.textbox.text()+"1")
    def number2(self):
        self.ui.textbox.setText(self.ui.textbox.text()+"2")
    def number3(self):
        self.ui.textbox.setText(self.ui.textbox.text()+"3")
    def number4(self):
        self.ui.textbox.setText(self.ui.textbox.text()+"4")
    def number5(self):
        self.ui.textbox.setText(self.ui.textbox.text()+"5")
    def number6(self):
        self.ui.textbox.setText(self.ui.textbox.text()+"6")
    def number7(self):
        self.ui.textbox.setText(self.ui.textbox.text()+"7")
    def number8(self):
        self.ui.textbox.setText(self.ui.textbox.text()+"8")
    def number9(self):
        self.ui.textbox.setText(self.ui.textbox.text()+"9")
    def number_dot(self):
        for i in self.ui.textbox.text():
            if "." in self.ui.textbox.text():
                break
            else:
                self.ui.textbox.setText(self.ui.textbox.text()+".")
    def ac(self):
        self.ui.textbox.setText("")
    
    
    def sum(self):
        self.opp = "+"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")

    def sub(self):
        self.opp = "-"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")

    def mul(self):
        self.opp = "*"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")

    def div(self):
        self.opp = "/"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")

    def sin(self):
        self.opp = "sin"
        self.ui.textbox.setText("Sin ")

    def cos(self):
        self.opp = "cos"
        self.ui.textbox.setText("Cos ")

    def tan(self):
        self.opp = "tan"
        self.ui.textbox.setText("Tan ")

    def sqrt(self):
        self.opp = "sqrt"
        self.ui.textbox.setText("√ ")

    def log(self):
        self.opp = "log"
        self.ui.textbox.setText("log ")

    def cot(self):
        self.opp = "cot"
        self.ui.textbox.setText("Cot ")

    def percent(self):
        self.opp = "%"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")       
        self.ui.textbox.setText(str(self.num1/100))

    def sign(self):
        self.opp = "+/-"
        self.num = float(self.ui.textbox.text())
        self.ui.textbox.setText(str(-1 * self.num))

    def eq(self):
        if self.opp =="+":
            self.num2 = float(self.ui.textbox.text())
            self.ui.textbox.setText(str(self.num1+self.num2))

        if self.opp =="-":
            self.num2 = float(self.ui.textbox.text())
            self.ui.textbox.setText(str(self.num1 - self.num2))

        if self.opp =="*":
            self.num2 = float(self.ui.textbox.text())
            self.ui.textbox.setText(str(self.num1 * self.num2))

        if self.opp =="/":
            self.num2 = float(self.ui.textbox.text())
            if self.num2 !=0:
                self.ui.textbox.setText(str(self.num1/self.num2))
            else:
                self.ui.textbox.setText("Can't divide by zero")
        
        if self.opp =="sin":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(math.sin(math.radians((self.num1)))))

        if self.opp =="cos":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(math.cos(math.radians(self.num1))))

        if self.opp =="tan":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(math.tan(math.radians(self.num1))))

        if self.opp =="sqrt":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(math.sqrt(self.num1)))

        if self.opp =="log":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(math.log(self.num1)))

        if self.opp =="cot":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            if self.num1 != 0:
                cal_sin = math.sin(math.radians(self.num1))
                cal_cos = math.cos(math.radians(self.num1))
                self.ui.textbox.setText(str(cal_cos/cal_sin))
            else:
                self.ui.textbox.setText("Can't divide by zero")

app = QApplication([])
window = Main()
app.exec()