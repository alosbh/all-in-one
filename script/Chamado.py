from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QThread
import time
import sys
from Ui_chamado import *
from datetime import datetime
import logging
import requests
import json

global logger
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)

class Support_Window(QtWidgets.QMainWindow, Ui_MainWindow):

    

    def __init__(self, *args, **kwargs):

        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.Support_QtWindow = QtWidgets.QMainWindow()
        self.setupUi(self.Support_QtWindow)
        self.Support_QtWindow.move((1366 - 353)/2, (768 - 240)/2)
        logger.error("instanciei a classe")
        self.posto = ""
        self.time = "Engenharia"
        self.motivo = ""
        self.horario = ""
        self.linha = "Linha Rodando"
        self.status = 0
        self.thread = CountSeconds()
        postBody = {}
        

        motivos = ["Descrição de problema 1", "Descrição de problema 2", "Descrição de problema 3", "Descrição de problema 4"]
        for motivo in motivos:
            self.lista_motivos.addItem(motivo)

        self.button_handle()

    def Show(self):

        self.Support_QtWindow.show()
    
    def button_handle(self):
        logger.error("setei os botoes")
        self.btn_solicitar.clicked.connect(self.enviaChamado)
        self.btn_concluir.clicked.connect(self.finaliza)
        self.btn_cancelar.clicked.connect(self.finaliza)
        self.rd_btn_engenharia.clicked.connect(self.setEngenharia)
        self.rd_btn_manufatura.clicked.connect(self.setManufatura)
        self.rd_btn_qualidade.clicked.connect(self.setQualidade)
        self.rd_btn_ic.clicked.connect(self.setIC)
        self.rd_btn_rodando.clicked.connect(self.setLinhaRodando)
        self.rd_btn_parada.clicked.connect(self.setLinhaParada)

        
    
    
    def enviaChamado(self):
   
        self.btn_solicitar.setVisible(False)
        self.btn_concluir.setVisible(True)
        self.btn_cancelar.setVisible(True)
        self.lbl_status.setText("Aguarde...")

        self.motivo = self.lista_motivos.currentText()
        self.horario = str(datetime.now().time())[0:5]




        headers = {'content-type': 'application/json'}
        url = 'http://BRBELRASPBUSTERDEV:3000/reloginho'
        postBody = {'workstation': self.posto,'risk': self.linha, 'calltime': self.horario, 'description':self.motivo}

        r = requests.post(url, data=json.dumps(postBody), headers=headers)
        

        logger.error(r.text)
        logger.error("enviei chamado")
        logger.error(self.posto)
        logger.error(self.time)
        logger.error(self.motivo)
        logger.error(self.horario)
        self.status = 1
        self.thread.startThread(self)
        
    

    def finaliza(self):
        self.btn_solicitar.setVisible(True)
        self.btn_concluir.setVisible(False)
        self.btn_cancelar.setVisible(False)
        self.lbl_status.setText("Não solicitado")
        self.status = 0
        self.lbl_tempo.setText("0:00:00")


    def setEngenharia(self):
        self.time = "Engenharia"
    def setManufatura(self):
        self.time = "Manufatura"
    def setIC(self):
        self.time = "IC"
    def setQualidade(self):
        self.time = "Qualidade"
    def setEngenharia(self):
        self.time = "Engenharia"
    def setEngenharia(self):
        self.time = "Engenharia"
    def setLinhaRodando(self):
        self.linha = "Linha Rodando"
    def setLinhaParada(self):
        self.linha = "Linha Parada"
        


class CountSeconds(QThread):
 

    def run(self):

        contadorThread = 0
        
        while(self.janelaSuporte.status == 1):

            self.seconds = datetime.now() - self.timeinit
            
            self.janelaSuporte.lbl_tempo.setText(str(self.seconds)[0:7])

            time.sleep(1)

    def startThread(self,janelaSuporte):
        self.timeinit = datetime.now()
        self.seconds = 0;
        
        self.janelaSuporte = janelaSuporte
        logger.error("startei a thread")
        
        self.start()