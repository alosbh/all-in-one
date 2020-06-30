# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logged.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Logged(object):
    def setupUi(self, Logged):
        Logged.setObjectName("Logged")
        Logged.resize(1365, 767)
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
        self.jabil = QtWidgets.QLabel(self.centralwidget)
        self.jabil.setGeometry(QtCore.QRect(80, 5, 201, 41))
        self.jabil.setStyleSheet("background: url(:/Imgs/LogoJabil.png);")
        self.jabil.setText("")
        self.jabil.setObjectName("jabil")
        self.aio = QtWidgets.QLabel(self.centralwidget)
        self.aio.setGeometry(QtCore.QRect(0, 52, 361, 71))
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
        self.web = QtWidgets.QGraphicsView(self.centralwidget)
        self.web.setGeometry(QtCore.QRect(361, 51, 1011, 721))
        self.web.setObjectName("web")
        self.LPA_button = QtWidgets.QPushButton(self.centralwidget)
        self.LPA_button.setGeometry(QtCore.QRect(0, 300, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
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
        self.FI_button = QtWidgets.QPushButton(self.centralwidget)
        self.FI_button.setGeometry(QtCore.QRect(0, 369, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FI_button.setFont(font)
        self.FI_button.setStyleSheet("background-color:  rgb(30, 40, 44);\n"
"color: rgb(236, 240, 245);")
        self.FI_button.setAutoDefault(False)
        self.FI_button.setDefault(True)
        self.FI_button.setFlat(True)
        self.FI_button.setObjectName("FI_button")
        self.lat_verde_2 = QtWidgets.QLabel(self.centralwidget)
        self.lat_verde_2.setGeometry(QtCore.QRect(0, 301, 6, 69))
        self.lat_verde_2.setStyleSheet("background-color: rgb(30, 40, 44);")
        self.lat_verde_2.setText("")
        self.lat_verde_2.setObjectName("lat_verde_2")
        self.lat_verde_3 = QtWidgets.QLabel(self.centralwidget)
        self.lat_verde_3.setGeometry(QtCore.QRect(0, 371, 6, 69))
        self.lat_verde_3.setStyleSheet("background-color: rgb(30, 40, 44);")
        self.lat_verde_3.setText("")
        self.lat_verde_3.setObjectName("lat_verde_3")
        self.BI_button = QtWidgets.QPushButton(self.centralwidget)
        self.BI_button.setGeometry(QtCore.QRect(0, 438, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
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
        self.lat_verde_4.setGeometry(QtCore.QRect(0, 442, 6, 69))
        self.lat_verde_4.setStyleSheet("background-color:  rgb(30, 40, 44);")
        self.lat_verde_4.setText("")
        self.lat_verde_4.setObjectName("lat_verde_4")
        self.chamado_button = QtWidgets.QPushButton(self.centralwidget)
        self.chamado_button.setGeometry(QtCore.QRect(0, 507, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chamado_button.setFont(font)
        self.chamado_button.setStyleSheet("background-color: rgb(30, 40, 44);\n"
"color: rgb(236, 240, 245);")
        self.chamado_button.setAutoDefault(False)
        self.chamado_button.setDefault(True)
        self.chamado_button.setFlat(True)
        self.chamado_button.setObjectName("chamado_button")
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
        self.yield = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.yield.setFont(font)
        self.yield.setStyleSheet("color: white;\n"
"")
        self.yield.setAlignment(QtCore.Qt.AlignCenter)
        self.yield.setObjectName("yield")
        self.gridLayout_2.addWidget(self.yield, 0, 0, 1, 1)
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
        self.lat_verde_5 = QtWidgets.QLabel(self.centralwidget)
        self.lat_verde_5.setGeometry(QtCore.QRect(0, 510, 6, 69))
        self.lat_verde_5.setStyleSheet("background-color:  rgb(30, 40, 44);")
        self.lat_verde_5.setText("")
        self.lat_verde_5.setObjectName("lat_verde_5")
        self.MainThread_IconGray = QtWidgets.QLabel(self.centralwidget)
        self.MainThread_IconGray.setEnabled(True)
        self.MainThread_IconGray.setGeometry(QtCore.QRect(15, 60, 24, 24))
        self.MainThread_IconGray.setAutoFillBackground(False)
        self.MainThread_IconGray.setStyleSheet("background: url(:/Imgs/circlegray.png);\n"
"")
        self.MainThread_IconGray.setText("")
        self.MainThread_IconGray.setObjectName("MainThread_IconGray")
        self.web_2 = QtWidgets.QLabel(self.centralwidget)
        self.web_2.setEnabled(True)
        self.web_2.setGeometry(QtCore.QRect(361, 51, 1011, 721))
        self.web_2.setStyleSheet("border-image: url(:/Imgs/LINK2500-2.png);")
        self.web_2.setText("")
        self.web_2.setObjectName("web_2")
        self.firight = QtWidgets.QLabel(self.centralwidget)
        self.firight.setGeometry(QtCore.QRect(1280, 690, 64, 64))
        self.firight.setStyleSheet("border-radius: 43px;\n"
"background-color: white;\n"
"background: url(:/Imgs/rightarrow.png);")
        self.firight.setText("")
        self.firight.setObjectName("firight")
        self.fileft = QtWidgets.QLabel(self.centralwidget)
        self.fileft.setGeometry(QtCore.QRect(1200, 690, 64, 64))
        self.fileft.setStyleSheet("border-radius: 43px;\n"
"background-color: white;\n"
"background: url(:/Imgs/leftarrow.png);")
        self.fileft.setText("")
        self.fileft.setObjectName("fileft")
        self.Reset_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Reset_Button.setGeometry(QtCore.QRect(380, 700, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Reset_Button.setFont(font)
        self.Reset_Button.setStyleSheet("background-color:  rgb(165, 201, 200);\n"
"color: rgb(236, 240, 245);\n"
"border-radius:10px")
        self.Reset_Button.setAutoDefault(False)
        self.Reset_Button.setDefault(True)
        self.Reset_Button.setFlat(True)
        self.Reset_Button.setObjectName("Reset_Button")
        self.background.raise_()
        self.lat_preto.raise_()
        self.posto_id.raise_()
        self.operador_id.raise_()
        self.sup_verde.raise_()
        self.foto.raise_()
        self.aro_branco.raise_()
        self.sup_branco.raise_()
        self.jabil.raise_()
        self.aio.raise_()
        self.lat_verde.raise_()
        self.web.raise_()
        self.LPA_button.raise_()
        self.FI_button.raise_()
        self.lat_verde_2.raise_()
        self.lat_verde_3.raise_()
        self.BI_button.raise_()
        self.lat_verde_4.raise_()
        self.chamado_button.raise_()
        self.gridLayoutWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        self.lat_verde_5.raise_()
        self.MainThread_IconGray.raise_()
        self.web_2.raise_()
        self.firight.raise_()
        self.fileft.raise_()
        self.Reset_Button.raise_()
        Logged.setCentralWidget(self.centralwidget)

        self.retranslateUi(Logged)
        QtCore.QMetaObject.connectSlotsByName(Logged)

    def retranslateUi(self, Logged):
        _translate = QtCore.QCoreApplication.translate
        Logged.setWindowTitle(_translate("Logged", "Logged"))
        self.posto_id.setText(_translate("Logged", "posto"))
        self.operador_id.setText(_translate("Logged", "Victor      Hugo      Faria     Dias     Magalhães"))
        self.aio.setText(_translate("Logged", "All In One v0.38"))
        self.LPA_button.setText(_translate("Logged", "LPA"))
        self.FI_button.setText(_translate("Logged", "Ficha de Instrução"))
        self.BI_button.setText(_translate("Logged", "Boas Ideias"))
        self.chamado_button.setText(_translate("Logged", "Solicitar Suporte"))
        self.yield.setText(_translate("Logged", "80"))
        self.boasideias.setText(_translate("Logged", "6"))
        self.produtividade.setText(_translate("Logged", "99"))
        self.jabilcoins.setText(_translate("Logged", "0"))
        self.Reset_Button.setText(_translate("Logged", "LPA não disponível ?\n"
"Clique Aqui"))
import resources_mat_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Logged = QtWidgets.QMainWindow()
    ui = Ui_Logged()
    ui.setupUi(Logged)
    Logged.show()
    sys.exit(app.exec_())
