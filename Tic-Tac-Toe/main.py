import random
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Tictactoe(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.flag = 0
        self.player1 = 0
        self.player2 = 0
        self.draw = 0
        self.game = [[self.ui.btn1,self.ui.btn2,self.ui.btn3],
                     [self.ui.btn4,self.ui.btn5,self.ui.btn6],
                     [self.ui.btn7,self.ui.btn8,self.ui.btn9]]
        self.ui.radio1.setChecked(True)
        for i in range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.tic_tac_toe,i,j))
        self.ui.btn_new.clicked.connect(self.newgame)
        self.ui.newgame.triggered.connect(self.newgame)
        self.ui.help.triggered.connect(self.help)
               
    def tic_tac_toe(self,i ,j):
            if self.game[i][j].text()=="":
                if self.flag == 0:
                    self.game[i][j].setStyleSheet("color:green;background-color:#63c132;border-width:40px;border-height:40px;border-radius:20px;")
                    self.game[i][j].setText("X") 
                    self.flag = 1
                    self.check()
                    if self.ui.radio2.isChecked():
                        if self.flag ==1:
                            while True:
                                i= random.randint(0,2)
                                j= random.randint(0,2)
                                if self.game[i][j].text()=="":
                                    self.game[i][j].setStyleSheet("color:#ff0035;background-color:#ff6978;border-width:40px;border-height:40px;border-radius:20px;")
                                    self.game[i][j].setText("O")
                                    self.flag = 0
                                    break                 
                else:
                    if self.ui.radio1.isChecked():
                        self.game[i][j].setStyleSheet("color:#ff0035;background-color:#ff6978;border-width:40px;border-height:40px;border-radius:20px;")
                        self.game[i][j].setText("O")
                        self.flag = 0          
            self.check()

    def check(self):
        for i in range(3):
            if all(self.game[i][j].text()=="X" for j in range(3)) or all(self.game[j][i].text()=="X" for j in range(3)) or all(self.game[j][j].text()=="X" for j in range(3)) or self.game[0][2].text()=="X" and self.game[1][1].text()=="X" and self.game[2][0].text()=="X":
                self.player1 +=1
                self.ui.label1.setText(str(self.player1))
                self.win_player("Player 1 Won")
                self.reset()
            elif all(self.game[i][j].text()=="O" for j in range(3)) or all(self.game[j][i].text()=="O" for j in range(3)) or all(self.game[j][j].text()=="O" for j in range(3)) or self.game[0][2].text()=="O" and self.game[1][1].text()=="O" and self.game[2][0].text()=="O":
                self.player2 +=1
                self.ui.label2.setText(str(self.player2))
                self.win_player("Player 2 Won")
                self.reset()
            elif self.game[0][0].text()!="" and self.game[0][1].text()!="" and self.game[0][2].text()!="" and self.game[1][0].text()!="" and self.game[1][1].text()!="" and self.game[1][2].text()!="" and self.game[2][0].text()!="" and self.game[2][1].text()!="" and self.game[2][2].text()!="":
                self.draw +=1
                self.ui.label3.setText(str(self.draw))
                self.win_player("The Game is Draw")
                self.reset()

    def reset(self):
        self.flag = 0
        for i in range(3):
            for j in range(3):
                self.game[i][j].setStyleSheet("QPushButton{ background-color: rgb(242, 175, 41);border-width:40px;border-height:40px;border-radius:20px;} QPushButton::pressed{background-color: rgb(213, 160, 27);}")
                self.game[i][j].setText("")

    def newgame(self):
        self.flag = 0
        for i in range(3):
            for j in range(3):
                self.game[i][j].setStyleSheet("QPushButton{ background-color: rgb(242, 175, 41);border-width:40px;border-height:40px;border-radius:20px;} QPushButton::pressed{background-color: rgb(213, 160, 27);}")
                self.game[i][j].setText("")
                self.player1 = 0
                self.player2 = 0
                self.draw = 0
                self.ui.label1.setText(str(self.player1))
                self.ui.label2.setText(str(self.player2))
                self.ui.label3.setText(str(self.draw)) 
    
    def help(self):
        msg = QMessageBox()
        msg.setText("Tic-Tac-Toe Game")
        msg.setInformativeText("GUI Tic-Tac-Toe Game using Pyside6\nThis program was developed by Alireza Kiaeipour\nContact developer: a.kiaipoor@gmail.com\nBuilt in 2021")
        msg.setIcon(QMessageBox.Information)
        msg.exec()

    def win_player(self,N):
        msg = QMessageBox()
        msg.setText(N)
        msg.setIcon(QMessageBox.Information)
        msg.exec()

app = QApplication([])
window = Tictactoe()
app.exec()