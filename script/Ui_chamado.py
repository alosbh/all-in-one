# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chamado.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(353, 240)
        MainWindow.setMinimumSize(QtCore.QSize(346, 133))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sup_verde = QtWidgets.QLabel(self.centralwidget)
        self.sup_verde.setGeometry(QtCore.QRect(0, 0, 508, 20))
        self.sup_verde.setStyleSheet("background: transparent;\n"
"background-color: rgb(0, 166, 90);\n"
"border-style: solid;\n"
"border-color: transparent;")
        self.sup_verde.setText("")
        self.sup_verde.setAlignment(QtCore.Qt.AlignCenter)
        self.sup_verde.setObjectName("sup_verde")
        self.lista_motivos = QtWidgets.QComboBox(self.centralwidget)
        self.lista_motivos.setGeometry(QtCore.QRect(90, 130, 231, 22))
        self.lista_motivos.setObjectName("lista_motivos")
        self.btn_solicitar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_solicitar.setGeometry(QtCore.QRect(30, 180, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_solicitar.sizePolicy().hasHeightForWidth())
        self.btn_solicitar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_solicitar.setFont(font)
        self.btn_solicitar.setStyleSheet("background-color:rgb(180, 231, 180);")
        self.btn_solicitar.setObjectName("btn_solicitar")
        self.rd_btn_engenharia = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_btn_engenharia.setEnabled(True)
        self.rd_btn_engenharia.setGeometry(QtCore.QRect(30, 30, 110, 17))
        self.rd_btn_engenharia.setObjectName("rd_btn_engenharia")
        self.rd_btn_manufatura = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_btn_manufatura.setEnabled(False)
        self.rd_btn_manufatura.setGeometry(QtCore.QRect(30, 50, 110, 17))
        self.rd_btn_manufatura.setObjectName("rd_btn_manufatura")
        self.rd_btn_ic = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_btn_ic.setEnabled(False)
        self.rd_btn_ic.setGeometry(QtCore.QRect(30, 90, 110, 17))
        self.rd_btn_ic.setObjectName("rd_btn_ic")
        self.rd_btn_qualidade = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_btn_qualidade.setEnabled(False)
        self.rd_btn_qualidade.setGeometry(QtCore.QRect(30, 70, 110, 17))
        self.rd_btn_qualidade.setObjectName("rd_btn_qualidade")
        self.lbl_motivos = QtWidgets.QLabel(self.centralwidget)
        self.lbl_motivos.setGeometry(QtCore.QRect(10, 130, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_motivos.setFont(font)
        self.lbl_motivos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.lbl_motivos.setObjectName("lbl_motivos")
        self.lbl_tempo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tempo.setGeometry(QtCore.QRect(170, 60, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tempo.setFont(font)
        self.lbl_tempo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tempo.setObjectName("lbl_tempo")
        self.lbl_status = QtWidgets.QLabel(self.centralwidget)
        self.lbl_status.setGeometry(QtCore.QRect(180, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_status.setFont(font)
        self.lbl_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status.setObjectName("lbl_status")
        self.btn_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancelar.setEnabled(True)
        self.btn_cancelar.setGeometry(QtCore.QRect(190, 180, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancelar.sizePolicy().hasHeightForWidth())
        self.btn_cancelar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setStyleSheet("background-color:rgb(230, 180, 180);")
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.btn_finalizar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_finalizar.setGeometry(QtCore.QRect(30, 180, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_finalizar.sizePolicy().hasHeightForWidth())
        self.btn_finalizar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_finalizar.setFont(font)
        self.btn_finalizar.setStyleSheet("background-color:rgb(180, 231, 180);")
        self.btn_finalizar.setObjectName("btn_finalizar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.btn_cancelar.setVisible(False)
        self.btn_finalizar.setVisible(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chamado"))
        self.btn_solicitar.setText(_translate("MainWindow", "Solicitar suporte"))
        self.rd_btn_engenharia.setText(_translate("MainWindow", "Engenharia"))
        self.rd_btn_manufatura.setText(_translate("MainWindow", "Manufatura"))
        self.rd_btn_ic.setText(_translate("MainWindow", "IC"))
        self.rd_btn_qualidade.setText(_translate("MainWindow", "Qualidade"))
        self.lbl_motivos.setText(_translate("MainWindow", "Motivo:"))
        self.lbl_tempo.setText(_translate("MainWindow", "00:00"))
        self.lbl_status.setText(_translate("MainWindow", "Não solicitado"))
        self.btn_cancelar.setText(_translate("MainWindow", "Cancelar chamado"))
        self.btn_finalizar.setText(_translate("MainWindow", "Finalizar chamado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
