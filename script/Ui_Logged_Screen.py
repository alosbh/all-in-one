# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\\brbelm0te01\Jabiltest\AIO\26- Leitura Crachá GUI V26\uis\logged.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from Hover import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebKitWidgets import *
import sip
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKit import *
from PyQt5.QtNetwork import *
from PyQt5.QtWebKit import QWebSettings

#from QtWebEngine import *
# from PyQt5.QtWebEngineWidgets import QWebEnginePage
# from PyQt5.QtWebEngineWidgets import QWebEngineView

class Ui_Logged_Screen(object):
    def setupUi(self, Logged):
        Logged.setObjectName("Logged")
        Logged.resize(1366, 768)
        Logged.setStyleSheet("background: transparent;")
        self.centralwidget = QtWidgets.QWidget(Logged)
        self.centralwidget.setStyleSheet("background: transparent;\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.background.setFont(font)
        self.background.setStyleSheet("background: transparent;\n"
"background-color: rgb(236, 240, 245);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.posto_id = QtWidgets.QLabel(self.centralwidget)
        self.posto_id.setGeometry(QtCore.QRect(76, 260, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.posto_id.setFont(font)
        self.posto_id.setStyleSheet("background: transparent;\n"
"background-color: transparent;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.posto_id.setAlignment(QtCore.Qt.AlignCenter)
        self.posto_id.setObjectName("posto_id")
        self.operador_id = QtWidgets.QLabel(self.centralwidget)
        self.operador_id.setGeometry(QtCore.QRect(1, 240, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.operador_id.setFont(font)
        self.operador_id.setStyleSheet("background: transparent;\n"
"background-color: transparent;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.operador_id.setAlignment(QtCore.Qt.AlignCenter)
        self.operador_id.setObjectName("operador_id")
        self.lat_preto = QtWidgets.QLabel(self.centralwidget)
        self.lat_preto.setGeometry(QtCore.QRect(0, 0, 361, 768))
        self.lat_preto.setStyleSheet("background: transparent;\n"
"background-color: rgb(34, 45, 50);\n"
"border-style: solid;\n"
"border-color: transparent;")
        self.lat_preto.setText("")
        self.lat_preto.setAlignment(QtCore.Qt.AlignCenter)
        self.lat_preto.setObjectName("lat_preto")
        self.sup_verde = QtWidgets.QLabel(self.centralwidget)
        self.sup_verde.setGeometry(QtCore.QRect(0, 0, 1366, 51))
        self.sup_verde.setStyleSheet("background: transparent;\n"
"background-color: rgb(0, 166, 90);\n"
"border-style: solid;\n"
"border-color: transparent;")
        self.sup_verde.setText("")
        self.sup_verde.setAlignment(QtCore.Qt.AlignCenter)
        self.sup_verde.setObjectName("sup_verde")
        self.foto = QtWidgets.QLabel(self.centralwidget)
        self.foto.setGeometry(QtCore.QRect(137, 129, 90, 90))
        self.foto.setStyleSheet("background-color: white;\n"
"border-radius: 45px;")
        self.foto.setText("")
        self.foto.setObjectName("foto")
        self.aro_branco = QtWidgets.QLabel(self.centralwidget)
        self.aro_branco.setGeometry(QtCore.QRect(138, 130, 86, 86))
        self.aro_branco.setStyleSheet("border-radius: 43px;\n"
"background-color: white;\n"
"background: url(:/Imgs/Webp.net-resizeimage.jpg);")
        self.aro_branco.setText("")
        self.aro_branco.setObjectName("aro_branco")
        self.sup_branco = QtWidgets.QLabel(self.centralwidget)
        self.sup_branco.setGeometry(QtCore.QRect(0, 0, 361, 51))
        self.sup_branco.setStyleSheet("background-color: rgb(236, 240, 245);\n"
"")
        self.sup_branco.setText("")
        self.sup_branco.setObjectName("sup_branco")
        self.jabil = QtWidgets.QPushButton(self.centralwidget)
        self.jabil.setGeometry(QtCore.QRect(1, 1, 360, 50))
        self.jabil.setStyleSheet("border-image: url(:/Imgs/LogoJabil.png);")
        self.jabil.setText("")
        self.jabil.setObjectName("jabil")
        self.aio = QtWidgets.QLabel(self.centralwidget)
        self.aio.setGeometry(QtCore.QRect(85, 52, 280, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.aio.setFont(font)
        self.aio.setStyleSheet("background-color: rgb(30, 40, 44);\n"
"color: rgb(236, 240, 245);")
        self.aio.setAlignment(QtCore.Qt.AlignCenter)
        self.aio.setObjectName("aio")
        self.lat_verde = QtWidgets.QLabel(self.centralwidget)
        self.lat_verde.setGeometry(QtCore.QRect(0, 52, 6, 71))
        self.lat_verde.setStyleSheet("background-color: rgb(0, 166, 90);")
        self.lat_verde.setText("")
        self.lat_verde.setObjectName("lat_verde")
        self.web = QWebView(self.centralwidget)
        #self.web = QWebEngineView(self.centralwidget)
        self.web.setGeometry(QtCore.QRect(361, 51, 1011, 721))
        self.web.setObjectName("web")
        self.webSettings = self.web.settings()
        
        self.LPA_button = QtWidgets.QPushButton(self.centralwidget)
        self.LPA_button.setGeometry(QtCore.QRect(0, 300, 361, 56))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LPA_button.setFont(font)
        self.LPA_button.setStyleSheet("\n"
"background-color: rgb(30, 40, 44);\n"
"color: rgb(236, 240, 245);\n"
"\n"
"\n"
"")
        self.LPA_button.setAutoDefault(False)
        self.LPA_button.setDefault(True)
        self.LPA_button.setFlat(True)
        self.LPA_button.setObjectName("LPA_button")

        self.lat_verde_2 = QtWidgets.QLabel(self.centralwidget)
        self.lat_verde_2.setGeometry(QtCore.QRect(0, 300, 6, 56))
        self.lat_verde_2.setStyleSheet("background-color: rgb(30, 40, 44);")
        self.lat_verde_2.setText("")
        self.lat_verde_2.setObjectName("lat_verde_2")




        self.FI_button = QtWidgets.QPushButton(self.centralwidget)
        self.FI_button.setGeometry(QtCore.QRect(0, 356, 361, 56))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.FI_button.setFont(font)
        self.FI_button.setStyleSheet("background-color:  rgb(30, 40, 44);\n"
"color: rgb(236, 240, 245);")
        self.FI_button.setAutoDefault(False)
        self.FI_button.setDefault(True)
        self.FI_button.setFlat(True)
        self.FI_button.setObjectName("FI_button")
        
        self.lat_verde_3 = QtWidgets.QLabel(self.centralwidget)
        self.lat_verde_3.setGeometry(QtCore.QRect(0, 356, 6, 56))
        self.lat_verde_3.setStyleSheet("background-color: rgb(30, 40, 44);")
        self.lat_verde_3.setText("")
        self.lat_verde_3.setObjectName("lat_verde_3")
        
        
        self.BI_button = QtWidgets.QPushButton(self.centralwidget)
        self.BI_button.setGeometry(QtCore.QRect(0, 412, 361, 56))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BI_button.setFont(font)
        self.BI_button.setStyleSheet("background-color: rgb(30, 40, 44);\n"
"color: rgb(236, 240, 245);")
        self.BI_button.setAutoDefault(False)
        self.BI_button.setDefault(True)
        self.BI_button.setFlat(True)
        self.BI_button.setObjectName("BI_button")
        
        self.lat_verde_4 = QtWidgets.QLabel(self.centralwidget)
        self.lat_verde_4.setGeometry(QtCore.QRect(0, 412, 6, 56))
        self.lat_verde_4.setStyleSheet("background-color:  rgb(30, 40, 44);")
        self.lat_verde_4.setText("")
        self.lat_verde_4.setObjectName("lat_verde_4")
        
        
        
        self.jiga_button = QtWidgets.QPushButton(self.centralwidget)
        self.jiga_button.setGeometry(QtCore.QRect(0, 468, 361, 56))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.jiga_button.setFont(font)
        self.jiga_button.setStyleSheet("background-color: rgb(30, 40, 44);\n"
"color: rgb(236, 240, 245);")
        self.jiga_button.setAutoDefault(False)
        self.jiga_button.setDefault(True)
        self.jiga_button.setFlat(True)
        self.jiga_button.setObjectName("jiga_button")

        self.lat_verde_5 = QtWidgets.QLabel(self.centralwidget)
        self.lat_verde_5.setGeometry(QtCore.QRect(0, 468, 6, 56))
        self.lat_verde_5.setStyleSheet("background-color:  rgb(30, 40, 44);")
        self.lat_verde_5.setText("")
        self.lat_verde_5.setObjectName("lat_verde_5")


        self.custom_button = QtWidgets.QPushButton(self.centralwidget)
        self.custom_button.setGeometry(QtCore.QRect(0, 524, 361, 56))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.custom_button.setFont(font)
        self.custom_button.setStyleSheet("background-color: rgb(30, 40, 44);\n"
"color: rgb(236, 240, 245);")
        self.custom_button.setAutoDefault(False)
        self.custom_button.setDefault(True)
        self.custom_button.setFlat(True)
        self.custom_button.setObjectName("custom_button")

        self.lat_verde_6 = QtWidgets.QLabel(self.centralwidget)
        self.lat_verde_6.setGeometry(QtCore.QRect(0, 524, 6, 56))
        self.lat_verde_6.setStyleSheet("background-color:  rgb(30, 40, 44);")
        self.lat_verde_6.setText("")
        self.lat_verde_6.setObjectName("lat_verde_6")


        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 580, 361, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("background: url( :/Imgs/Yield.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("background: url(:/Imgs/boasideia.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("background: url( :/Imgs/Produtividade.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("background: url(:/Imgs/jabilcoin.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 670, 361, 91))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.yield1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.yield1.setFont(font)
        self.yield1.setStyleSheet("color: white;\n"
"")
        self.yield1.setAlignment(QtCore.Qt.AlignCenter)
        self.yield1.setObjectName("yield")
        self.gridLayout_2.addWidget(self.yield1, 0, 0, 1, 1)
        self.boasideias = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.boasideias.setFont(font)
        self.boasideias.setStyleSheet("color: white;\n"
"")
        self.boasideias.setAlignment(QtCore.Qt.AlignCenter)
        self.boasideias.setObjectName("boasideias")
        self.gridLayout_2.addWidget(self.boasideias, 0, 2, 1, 1)
        self.produtividade = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.produtividade.setFont(font)
        self.produtividade.setStyleSheet("color: white;\n"
"")
        self.produtividade.setAlignment(QtCore.Qt.AlignCenter)
        self.produtividade.setObjectName("produtividade")
        self.gridLayout_2.addWidget(self.produtividade, 0, 1, 1, 1)
        self.jabilcoins = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.jabilcoins.setFont(font)
        self.jabilcoins.setStyleSheet("color: white;\n"
"")
        self.jabilcoins.setAlignment(QtCore.Qt.AlignCenter)
        self.jabilcoins.setObjectName("jabilcoins")
        self.gridLayout_2.addWidget(self.jabilcoins, 0, 3, 1, 1)
        


        self.mainthread_icon = QtWidgets.QLabel(self.centralwidget)
        self.mainthread_icon.setEnabled(True)
        self.mainthread_icon.setGeometry(QtCore.QRect(15, 60, 24, 24))
        self.mainthread_icon.setAutoFillBackground(True)
        self.mainthread_icon.setStyleSheet("background-color: green;\n"
" border-radius: 12px;\n"
"background-color:rgb(0, 200, 50);\n"
"")
        self.mainthread_icon.setText("")
        self.mainthread_icon.setObjectName("mainthread_icon")
        self.logthread_icon = QtWidgets.QLabel(self.centralwidget)
        self.logthread_icon.setEnabled(True)
        self.logthread_icon.setGeometry(QtCore.QRect(15, 92, 24, 24))
        self.logthread_icon.setAutoFillBackground(True)
        self.logthread_icon.setStyleSheet("background-color: green;\n"
" border-radius: 12px;\n"
"background-color:rgb(0, 200, 50);\n"
"")
        self.logthread_icon.setText("")
        self.logthread_icon.setObjectName("logthread_icon")
        self.mainthread_icon_off = QtWidgets.QLabel(self.centralwidget)
        self.mainthread_icon_off.setEnabled(True)
        self.mainthread_icon_off.setGeometry(QtCore.QRect(15, 60, 24, 24))
        self.mainthread_icon_off.setAutoFillBackground(True)
        self.mainthread_icon_off.setStyleSheet("background-color: green;\n"
" border-radius: 12px;\n"
"background-color:rgb(150, 150, 150);\n"
"")
        self.mainthread_icon_off.setText("")
        self.mainthread_icon_off.setObjectName("mainthread_icon_off")
        self.logthread_icon_off = QtWidgets.QLabel(self.centralwidget)
        self.logthread_icon_off.setEnabled(True)
        self.logthread_icon_off.setGeometry(QtCore.QRect(15, 92, 24, 24))
        self.logthread_icon_off.setAutoFillBackground(True)
        self.logthread_icon_off.setStyleSheet("background-color: green;\n"
" border-radius: 12px;\n"
"background-color:rgb(150, 150, 150);\n"
"")
        self.logthread_icon_off.setText("")
        self.logthread_icon_off.setObjectName("logthread_icon_off")

        self.ReadIcon = QtWidgets.QLabel(self.centralwidget)
        self.ReadIcon.setGeometry(QtCore.QRect(50, 54, 32, 32))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ReadIcon.setFont(font)
        self.ReadIcon.setEnabled(True)
        self.ReadIcon.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.ReadIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.ReadIcon.setObjectName("ReadIcon")
        self.LogIcon = QtWidgets.QLabel(self.centralwidget)
        self.LogIcon.setGeometry(QtCore.QRect(50, 86, 32, 32))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LogIcon.setFont(font)
        self.LogIcon.setEnabled(True)
        self.LogIcon.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.LogIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.LogIcon.setObjectName("LogIcon")


        self.web_2 = QtWidgets.QLabel(self.centralwidget)
        self.web_2.setGeometry(QtCore.QRect(361, 0, 1011, 728))
        self.web_2.setStyleSheet("border-image: url(:/Imgs/LINK2500-6.png);")
        self.web_2.setText("")
        self.web_2.setObjectName("web_2")
        self.web_2.setVisible(False)


        self.homepage = QtWidgets.QLabel(self.centralwidget)
        self.homepage.setGeometry(QtCore.QRect(361, 51, 1011, 728))
        self.homepage.setStyleSheet("border-image: url(:/Imgs/main.png);")
        self.homepage.setText("")
        self.homepage.setObjectName("homepage")
        self.homepage.setVisible(True)




        self.firight = QtWidgets.QPushButton(self.centralwidget)
        self.firight.setGeometry(QtCore.QRect(1280, 690, 64, 64))
        self.firight.setStyleSheet("border-radius: 43px;\n"
"background-color: white;\n"
"background: url(:/Imgs/rightarrow.png);")
        self.firight.setText("")
        self.firight.setObjectName("firight")
        self.firight.setVisible(False)
        self.fileft = QtWidgets.QPushButton(self.centralwidget)
        self.fileft.setGeometry(QtCore.QRect(1200, 690, 64, 64))
        self.fileft.setStyleSheet("border-radius: 43px;\n"
"background-color: white;\n"
"background: url(:/Imgs/leftarrow.png);")
        self.fileft.setText("")
        self.fileft.setObjectName("fileft")
        self.fileft.setVisible(False)


     


        self.Reset_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Reset_Button.setGeometry(QtCore.QRect(1190, 700, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        self.Reset_Button.setFont(font)
        self.Reset_Button.setStyleSheet("background-color:  rgb(5, 80, 135);\n"
"color: rgb(236, 240, 245);\n"
"border-radius:10px")
        self.Reset_Button.setAutoDefault(False)
        self.Reset_Button.setDefault(True)
        self.Reset_Button.setFlat(True)
        self.Reset_Button.setObjectName("Reset_Button")
        self.Reset_Button.setVisible(False)



        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(880, 310, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet("")
        self.Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.Titulo.setObjectName("Titulo")
        self.ReleaseNotes = QtWidgets.QLabel(self.centralwidget)
        self.ReleaseNotes.setGeometry(QtCore.QRect(880, 360, 451, 371))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ReleaseNotes.setFont(font)
        self.ReleaseNotes.setStyleSheet("")
        self.ReleaseNotes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ReleaseNotes.setWordWrap(True)
        self.ReleaseNotes.setObjectName("ReleaseNotes")
        self.LPA_Label = QtWidgets.QLabel(self.centralwidget)
        self.LPA_Label.setGeometry(QtCore.QRect(390, 190, 151, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LPA_Label.setFont(font)
        self.LPA_Label.setStyleSheet("")
        self.LPA_Label.setTextFormat(QtCore.Qt.AutoText)
        self.LPA_Label.setScaledContents(True)
        self.LPA_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.LPA_Label.setWordWrap(True)
        self.LPA_Label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.LPA_Label.setObjectName("LPA_Label")
        self.FI_Label = QtWidgets.QLabel(self.centralwidget)
        self.FI_Label.setGeometry(QtCore.QRect(575, 285, 151, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.FI_Label.setFont(font)
        self.FI_Label.setStyleSheet("")
        self.FI_Label.setTextFormat(QtCore.Qt.AutoText)
        self.FI_Label.setScaledContents(True)
        self.FI_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.FI_Label.setWordWrap(True)
        self.FI_Label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.FI_Label.setObjectName("FI_Label")
        self.BI_Label = QtWidgets.QLabel(self.centralwidget)
        self.BI_Label.setGeometry(QtCore.QRect(580, 410, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BI_Label.setFont(font)
        self.BI_Label.setStyleSheet("")
        self.BI_Label.setTextFormat(QtCore.Qt.AutoText)
        self.BI_Label.setScaledContents(True)
        self.BI_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.BI_Label.setWordWrap(True)
        self.BI_Label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.BI_Label.setObjectName("BI_Label")
        self.SCTC_Label = QtWidgets.QLabel(self.centralwidget)
        self.SCTC_Label.setGeometry(QtCore.QRect(580, 510, 151, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SCTC_Label.setFont(font)
        self.SCTC_Label.setStyleSheet("")
        self.SCTC_Label.setTextFormat(QtCore.Qt.AutoText)
        self.SCTC_Label.setScaledContents(True)
        self.SCTC_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.SCTC_Label.setWordWrap(True)
        self.SCTC_Label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.SCTC_Label.setObjectName("SCTC_Label")
        self.Custom_Label = QtWidgets.QLabel(self.centralwidget)
        self.Custom_Label.setGeometry(QtCore.QRect(390, 600, 151, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Custom_Label.setFont(font)
        self.Custom_Label.setStyleSheet("")
        self.Custom_Label.setTextFormat(QtCore.Qt.AutoText)
        self.Custom_Label.setScaledContents(True)
        self.Custom_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Custom_Label.setWordWrap(True)
        self.Custom_Label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Custom_Label.setObjectName("Custom_Label")

        self.botao5s = QtWidgets.QWidget(self.centralwidget)
        
        # self.tag5s = QtWidgets.QPushButton(self.centralwidget)


        self.tag5s = Tag5s(self.centralwidget)
        self.tag5s.setGeometry(QtCore.QRect(309, 246, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tag5s.setFont(font)
        self.tag5s.setStyleSheet("background-color:rgba(255,255,255,0.01);color: rgb(50, 40, 50);")
        self.tag5s.setAutoDefault(False)
        self.tag5s.setDefault(True)
        self.tag5s.setFlat(True)
        self.tag5s.setObjectName("tag5s")


        self.botao5s.label = Botao()
        self.botao5s.graphicsview = QtWidgets.QGraphicsView()
        self.botao5s.graphicsview.setGeometry(0,50,350,280)
        self.botao5s.graphicsview.setStyleSheet("border-width: 0px; border-style: solid;background:transparent")
        self.botao5s.scene = QtWidgets.QGraphicsScene(self.botao5s.graphicsview)
        self.botao5s.scene.setSceneRect(0,50,350,280)
        
        self.botao5s.graphicsview.setScene(self.botao5s.scene)

        
        self.botao5s.proxy = QtWidgets.QGraphicsProxyWidget()
        self.botao5s.proxy.setWidget(self.botao5s.label)
        # self.botao5s.proxy2 = QtWidgets.QGraphicsProxyWidget()
        # self.botao5s.proxy2.setWidget(self.botao5s.tag)

        
        self.botao5s.proxy.setGeometry(QtCore.QRectF(278,265,75,71))
        # self.botao5s.proxy2.setGeometry(QtCore.QRectF(270,277,30,30))
        self.botao5s.proxy.setTransformOriginPoint(self.botao5s.proxy.boundingRect().center())
        # self.botao5s.proxy2.setTransformOriginPoint(self.botao5s.proxy2.boundingRect().center())
        
        self.botao5s.scene.addItem(self.botao5s.proxy)
        # self.botao5s.scene.addItem(self.botao5s.proxy2)

        self.botao5s.lay = QtWidgets.QVBoxLayout(self.botao5s)
        self.botao5s.lay.addWidget(self.botao5s.graphicsview)

        self.botao5s.thread = RotateThread()
        
        self.botao5s.thread.startThread(self.botao5s.proxy,self.botao5s.label,self.tag5s)

        


        
        
        self.previous5s = QtWidgets.QPushButton(self.centralwidget)
        self.previous5s.setGeometry(QtCore.QRect(395, 10, 23, 23))
        self.previous5s.setStyleSheet("image: url(:/Imgs/leftarrow.png);\n"
"border:10px;")
        self.previous5s.setText("")
        self.previous5s.setObjectName("previous5s")
        self.next5s = QtWidgets.QPushButton(self.centralwidget)
        self.next5s.setGeometry(QtCore.QRect(492, 10, 23, 23))
        self.next5s.setStyleSheet("image: url(:/Imgs/rightarrow.png);\n"
"border:10px;")
        self.next5s.setText("")
        self.next5s.setObjectName("next5s")
        self.pagtual = QtWidgets.QLabel(self.centralwidget)
        self.pagtual.setGeometry(QtCore.QRect(430, 7, 30, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pagtual.setFont(font)
        self.pagtual.setToolTipDuration(-4)
        self.pagtual.setAutoFillBackground(False)
        self.pagtual.setStyleSheet("background-color:transparent;")
        self.pagtual.setObjectName("pagtual")
        self.pagtotal = QtWidgets.QLabel(self.centralwidget)
        self.pagtotal.setGeometry(QtCore.QRect(465, 7, 30, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pagtotal.setFont(font)
        self.pagtotal.setAutoFillBackground(False)
        self.pagtotal.setStyleSheet("background-color:transparent;")
        self.pagtotal.setObjectName("pagtotal")
        self.barra = QtWidgets.QLabel(self.centralwidget)
        self.barra.setGeometry(QtCore.QRect(450, 7, 30, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.barra.setFont(font)
        self.barra.setAutoFillBackground(False)
        self.barra.setStyleSheet("background-color:transparent;")
        self.barra.setObjectName("barra")
        
        self.pagtotal.setVisible(False)
        self.pagtual.setVisible(False)
        self.barra.setVisible(False)
        self.previous5s.setVisible(False)
        self.next5s.setVisible(False)
        

      



        self.background.raise_()
        self.lat_preto.raise_()
        self.posto_id.raise_()
        self.operador_id.raise_()
        self.sup_verde.raise_()
        self.foto.raise_()
        self.aro_branco.raise_()
        self.sup_branco.raise_()
        
        self.aio.raise_()
        self.lat_verde.raise_()
        self.web.raise_()
        self.LPA_button.raise_()
        self.lat_verde_2.raise_()
        self.FI_button.raise_()        
        self.lat_verde_3.raise_()
        self.BI_button.raise_()
        self.lat_verde_4.raise_()
        self.jiga_button.raise_()
        self.lat_verde_5.raise_()
        self.custom_button.raise_()
        self.lat_verde_6.raise_()
        self.gridLayoutWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        
        self.mainthread_icon_off.raise_()
        self.logthread_icon_off.raise_()
        self.mainthread_icon.raise_()
        self.logthread_icon.raise_()
        self.ReadIcon.raise_()
        self.LogIcon.raise_()
        self.web_2.raise_()
        self.homepage.raise_()
        self.firight.raise_()
        self.fileft.raise_()
        self.Reset_Button.raise_()
        
        self.Titulo.raise_()
        self.ReleaseNotes.raise_()
        self.LPA_Label.raise_()
        self.FI_Label.raise_()
        self.BI_Label.raise_()
        self.SCTC_Label.raise_()
        self.Custom_Label.raise_()
        self.botao5s.raise_()
        self.tag5s.raise_()
        self.pagtotal.raise_()
        self.pagtual.raise_()
        self.barra.raise_()
        
        self.jabil.raise_()
        self.previous5s.raise_()
        self.next5s.raise_()

        Logged.setCentralWidget(self.centralwidget)

        self.retranslateUi(Logged)
        QtCore.QMetaObject.connectSlotsByName(Logged)
        

        

    def retranslateUi(self, Logged):
        _translate = QtCore.QCoreApplication.translate
        Logged.setWindowTitle(_translate("Logged", "Logged"))
        self.posto_id.setText(_translate("Logged", "posto"))
        self.operador_id.setText(_translate("Logged", "Victor      Hugo      Faria     Dias     Magalhães"))
        self.aio.setText(_translate("Logged", "All In One"))
        self.LPA_button.setText(_translate("Logged", "LPA"))
        self.FI_button.setText(_translate("Logged", "Ficha de Instrução"))
        self.BI_button.setText(_translate("Logged", "Solicitar Suporte"))
        self.jiga_button.setText(_translate("Logged", "Listar ferramentais"))
        self.custom_button.setText(_translate("Logged", "Custom Button"))
        self.yield1.setText(_translate("Logged", "80"))
        self.boasideias.setText(_translate("Logged", "6"))
        self.produtividade.setText(_translate("Logged", "99"))
        self.jabilcoins.setText(_translate("Logged", "0"))
        self.ReadIcon.setText(_translate("Matricula", "Read"))
        self.LogIcon.setText(_translate("Matricula", "Log"))
        self.Reset_Button.setText(_translate("Logged", "LPA não disponível ?\n"
"Clique Aqui"))
        self.Titulo.setText(_translate("Logged", "Novidades"))
        self.ReleaseNotes.setText(_translate("Logged", "<html><head/><body><p>v52:</p><p>• Implementação de 5S Posto Ideal produção.</p><p>• Implementação FI Creator produção.</p><p>v51:</p><p>• Implementação de 5S Posto Ideal produção.</p><p>v47: </p><p>• Atalho para página inicial agora no logo da Jabil.</p><p>• Implementação FI Creator Stage.</p><p>v46:</p><p>• Novo botão de reset na tela inicial, para reiniciar o</p><p> All in One sem precisar fazer login.</p></body></html>"))
        self.LPA_Label.setText(_translate("Logged", "<html><head/><body><p><span style=\" color:#4c4c4c;\">Aos ínicios de turno, clique em &quot;LPA&quot; para carregar e preencher LPA.</span></p></body></html>"))
        self.FI_Label.setText(_translate("Logged", "<html><head/><body><p><span style=\" color:#4c4c4c;\">Carrega a Ficha de Instrução referente ao posto e ao produto rodando na linha.</span></p></body></html>"))
        self.BI_Label.setText(_translate("Logged", "<html><head/><body><p><span style=\" color:#4c4c4c;\">Carrega Formulário para registro de Boas Ideias. </span></p></body></html>"))
        self.SCTC_Label.setText(_translate("Logged", "<html><head/><body><p><span style=\" color:#4c4c4c;\">Exibe ferramentas a vencer/vencidas para esta linha no SCTC.</span></p></body></html>"))
        self.Custom_Label.setText(_translate("Logged", "<html><head/><body><p><span style=\" color:#4c4c4c;\">Em construção</span></p></body></html>"))
        self.tag5s.setText(_translate("Logged", "5s"))
        self.pagtotal.setText(_translate("Logged", "3"))
        self.pagtual.setText(_translate("Logged", "1"))
        self.barra.setText(_translate("Logged", "/"))
import new_resource_image
