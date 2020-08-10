# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\\brbelm0te01\Jabiltest\AIO\26- Leitura Crachá GUI V26\uis\chamado.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(346, 133)
        MainWindow.setMinimumSize(QtCore.QSize(346, 133))
        MainWindow.setMaximumSize(QtCore.QSize(346, 133))
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
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(57, 60, 232, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(27, 20, 292, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 100, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(231, 231, 231);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chamado"))
        self.label.setText(_translate("MainWindow", "De qual time você precisa de suporte?"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
