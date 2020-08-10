from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
import time
import sys
from Ui_chamado import *


class Support_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
    
    # def button_handle(self):
    #     # self.pushButton.clicked.connect(self.enviaChamado)
    
    # def enviaChamado(self):
    #     # chamado.hide()
        
    #     # print(time, linha, nome, status, work)
    #     #lib.requestSupport(time, linha, nome, work)