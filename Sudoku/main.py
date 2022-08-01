import random
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui",None)
        self.ui.show()
        self.ui.newgame.clicked.connect(self.newgame)
        self.ui.check.clicked.connect(self.check)
        self.ui.reset.clicked.connect(self.reset)
        self.ui.darkmod.triggered.connect(self.darkmod)
        self.ui.lightmod.triggered.connect(self.lightmod)
        self.ui.ac_newgame.triggered.connect(self.newgame)
        self.ui.exit.triggered.connect(exit)
        self.ui.help.triggered.connect(self.help)
        self.ui.autocheck.triggered.connect(self.auto)
        self.game = [[None for i in range(9)]   for j in range(9)]
        for i in range(9):
            for j in range(9):
                textbox = QLineEdit()
                textbox.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
                textbox.setAlignment(Qt.AlignCenter)
                textbox.setStyleSheet("font-size: 22px;")
                self.game[i][j] = textbox
                self.ui.gridlayout.addWidget(textbox,i,j)
        self.mod =0
                
    def newgame(self):  
        for i in range(9):
            for j in range(9):
                self.game[i][j].setReadOnly(False)
                self.game[i][j].setText("")
        try:
            data = open(f"data/s{random.randint(1,7)}.txt","r")
            data = data.read().split("\n")
            for i in range(9):
                num = data[i].split(" ")
                for j in range(9):                
                    if num[j] !="0":
                        self.game[i][j].setText(num[j])
                        self.game[i][j].setReadOnly(True)
                        if self.mod ==1:
                            self.game[i][j].setStyleSheet("background-color:#333333;font-size:22px;color:white")
                        else:
                            self.game[i][j].setStyleSheet("font-size:22px;color:black")
                    else:
                        if self.mod == 1:
                            self.game[i][j].setStyleSheet("color:white;font-size:22px")
                        else:
                            self.game[i][j].setStyleSheet("color:black;font-size:22px")
        except:
            self.ui.label.setText("We Are Ofline")

    def reset(self):
        for i in range(9):
            for j in range(9):
                if self.game[i][j].isReadOnly()==False:
                    self.game[i][j].setText("")
                    if self.mod ==1:
                            self.game[i][j].setStyleSheet("background-color:#333333;font-size:22px;color:white")
                    else:
                            self.game[i][j].setStyleSheet("font-size:22px;color:black")
                if self.game[i][j].isReadOnly():
                    if self.mod ==1:
                            self.game[i][j].setStyleSheet("background-color:#333333;font-size:22px;color:white")
                    else:
                            self.game[i][j].setStyleSheet("font-size:22px;color:black")

    def check(self):
        self.win = 0
        for i in range(9):
            for j in range(9):
                if self.mod ==1:
                    self.game[i][j].setStyleSheet("background-color:#333333;color: white;font-size:22px")
                else: 
                    self.game[i][j].setStyleSheet("color: black;font-size:22px")

        for i in range(9):
            for j in range(9):
                if self.game[i][j].text()=="":
                    self.win =1

        for row in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text() ==self.game[row][j].text() and i!=j and self.game[row][i].text()!="":
                        self.game[row][i].setStyleSheet("background-color: pink;color: red;font-size:22px")
                        self.win =1

        for col in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text() ==self.game[j][col].text() and i!=j and self.game[i][col].text()!="":
                        self.game[i][col].setStyleSheet("background-color: pink;color: red;font-size:22px")
                        self.win =1
          
        for row in range(0,3):
            for col in range(0,3):
                for i in range(0,3):
                    for j in range(0,3):
                        if self.game[row][col].text() ==self.game[i][j].text() and row!=i and col!=j and self.game[row][col].text()!='':
                            self.game[row][col].setStyleSheet("background-color: pink;color: red;font-size:22px")
                            self.win =1
            for col in range(3,6):
                for i in range(0,3):
                    for j in range(3,6):
                        if self.game[row][col].text() ==self.game[i][j].text() and row!=i and col!=j and self.game[row][col].text()!='':
                            self.game[row][col].setStyleSheet("background-color: pink;color: red;font-size:22px")
                            self.win =1
            for col in range(6,9):
                for i in range(0,3):
                    for j in range(6,9):
                        if self.game[row][col].text() ==self.game[i][j].text() and row!=i and col!=j and self.game[row][col].text()!='':
                            self.game[row][col].setStyleSheet("background-color: pink;color: red;font-size:22px")
                            self.win =1

        for row in range(3,6):
            for col in range(0,3):
                for i in range(3,6):
                    for j in range(0,3):
                        if self.game[row][col].text() ==self.game[i][j].text() and row!=i and col!=j and self.game[row][col].text()!='':
                            self.game[row][col].setStyleSheet("background-color: pink;color: red;font-size:22px")
                            self.win =1
            for col in range(3,6):
                for i in range(3,6):
                    for j in range(3,6):
                        if self.game[row][col].text() ==self.game[i][j].text() and row!=i and col!=j and self.game[row][col].text()!='':
                            self.game[row][col].setStyleSheet("background-color: pink;color: red;font-size:22px")
                            self.win =1
            for col in range(6,9):
                for i in range(3,6):
                    for j in range(6,9):
                        if self.game[row][col].text() ==self.game[i][j].text() and row!=i and col!=j and self.game[row][col].text()!='':
                            self.game[row][col].setStyleSheet("background-color: pink;color: red;font-size:22px")
                            self.win =1

        for row in range(6,9):
            for col in range(0,3):
                for i in range(6,9):
                    for j in range(0,3):
                        if self.game[row][col].text() ==self.game[i][j].text() and row!=i and col!=j and self.game[row][col].text()!='':
                            self.game[row][col].setStyleSheet("background-color: pink;color: red;font-size:22px")
                            self.win =1
            for col in range(3,6):
                for i in range(6,9):
                    for j in range(3,6):
                        if self.game[row][col].text() ==self.game[i][j].text() and row!=i and col!=j and self.game[row][col].text()!='':
                            self.game[row][col].setStyleSheet("background-color: pink;color: red;font-size:22px")
                            self.win =1
            for col in range(6,9):
                for i in range(6,9):
                    for j in range(6,9):
                        if self.game[row][col].text() ==self.game[i][j].text() and row!=i and col!=j and self.game[row][col].text()!='':
                            self.game[row][col].setStyleSheet("background-color: pink;color: red;font-size:22px")
                            self.win =1
        if self.win==0:
            msg = QMessageBox()
            msg.setText("You Win")
            msg.setIcon(QMessageBox.Information)
            msg.exec()
                    
    def darkmod(self):
        self.mod = 1
        self.ui.setStyleSheet("background-color:#333333")
        self.ui.menubar.setStyleSheet("color:white;background-color:#292929")
        for i in range(9):
            for j in range(9):
                self.game[i][j].setStyleSheet("background-color:#333333;color:white;font-size: 22px")
    
    def lightmod(self):
        self.mod = 0
        self.ui.setStyleSheet("background-color:#d6e6ec")
        self.ui.menubar.setStyleSheet("color:black;background-color:#c4d3d8")
        for i in range(9):
            for j in range(9):
                self.game[i][j].setStyleSheet("background-color:#d6e6ec;color:black;font-size: 22px")

    def help(self):
        msg = QMessageBox()
        msg.setText("Sudoku")
        msg.setInformativeText("Sudoku using Pyside6\nThis program was developed by Alireza Kiaeipour\nContact developer: a.kiaipoor@gmail.com\nBuilt in 2021")
        msg.setIcon(QMessageBox.Information)
        msg.exec()

    def auto(self,):
        self.ui.check.setEnabled(False)
        for i in range(9):
            for j in range(9):
                self.game[i][j].textChanged.connect(self.check)

app = QApplication()
window = Main()
app.exec()