from PyQt6.QtWidgets import *
from PyQt6 import uic
import sys
import re
import math

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('form.ui', self) # Load the .ui file
        for x in range(0, 24):
            exec(f"self.pushButton{x}.clicked.connect(self.buttonClicked)")
    def calc(self):
        x = self.lineEdit.text().replace("÷", "/")
        x = x.replace("²", "**2")
        x = x.replace(",", ".")
        x = x.replace("π", str(math.pi))
        x = x.replace("√", " ** (0.5)")
        try:
            y = eval(x)
        except:
            return "Incorrect formula"
        else:
            return y
    def buttonClicked(self):
        sender = self.sender().text()
        if (True if (re.fullmatch(r"[0-9\-\+\*\,\%\(\)\÷\π\√]", sender)) else False):
            self.lineEdit.setText(self.lineEdit.text() + sender)
        elif (True if (re.match(r"x²", sender)) else False):
            self.lineEdit.setText(self.lineEdit.text() + "²")
        elif (True if (re.match(r"[\=]", sender)) else False):
            self.lineEdit.setText(str(self.calc()))
        elif (True if (re.match(r"⌫", sender)) else False):
            self.lineEdit.setText(self.lineEdit.text()[:-1])
        elif (True if (re.match(r"CE", sender)) else False):
            self.lineEdit.setText("")
 
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
