from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.mylist = []
        self.english = []
        self.persian = []
        file = open('translate.txt',encoding='UTF-8')
        data=file.read().lower().split("\n")
        for i in range(len(data)):
            if i%2==0:
                self.dic={}
                self.dic["english"]=data[i]
            else: 
                self.dic["persian"]=data[i]
                self.mylist.append(self.dic)

        self.ui.radio1.setChecked(True)
        self.ui.btn.clicked.connect(self.translate)
        self.ui.help.triggered.connect(self.help)
    
    def translate(self):
        if self.ui.radio1.isChecked():
            self.word_en = self.ui.textbox1.toPlainText()
            self.en=self.word_en.lower().split(".")
            for k in range(len(self.en)):
                self.eng = self.en[k].split(" ")
                for j in range(len(self.eng)):
                    for i in range(len(self.mylist)):
                        if self.mylist[i]["english"]==self.eng[j]:
                            self.english.append(self.mylist[i]["persian"])
                            break  
                        elif self.mylist[i]['english']==".":
                            len(self.mylist)-1
                            self.english.append("\b.")
            self.ui.textbox2.setPlainText(" ".join(map(str,self.english)))
            self.english.clear()
        
        elif self.ui.radio2.isChecked():
            self.word_pe = self.ui.textbox1.toPlainText()
            self.pe= self.word_pe.split(".")
            for k in range(len(self.pe)):
                self.per=self.pe[k].split(" ")
                for j in range(len(self.per)):
                    for i in range(len(self.mylist)):
                        if self.mylist[i]["persian"]==self.per[j]:
                            self.persian.append(self.mylist[i]["english"])
                            break
                        elif self.mylist[i]["persian"]==".":
                            self.persian.append("\b.")
            self.ui.textbox2.setPlainText(" ".join(map(str,self.persian)))
            self.persian.clear()

    def help(self):
        msg = QMessageBox()
        msg.setText("Translate")
        msg.setInformativeText("GUI Translate using Pyside6\nThis program was developed by Alireza Kiaeipour\nContact developer: a.kiaipoor@gmail.com\nBuilt in 2021")
        msg.setIcon(QMessageBox.Information)
        msg.exec()

app = QApplication([])
window = Main()
app.exec()