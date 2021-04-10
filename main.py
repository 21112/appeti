import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from interface import *
from db import *
from logik import *

class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.getting)
        self.ui.pushButton_1.clicked.connect(self.add_dish)
        self.ui.pushButton_2.clicked.connect(self.add_desert)
        self.l = self.ui.lineEdit
        self.l2 = self.ui.lineEdit_2
        self.check_db = check()
        self.check_db.mysignal.connect(self.signal_handler)

    def signal_handler(self,value):
        QtWidgets.QMessageBox.about(self,'Message', value)

    def getting(self):
        self.check_db.generation()

    def add_dish(self):
        self.dish = self.l.text()
        self.check_db.add_di(self.dish)

    def add_desert(self):
        self.desert = self.l2.text()
        self.check_db.add_de(self.desert)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)      
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_()) 

