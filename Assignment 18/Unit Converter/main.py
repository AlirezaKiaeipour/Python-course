from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui",None)
        self.ui.show()
        self.ui.btn_weight.clicked.connect(self.weight)
        self.ui.btn_length.clicked.connect(self.length)
        self.ui.btn_temp.clicked.connect(self.temp)
        self.ui.btn_digital.clicked.connect(self.digital)
        self.ui.help.triggered.connect(self.message)
        self.ui.exit.triggered.connect(self.ex)

    def weight(self):
        if self.ui.combo_fw.currentText() == "gram" and self.ui.combo_tw.currentText() == "gram":
            self.ui.textbox_w2.setText(self.ui.textbox_w1.text())
        elif self.ui.combo_fw.currentText() == "gram" and self.ui.combo_tw.currentText() == "Kilogram":
            self.ui.textbox_w2.setText(str(float(self.ui.textbox_w1.text())/1000))
        elif self.ui.combo_fw.currentText() == "gram" and self.ui.combo_tw.currentText() == "Pound":
            self.ui.textbox_w2.setText(str(float(self.ui.textbox_w1.text())*0.0022))
        elif self.ui.combo_fw.currentText() == "gram" and self.ui.combo_tw.currentText() == "Ton":
            self.ui.textbox_w2.setText(str(float(self.ui.textbox_w1.text())/10**6))
        elif self.ui.combo_fw.currentText() == "Kilogram" and self.ui.combo_tw.currentText() == "gram":
            self.ui.textbox_w2.setText(str(float(self.ui.textbox_w1.text())*1000))
        elif self.ui.combo_fw.currentText() == "Kilogram" and self.ui.combo_tw.currentText() == "Kilogram":
            self.ui.textbox_w2.setText(self.ui.textbox_w1.text())
        elif self.ui.combo_fw.currentText() == "Kilogram" and self.ui.combo_tw.currentText() == "Pound":
            self.ui.textbox_w2.setText(str(float(self.ui.textbox_w1.text())*2.2046))
        elif self.ui.combo_fw.currentText() == "Kilogram" and self.ui.combo_tw.currentText() == "Ton":
            self.ui.textbox_w2.setText(str(float(self.ui.textbox_w1.text())/1000))
        elif self.ui.combo_fw.currentText() == "Pound" and self.ui.combo_tw.currentText() == "gram":
            self.ui.textbox_w2.setText(str(float(self.ui.textbox_w1.text())/0.0022))
        elif self.ui.combo_fw.currentText() == "Pound" and self.ui.combo_tw.currentText() == "Kilogram":
            self.ui.textbox_w2.setText(str(float(self.ui.textbox_w1.text())/2.2046))
        elif self.ui.combo_fw.currentText() == "Pound" and self.ui.combo_tw.currentText() == "Pound":
            self.ui.textbox_w2.setText(self.ui.textbox_w1.text())
        elif self.ui.combo_fw.currentText() == "Pound" and self.ui.combo_tw.currentText() == "Ton":
            self.ui.textbox_w2.setText(str(float(self.ui.textbox_w1.text())*0.0005))
        elif self.ui.combo_fw.currentText() == "Ton" and self.ui.combo_tw.currentText() == "gram":
            self.ui.textbox_w2.setText(str(float(self.ui.textbox_w1.text())*10**6))
        elif self.ui.combo_fw.currentText() == "Ton" and self.ui.combo_tw.currentText() == "Kilogram":
            self.ui.textbox_w2.setText(str(float(self.ui.textbox_w1.text())*1000))
        elif self.ui.combo_fw.currentText() == "Ton" and self.ui.combo_tw.currentText() == "Pound":
            self.ui.textbox_w2.setText(str(float(self.ui.textbox_w1.text())/0.0005))
        elif self.ui.combo_fw.currentText() == "Ton" and self.ui.combo_tw.currentText() == "Ton":
            self.ui.textbox_w2.setText(self.ui.textbox_w1.text())

    def length(self):
        if self.ui.combo_fl.currentText() == "millimeter" and self.ui.combo_tl.currentText() == "millimeter":
            self.ui.textbox_l2.setText(self.ui.textbox_l1.text())
        elif self.ui.combo_fl.currentText() == "millimeter" and self.ui.combo_tl.currentText() == "Centimeter":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*0.1))
        elif self.ui.combo_fl.currentText() == "millimeter" and self.ui.combo_tl.currentText() == "Meter":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*0.001))
        elif self.ui.combo_fl.currentText() == "millimeter" and self.ui.combo_tl.currentText() == "Kilometers":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*1*10**-6))
        elif self.ui.combo_fl.currentText() == "millimeter" and self.ui.combo_tl.currentText() == "Inches":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())* 0.0393700787))
        elif self.ui.combo_fl.currentText() == "Centimeter" and self.ui.combo_tl.currentText() == "millimeter":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())/ 10))
        elif self.ui.combo_fl.currentText() == "Centimeter" and self.ui.combo_tl.currentText() == "Centimeter":
            self.ui.textbox_l2.setText(self.ui.textbox_l1.text())
        elif self.ui.combo_fl.currentText() == "Centimeter" and self.ui.combo_tl.currentText() == "Meter":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())* 0.01))
        elif self.ui.combo_fl.currentText() == "Centimeter" and self.ui.combo_tl.currentText() == "Kilometers":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*1*10**-5))
        elif self.ui.combo_fl.currentText() == "Centimeter" and self.ui.combo_tl.currentText() == "Inches":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())* 0.3937007874))
        elif self.ui.combo_fl.currentText() == "Meter" and self.ui.combo_tl.currentText() == "millimeter":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*1000))
        elif self.ui.combo_fl.currentText() == "Meter" and self.ui.combo_tl.currentText() == "Centimeter":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())* 100))
        elif self.ui.combo_fl.currentText() == "Meter" and self.ui.combo_tl.currentText() == "Meter":
            self.ui.textbox_l2.setText(self.ui.textbox_l1.text())
        elif self.ui.combo_fl.currentText() == "Meter" and self.ui.combo_tl.currentText() == "Kilometers":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())* 0.001))
        elif self.ui.combo_fl.currentText() == "Meter" and self.ui.combo_tl.currentText() == "Inches":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())* 39.3700787))
        elif self.ui.combo_fl.currentText() == "Kilometers" and self.ui.combo_tl.currentText() == "millimeter":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*10**6))
        elif self.ui.combo_fl.currentText() == "Kilometers" and self.ui.combo_tl.currentText() == "Centimeter":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*10**5))
        elif self.ui.combo_fl.currentText() == "Kilometers" and self.ui.combo_tl.currentText() == "Meter":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*10**3))
        elif self.ui.combo_fl.currentText() == "Kilometers" and self.ui.combo_tl.currentText() == "Kilometers":
            self.ui.textbox_l2.setText(self.ui.textbox_l1.text())
        elif self.ui.combo_fl.currentText() == "Kilometers" and self.ui.combo_tl.currentText() == "Inches":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*39370.0787))
        elif self.ui.combo_fl.currentText() == "Inches" and self.ui.combo_tl.currentText() == "millimeter":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*25.4))
        elif self.ui.combo_fl.currentText() == "Inches" and self.ui.combo_tl.currentText() == "Centimeter":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*2.54))
        elif self.ui.combo_fl.currentText() == "Inches" and self.ui.combo_tl.currentText() == "Meter":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*0.0254))
        elif self.ui.combo_fl.currentText() == "Inches" and self.ui.combo_tl.currentText() == "Kilometers":
            self.ui.textbox_l2.setText(str(float(self.ui.textbox_l1.text())*2.54*10**(-5)))
        elif self.ui.combo_fl.currentText() == "Inches" and self.ui.combo_tl.currentText() == "Inches":
            self.ui.textbox_l2.setText(self.ui.textbox_l1.text())

    def temp(self):
        if self.ui.combo_ft.currentText() == "Celsius" and self.ui.combo_tt.currentText() == "Celsius":
            self.ui.textbox_t2.setText(self.ui.textbox_t1.text())
        elif self.ui.combo_ft.currentText() == "Celsius" and self.ui.combo_tt.currentText() == "Fahrenheit":
            self.ui.textbox_t2.setText(str(float(self.ui.textbox_t1.text())+32))
        elif self.ui.combo_ft.currentText() == "Celsius" and self.ui.combo_tt.currentText() == "Kelvin":
            self.ui.textbox_t2.setText(str(float(self.ui.textbox_t1.text())+273.15))
        elif self.ui.combo_ft.currentText() == "Fahrenheit" and self.ui.combo_tt.currentText() == "Celsius":
            self.ui.textbox_t2.setText(str(float(self.ui.textbox_t1.text())-32))
        elif self.ui.combo_ft.currentText() == "Fahrenheit" and self.ui.combo_tt.currentText() == "Fahrenheit":
            self.ui.textbox_t2.setText(self.ui.textbox_t1.text())
        elif self.ui.combo_ft.currentText() == "Fahrenheit" and self.ui.combo_tt.currentText() == "Kelvin":
            self.ui.textbox_t2.setText(str((float(self.ui.textbox_t1.text())+459.67)*5//9))
        elif self.ui.combo_ft.currentText() == "Kelvin" and self.ui.combo_tt.currentText() == "Celsius":
            self.ui.textbox_t2.setText(str(float(self.ui.textbox_t1.text())-273.15))
        elif self.ui.combo_ft.currentText() == "Kelvin" and self.ui.combo_tt.currentText() == "Fahrenheit":
            self.ui.textbox_t2.setText(str(float(self.ui.textbox_t1.text())* 9/5-459.67))
        elif self.ui.combo_ft.currentText() == "Kelvin" and self.ui.combo_tt.currentText() == "Kelvin":
            self.ui.textbox_t2.setText(self.ui.textbox_t1.text())

    def digital(self):
        if self.ui.combo_fd.currentText() == "Bit" and self.ui.combo_td.currentText() == "Bit":
            self.ui.textbox_d2.setText(self.ui.textbox_d1.text())
        elif self.ui.combo_fd.currentText() == "Bit" and self.ui.combo_td.currentText() == "byte":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*1/8))
        elif self.ui.combo_fd.currentText() == "Bit" and self.ui.combo_td.currentText() == "KB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*(1/8)*10**-3))
        elif self.ui.combo_fd.currentText() == "Bit" and self.ui.combo_td.currentText() == "MB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*(1/8)*10**-6))
        elif self.ui.combo_fd.currentText() == "Bit" and self.ui.combo_td.currentText() == "GB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*(1/8)*10**-9))
        elif self.ui.combo_fd.currentText() == "Bit" and self.ui.combo_td.currentText() == "TB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*(1/8)*10**-12))
        elif self.ui.combo_fd.currentText() == "byte" and self.ui.combo_td.currentText() == "Bit":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*8))
        elif self.ui.combo_fd.currentText() == "byte" and self.ui.combo_td.currentText() == "byte":
            self.ui.textbox_d2.setText(self.ui.textbox_d1.text())
        elif self.ui.combo_fd.currentText() == "byte" and self.ui.combo_td.currentText() == "KB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**-3))
        elif self.ui.combo_fd.currentText() == "byte" and self.ui.combo_td.currentText() == "MB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**-6))
        elif self.ui.combo_fd.currentText() == "byte" and self.ui.combo_td.currentText() == "GB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**-9))
        elif self.ui.combo_fd.currentText() == "byte" and self.ui.combo_td.currentText() == "TB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**-12))
        elif self.ui.combo_fd.currentText() == "KB" and self.ui.combo_td.currentText() == "Bit":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*8*10**3))
        elif self.ui.combo_fd.currentText() == "KB" and self.ui.combo_td.currentText() == "byte":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**3))
        elif self.ui.combo_fd.currentText() == "KB" and self.ui.combo_td.currentText() == "KB":
            self.ui.textbox_d2.setText(self.ui.textbox_d1.text())
        elif self.ui.combo_fd.currentText() == "KB" and self.ui.combo_td.currentText() == "MB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**-3))
        elif self.ui.combo_fd.currentText() == "KB" and self.ui.combo_td.currentText() == "GB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**-6))
        elif self.ui.combo_fd.currentText() == "KB" and self.ui.combo_td.currentText() == "TB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**-9))
        elif self.ui.combo_fd.currentText() == "MB" and self.ui.combo_td.currentText() == "Bit":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*8*10**6))
        elif self.ui.combo_fd.currentText() == "MB" and self.ui.combo_td.currentText() == "byte":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**6))
        elif self.ui.combo_fd.currentText() == "MB" and self.ui.combo_td.currentText() == "KB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**3))
        elif self.ui.combo_fd.currentText() == "MB" and self.ui.combo_td.currentText() == "MB":
            self.ui.textbox_d2.setText(self.ui.textbox_d1.text())
        elif self.ui.combo_fd.currentText() == "MB" and self.ui.combo_td.currentText() == "GB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**-3))
        elif self.ui.combo_fd.currentText() == "MB" and self.ui.combo_td.currentText() == "TB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**-6))
        elif self.ui.combo_fd.currentText() == "GB" and self.ui.combo_td.currentText() == "Bit":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*8*10**9))
        elif self.ui.combo_fd.currentText() == "GB" and self.ui.combo_td.currentText() == "byte":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**9))
        elif self.ui.combo_fd.currentText() == "GB" and self.ui.combo_td.currentText() == "KB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**6))
        elif self.ui.combo_fd.currentText() == "GB" and self.ui.combo_td.currentText() == "MB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**3))
        elif self.ui.combo_fd.currentText() == "GB" and self.ui.combo_td.currentText() == "GB":
            self.ui.textbox_d2.setText(self.ui.textbox_d1.text())
        elif self.ui.combo_fd.currentText() == "GB" and self.ui.combo_td.currentText() == "TB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**-3))
        elif self.ui.combo_fd.currentText() == "TB" and self.ui.combo_td.currentText() == "Bit":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*8*10**12))
        elif self.ui.combo_fd.currentText() == "TB" and self.ui.combo_td.currentText() == "byte":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**12))
        elif self.ui.combo_fd.currentText() == "TB" and self.ui.combo_td.currentText() == "KB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**9))
        elif self.ui.combo_fd.currentText() == "TB" and self.ui.combo_td.currentText() == "MB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**6))
        elif self.ui.combo_fd.currentText() == "TB" and self.ui.combo_td.currentText() == "GB":
            self.ui.textbox_d2.setText(str(float(self.ui.textbox_d1.text())*10**3))
        elif self.ui.combo_fd.currentText() == "TB" and self.ui.combo_td.currentText() == "TB":
            self.ui.textbox_d2.setText(self.ui.textbox_d1.text())

    def message(self):
        msg = QMessageBox()
        msg.setText("Unit Converter")
        msg.setInformativeText("GUI Unit Converter using Pyside6\nThis program was developed by Alireza Kiaeipour\nContact developer: a.kiaipoor@gmail.com\nBuilt in 2021")
        msg.setIcon(QMessageBox.Information)
        msg.exec()   
    def ex(self):
        exit()
        
app = QApplication()
window = Main()
app.exec()