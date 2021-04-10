from PyQt5 import QtCore, QtGui, QtWidgets
from db import *
    

class check(QtCore.QThread):
   mysignal = QtCore.pyqtSignal(str)
   
   def add_di(self,dish):
      add_dish(dish,self.mysignal)
      
   def add_de(self,desert):
      add_desert(desert,self.mysignal)

   def generation(self):
      get_dish(self.mysignal)

