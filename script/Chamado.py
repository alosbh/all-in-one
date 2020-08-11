from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QThread
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
        self.status = 0
        self.thread = CountSeconds()
        

        motivos = ["Descrição de problema 1", "Descrição de problema 2", "Descrição de problema 3", "Descrição de problema 4"]
        for motivo in motivos:
            self.lista_motivos.addItem(motivo)

        self.button_handle()

    def Show(self):

        self.Support_QtWindow.show()
    
    def button_handle(self):
        logger.error("setei os botoes")
        self.btn_solicitar.clicked.connect(self.enviaChamado)
    
    
    def enviaChamado(self):
   
        self.btn_solicitar.setVisible(False)
        self.btn_finalizar.setVisible(True)
        self.btn_cancelar.setVisible(True)
        self.lbl_status.setText("Aguarde...")

        self.motivo = self.lista_motivos.currentText()
        self.horario = str(datetime.now().time())[0:5]
        self.time = "Engenharia"
        logger.error("enviei chamado")
        logger.error(self.posto)
        logger.error(self.time)
        logger.error(self.motivo)
        logger.error(self.horario)
        self.status = 1
        self.thread.startThread(self)
        
    

    def finaliza(self):
        self.btn_solicitar.setVisible(True)
        self.btn_finalizar.setVisible(False)
        self.btn_cancelar.setVisible(False)
        self.lbl_status.setText("Não solicitado")
        self.status = 0


class CountSeconds(QThread):
 

    def run(self):

        contadorThread = 0
        
        while(self.janelaSuporte.status == 1):

           
            logger.error("Status janela:"+str(self.janelaSuporte.status))

            self.seconds = datetime.now() - self.timeinit
            logger.error(str(datetime.now()))
            logger.error(str(self.seconds))
            self.janelaSuporte.lbl_tempo.setText(str(self.seconds))
            

            

            
            
            time.sleep(1)



    def startThread(self,janelaSuporte):
        self.timeinit = datetime.now()
        self.seconds = 0;
        
        self.janelaSuporte = janelaSuporte
        logger.error("startei a thread")
        
        self.start()