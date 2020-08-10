from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
import time
import sys
from Ui_chamado import *
from datetime import datetime
import logging
global logger
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)

class Support_Window(QtWidgets.QMainWindow, Ui_MainWindow):

    

    def __init__(self, *args, **kwargs):

        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.Support_QtWindow = QtWidgets.QMainWindow()
        self.setupUi(self.Support_QtWindow)
        self.Support_QtWindow.move((1366 - 511)/2, (768 - 240)/2)
        logger.error("instanciei a classe")
        self.posto = ""
        self.time = ""
        self.motivo = ""
        self.horario = ""

        motivos = ["Descrição de problema 1", "Descrição de problema 2", "Descrição de problema 3", "Descrição de problema 4"]
        for motivo in motivos:
            self.lista_motivos.addItem(motivo)

        self.button_handle()

    def Show(self):

        self.Support_QtWindow.show()
    
    def button_handle(self):
        logger.error("enviei chamado")
        self.btn_solicitar.clicked.connect(self.enviaChamado)
    
    def enviaChamado(self):
    #     # chamado.hide()
        self.btn_solicitar.setVisible(False)
        self.btn_finalizar.setVisible(True)
        self.btn_cancelar.setVisible(True)

        self.motivo = self.lista_motivos.currentText()
        self.horario = datetime.now().time()
        logger.error("enviei chamado")
        logger.error(self.posto,self.time, self.motivo, self.horario)
        print(self.posto,self.time, self.motivo, self.horario)
    #     #lib.requestSupport(time, linha, nome, work)