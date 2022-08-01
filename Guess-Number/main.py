from random import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.number = randint(1,50)
        self.score = 10
        self.ui.btn_guess.clicked.connect(self.play)
        self.ui.btn_reset.clicked.connect(self.reset)
        self.ui.newgame.triggered.connect(self.reset)
        self.ui.help.triggered.connect(self.help)

    def play(self):
        self.score -=1
        self.ui.label1.setText(str(self.score))
        self.ui.textbox.setText("")
        self.user = self.ui.spinbox.value()
        if self.user > self.number:
            self.ui.textbox.setStyleSheet("color:white;background-color:#ff6978;border-radius: 10px;font: 700 17pt 'Segoe UI';")
            self.ui.textbox.setText("Go Down")
        elif self.user < self.number:
            self.ui.textbox.setStyleSheet("color:white;background-color:#ff6978;border-radius: 10px;font: 700 17pt 'Segoe UI';")
            self.ui.textbox.setText("Go Up")
        elif self.user == self.number:
            self.ui.textbox.setStyleSheet("color:white;background-color:#63c132;border-radius: 10px;font: 700 17pt 'Segoe UI';")
            self.ui.textbox.setText("You Win")
            self.message("You Win")
            self.ui.btn_guess.setEnabled(False)
        if self.score ==0:
            self.ui.textbox.setStyleSheet("color:white;background-color:#ff6978;border-radius: 10px;font: 700 17pt 'Segoe UI';")
            self.ui.textbox.setText("Game Over")
            self.message("Game Over")
            self.ui.btn_guess.setEnabled(False)

    def reset(self):
        self.number = randint(1,50)
        self.score = 10
        self.ui.btn_guess.setEnabled(True)
        self.ui.textbox.setText("")
        self.ui.textbox.setStyleSheet("color:white;background-color: rgb(253, 255, 108);;border-radius: 10px;font: 700 17pt 'Segoe UI';")
        self.ui.spinbox.clear()
        self.ui.label1.setText(str(self.score))

    def message(self,M):
        msg = QMessageBox()
        msg.setText(M)
        msg.setIcon(QMessageBox.Information)
        msg.exec()

    def help(self):
        msg = QMessageBox()
        msg.setText("Guess Number\n\nGUI Guess Number Game using Pyside6\nThis program was developed by Alireza Kiaeipour\nContact developer: a.kiaipoor@gmail.com\nBuilt in 2021")
        msg.setIcon(QMessageBox.Information)
        msg.exec()

app = QApplication([])
window = Main()
app.exec()