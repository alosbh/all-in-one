# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\\brbelm0te01\Jabiltest\AIO\22 - Leitura Crachá GUI V22\uis\matricula.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NonLogged_Screen(object):
    def setupUi(self, Matricula):
        Matricula.setObjectName("Matricula")
        Matricula.resize(1366, 768)
        Matricula.setStyleSheet("background:transparent;\n"
"\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.517, y1:0.057, x2:0.505909, y2:1, stop:0 rgb(0, 82, 136), stop:1 rgb(34, 45, 50));\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(Matricula)
        self.centralwidget.setStyleSheet("background: transparent;")
        self.centralwidget.setObjectName("centralwidget")
        self.centro = QtWidgets.QLabel(self.centralwidget)
        self.centro.setGeometry(QtCore.QRect(514, 110, 341, 600))
        self.centro.setStyleSheet("background: transparent;\n"
"background-color: rgb(230, 230, 230);\n"
"border-color: transparent;\n"
"border-style: solid;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.centro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.centro.setText("")
        self.centro.setObjectName("centro")
        self.rfid_image = QtWidgets.QLabel(self.centralwidget)
        self.rfid_image.setGeometry(QtCore.QRect(604, 260, 161, 141))
        self.rfid_image.setStyleSheet("background: url(:/Imgs/image (1).png);\n"
"")
        self.rfid_image.setText("")
        self.rfid_image.setObjectName("rfid_image")

        self.mainthreadicon_on = QtWidgets.QLabel(self.centralwidget)
        self.mainthreadicon_on.setGeometry(QtCore.QRect(20, 720, 32, 32))
        self.mainthreadicon_on.setStyleSheet("background: url(:/Imgs/circlegreen.png);\n"
"")
        self.mainthreadicon_on.setText("")
        self.mainthreadicon_on.setObjectName("mainthreadicon_on")


        # self.label = QLabel()
        # self.movie = QMovie("loading.gif")
        # self.label.setMovie(self.movie)
        # self.movie.start()



        self.insira = QtWidgets.QLabel(self.centralwidget)
        self.insira.setGeometry(QtCore.QRect(558, 420, 252, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.insira.setFont(font)
        self.insira.setStyleSheet("background: transparent;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.insira.setAlignment(QtCore.Qt.AlignCenter)
        self.insira.setObjectName("insira")




        self.nome_posto = QtWidgets.QLabel(self.centralwidget)
        self.nome_posto.setGeometry(QtCore.QRect(614, 580, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nome_posto.setFont(font)
        self.nome_posto.setStyleSheet("background: transparent;\n"
"background-color: transparent;\n"
"border-color: transparent;\n"
"border-style: solid;")
        self.nome_posto.setText("")
        self.nome_posto.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_posto.setObjectName("nome_posto")
        self.posto = QtWidgets.QLabel(self.centralwidget)
        self.posto.setGeometry(QtCore.QRect(574, 540, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.posto.setFont(font)
        self.posto.setStyleSheet("background: transparent;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.posto.setAlignment(QtCore.Qt.AlignCenter)
        self.posto.setObjectName("posto")
        self.aro_azul = QtWidgets.QLabel(self.centralwidget)
        self.aro_azul.setGeometry(QtCore.QRect(594, 30, 180, 180))
        self.aro_azul.setStyleSheet("background-color: white;\n"
" border-radius: 90px;\n"
"background-color:rgb(0, 82, 136);\n"
"")
        self.aro_azul.setText("")
        self.aro_azul.setObjectName("aro_azul")
        self.aro_verde = QtWidgets.QLabel(self.centralwidget)
        self.aro_verde.setGeometry(QtCore.QRect(604, 40, 160, 160))
        self.aro_verde.setStyleSheet("background-color:rgb(0, 138, 95);\n"
" border-radius: 80px;\n"
"\n"
"")
        self.aro_verde.setText("")
        self.aro_verde.setObjectName("aro_verde")
        self.aro_branco = QtWidgets.QLabel(self.centralwidget)
        self.aro_branco.setGeometry(QtCore.QRect(610, 46, 148, 148))
        self.aro_branco.setStyleSheet("background-color:rgb(230, 230, 230);\n"
" border-radius: 74px;\n"
"\n"
"")
        self.aro_branco.setText("")
        self.aro_branco.setObjectName("aro_branco")
        self.jota = QtWidgets.QLabel(self.centralwidget)
        self.jota.setGeometry(QtCore.QRect(644, 80, 81, 81))
        self.jota.setStyleSheet("background: url(:/Imgs/JOTA.png);")
        self.jota.setText("")
        self.jota.setObjectName("jota")
        self.posto_2 = QtWidgets.QLabel(self.centralwidget)
        self.posto_2.setGeometry(QtCore.QRect(574, 620, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.posto_2.setFont(font)
        self.posto_2.setStyleSheet("background: transparent;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.posto_2.setAlignment(QtCore.Qt.AlignCenter)
        self.posto_2.setObjectName("posto_2")
        self.nome_host = QtWidgets.QLabel(self.centralwidget)
        self.nome_host.setGeometry(QtCore.QRect(614, 660, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nome_host.setFont(font)
        self.nome_host.setStyleSheet("background: transparent;\n"
"background-color: transparent;\n"
"border-color: transparent;\n"
"border-style: solid;")
        self.nome_host.setText("")
        self.nome_host.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_host.setObjectName("nome_host")
        self.version = QtWidgets.QLabel(self.centralwidget)
        self.version.setGeometry(QtCore.QRect(1240, 690, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.version.setFont(font)
        self.version.setStyleSheet("color: rgb(230, 230, 230);")
        self.version.setObjectName("version")
        self.centro.raise_()
        self.aro_azul.raise_()
        self.rfid_image.raise_()
        self.mainthreadicon_on.raise_()
        self.insira.raise_()
        self.nome_posto.raise_()
        self.posto.raise_()
        self.aro_verde.raise_()
        self.aro_branco.raise_()
        self.jota.raise_()
        self.posto_2.raise_()
        self.nome_host.raise_()
        self.version.raise_()
        Matricula.setCentralWidget(self.centralwidget)

        self.retranslateUi(Matricula)
        QtCore.QMetaObject.connectSlotsByName(Matricula)

    def retranslateUi(self, Matricula):
        _translate = QtCore.QCoreApplication.translate
        Matricula.setWindowTitle(_translate("Matricula", "Matrícula"))
        self.insira.setText(_translate("Matricula", "Insira seu crachá:"))
        self.posto.setText(_translate("Matricula", "Posto:"))
        self.posto_2.setText(_translate("Matricula", "Hostname:"))
        self.version.setText(_translate("Matricula", ""))
import resources_mat_rc
