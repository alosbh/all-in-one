from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QThread
import time
import sys
from Ui_chamado import *
from datetime import datetime,timedelta
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
        self.index = 0
        self.time = "Engenharia"
        self.motivos = []
        self.horario = ""
        self.linha = "Rodando"
        self.status = 0
        self.thread = CountSeconds()
        self.watchthread = WatchStatus()
        postBody = {}
        

        

        
        

        

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
        self.rd_btn_rodando.clicked.connect(self.setLinhaParada)
        self.rd_btn_parada.clicked.connect(self.setLinhaRodando)

    def populateMotivos(self):

        motivos1 =["Escolha o Motivo","FI sem assinatura","Problemas All In One (posto ao lado)","Falha CNCS (API)","Micro NFS indisponivel","Porta NFS indisponivel","Reprovação de terminal","Terminais não abrem tela do Cliente","Todos terminais com falha de gravação","Troca de Etiqueta / Ribbon","Um terminal com falha de gravação","Micro Travado / Reiniciando","Outro"]
        motivos2=motivos1
        motivos3=["Escolha o Motivo","FI sem assinatura","Problemas All In One (posto ao lado)","Falha Nascimento do terminal","Jabil Test não abre","Lentidão no Jabil Test","Reprovação de terminal","Terminais não abrem tela do Cliente","Todos Genisys Offline","Todos terminais com falha de gravação","Um Genisys Offline","Um terminal com falha de gravação","Micro Travado / Reiniciando","Outro"]
        motivos4=["Escolha o Motivo","FI sem assinatura","Problemas All In One (posto ao lado)","Falha Nascimento do terminal","Jabil Test não abre","Lentidão no Jabil Test","Reprovação de terminal","Terminais não abrem tela do Cliente","Falha no SAFF Extractor","Micro Travado / Reiniciando","Outro"]
        motivos5=["Escolha o Motivo","FI sem assinatura","Problemas All In One (posto ao lado)","Outro"]
        motivos6=["Escolha o Motivo","FI sem assinatura","Problemas All In One (posto ao lado)","Jabil Test não abre","Lentidão no Jabil Test","Troca de Etiqueta / Ribbon","Micro Travado / Reiniciando","Um terminal com falha agregação","Todos Terminais com falha de agregação","Falha Pick To Light","Falha na Rotuladora","Etiqueta não gerada - Zebra","Regerar Etiqueta","Outro"]
        motivos7=["Escolha o Motivo","FI sem assinatura","Problemas All In One (posto ao lado)","Jabil Test não abre","Lentidão no Jabil Test","Reprovação de terminal","Troca de Etiqueta / Ribbon","Micro Travado / Reiniciando","Falha na Rotuladora","Regerar Etiqueta","Etiqueta trocada / Ausente","Reteste camera","Falha jiga / sensor","Outro"]
        motivos8=["Escolha o Motivo","FI sem assinatura","Problemas All In One (posto ao lado)","Jabil Test não abre","Lentidão no Jabil Test","Micro Travado / Reiniciando","Falha no braço da balança","Camera Balança não lê","Uma caixa com peso fora do especificado","Todas caixas - peso fora do especificado","Um terminal não embala","Todos terminais não embalam","MES não abre","Caixa no BIN","Outro"]
        motivos9=["Escolha o Motivo","FI sem assinatura","Problemas All In One (posto ao lado)","Jabil Test não abre","Micro Travado / Reiniciando","Problema no Relatorio de Pallet / BOX","Duvidas Script de liberação de Pallet","Falha Script de liberação do Pallet","Outro"]

        if(self.index==1):
            self.motivos = motivos1
        elif(self.index==2):
            self.motivos=motivos2
        elif(self.index==3):
            self.motivos=motivos3
        elif(self.index==4):
            self.motivos=motivos4
        elif(self.index==5):
            self.motivos=motivos5
        elif(self.index==6):
            self.motivos=motivos6
        elif(self.index==7):
            self.motivos=motivos7
        elif(self.index==8):
            self.motivos=motivos8
        elif(self.index==9):
            self.motivos=motivos9
        else:
            self.motivos=motivos5

        for motivo in self.motivos:
            self.lista_motivos.addItem(motivo)


    
    
    def enviaChamado(self):
   
        self.btn_solicitar.setVisible(False)
        self.btn_concluir.setVisible(True)
        self.btn_cancelar.setVisible(True)
        self.lbl_status.setText("Aguarde...")

        self.motivo = self.lista_motivos.currentText()
        horaagora = datetime.now() - timedelta(hours=3, minutes=0)
        self.horario = str(horaagora.time())[0:5]



        
        headers = {'content-type': 'application/json'}
        url = 'http://10.57.38.132/receberchamado'
        
        postBody = {'id':'4','workstation': self.posto,'risk': self.linha, 'calltime': self.horario, 'description':self.motivo}

        r = requests.post(url, data=json.dumps(postBody), headers=headers)

       

        logger.error("enviei chamado")

        logger.error(r.text)
      
        
        logger.error(self.posto)
        logger.error(self.time)
        logger.error(self.motivo)
        logger.error(self.horario)
        logger.error("index eh")
        logger.error(self.index)
        self.status = 1
        self.thread.startThread(self)
        self.watchthread.startThread(self)
        
    

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
        self.linha = "Rodando"
    def setLinhaParada(self):
        self.linha = "Parada"
        


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


class WatchStatus(QThread):
 

    def run(self):

        
        
        while(self.janelaSuporte.status == 1):

            getrequest = requests.get(self.url)
            if(getrequest.text == "Confirmed"):
                self.lbl_status.setText("Chamado confirmado")
            elif(getrequest.text == "onGoing"):
                self.lbl_status.setText("Chamado iniciado")
            elif(getrequest.text == "Done"):
                self.lbl_status.setText("Chamado Finalizado")


           


            time.sleep(5)

    def startThread(self,janelaSuporte):
              
        
        self.url = "http://brbelraspbusterdev:3000/status"
        
        
        self.janelaSuporte = janelaSuporte
        
        
        self.start()
        

