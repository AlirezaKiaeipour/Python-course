import string
from random import choice
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.lower_string = string.ascii_lowercase
        self.upper_string = string.ascii_uppercase
        self.num = string.digits
        self.special = string.punctuation
        self.char = list(self.lower_string + self.upper_string + self.num + self.special)
        self.ui.btn.clicked.connect(self.main)

    def main(self):
        if self.ui.combobox.currentText() == "Standard Strong Password":
            self.generate(8)
        elif self.ui.combobox.currentText() == "Extra Strong Password":
            self.generate(12)
        elif self.ui.combobox.currentText() == "Super Strong Password":
            self.generate(20)

    def generate(self,N):
        self.password = []
        for i in range(N):
            self.password.append(choice(self.char))
        self.ui.textbox.setText("".join(map(str,self.password)))
        
app = QApplication([])
window = Main()
app.exec()