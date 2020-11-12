# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login_Screen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 773)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_loginscreen = QtWidgets.QWidget(MainWindow)
        self.main_loginscreen.setObjectName("main_loginscreen")
        self.btn_reset = QtWidgets.QPushButton(self.main_loginscreen)
        self.btn_reset.setGeometry(QtCore.QRect(5, 5, 41, 41))
        self.btn_reset.setStyleSheet("image: url(:/Img/desligar branco.png);\n"
"background-color: rgb(58, 77, 215);\n"
"border: 10px")
        self.btn_reset.setText("")
        self.btn_reset.setObjectName("btn_reset")
        self.lbl_BIGlogo = QtWidgets.QLabel(self.main_loginscreen)
        self.lbl_BIGlogo.setGeometry(QtCore.QRect(0, 0, 767, 773))
        self.lbl_BIGlogo.setStyleSheet("border-image: url(:/Img/BIG_logo.PNG);")
        self.lbl_BIGlogo.setText("")
        self.lbl_BIGlogo.setObjectName("lbl_BIGlogo")
        self.lbl_iconcracha = QtWidgets.QLabel(self.main_loginscreen)
        self.lbl_iconcracha.setGeometry(QtCore.QRect(1035, 590, 61, 61))
        self.lbl_iconcracha.setStyleSheet("image: url(:/Img/insert_badge.png);")
        self.lbl_iconcracha.setText("")
        self.lbl_iconcracha.setObjectName("lbl_iconcracha")
        self.lbl_insertbadge = QtWidgets.QLabel(self.main_loginscreen)
        self.lbl_insertbadge.setGeometry(QtCore.QRect(1015, 660, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_insertbadge.setFont(font)
        self.lbl_insertbadge.setStyleSheet("color: rgb(45, 34, 94)")
        self.lbl_insertbadge.setObjectName("lbl_insertbadge")
        self.lbl_verticallogo = QtWidgets.QLabel(self.main_loginscreen)
        self.lbl_verticallogo.setGeometry(QtCore.QRect(430, -250, 1251, 871))
        self.lbl_verticallogo.setStyleSheet("image: url(:/Img/logo_vert-01.svg);")
        self.lbl_verticallogo.setText("")
        self.lbl_verticallogo.setObjectName("lbl_verticallogo")
        self.lbl_value_version = QtWidgets.QLabel(self.main_loginscreen)
        self.lbl_value_version.setGeometry(QtCore.QRect(1163, 250, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(11)
        self.lbl_value_version.setFont(font)
        self.lbl_value_version.setStyleSheet("color: rgb(45, 34, 94)")
        self.lbl_value_version.setObjectName("lbl_value_version")
        self.lbl_value_workstation = QtWidgets.QLabel(self.main_loginscreen)
        self.lbl_value_workstation.setGeometry(QtCore.QRect(930, 370, 291, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_value_workstation.setFont(font)
        self.lbl_value_workstation.setStyleSheet("color: rgb(45, 34, 94)")
        self.lbl_value_workstation.setObjectName("lbl_value_workstation")
        self.lbl_workstation = QtWidgets.QLabel(self.main_loginscreen)
        self.lbl_workstation.setGeometry(QtCore.QRect(1035, 405, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(10)
        self.lbl_workstation.setFont(font)
        self.lbl_workstation.setStyleSheet("color: rgb(116, 111, 138)")
        self.lbl_workstation.setObjectName("lbl_workstation")
        self.lbl_jabilogo = QtWidgets.QLabel(self.main_loginscreen)
        self.lbl_jabilogo.setGeometry(QtCore.QRect(10, 740, 71, 31))
        self.lbl_jabilogo.setStyleSheet("IMAGE: url(:/Img/JabilMasterBrand_White.png);\n"
"background-color:rgb(72, 75, 218)")
        self.lbl_jabilogo.setText("")
        self.lbl_jabilogo.setObjectName("lbl_jabilogo")
        self.lbl_value_hostname = QtWidgets.QLabel(self.main_loginscreen)
        self.lbl_value_hostname.setGeometry(QtCore.QRect(980, 465, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_value_hostname.setFont(font)
        self.lbl_value_hostname.setStyleSheet("color: rgb(45, 34, 94)")
        self.lbl_value_hostname.setObjectName("lbl_value_hostname")
        self.lbl_hostname = QtWidgets.QLabel(self.main_loginscreen)
        self.lbl_hostname.setGeometry(QtCore.QRect(1025, 500, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(10)
        self.lbl_hostname.setFont(font)
        self.lbl_hostname.setStyleSheet("color: rgb(116, 111, 138)")
        self.lbl_hostname.setObjectName("lbl_hostname")
        self.lbl_verticallogo.raise_()
        self.lbl_BIGlogo.raise_()
        self.btn_reset.raise_()
        self.lbl_iconcracha.raise_()
        self.lbl_insertbadge.raise_()
        self.lbl_value_version.raise_()
        self.lbl_value_workstation.raise_()
        self.lbl_workstation.raise_()
        self.lbl_jabilogo.raise_()
        self.lbl_value_hostname.raise_()
        self.lbl_hostname.raise_()
        MainWindow.setCentralWidget(self.main_loginscreen)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_insertbadge.setText(_translate("MainWindow", "Insira seu crachá"))
        self.lbl_value_version.setText(_translate("MainWindow", "V1.00"))
        self.lbl_value_workstation.setText(_translate("MainWindow", "INGCUSMIN002"))
        self.lbl_workstation.setText(_translate("MainWindow", "POSTO"))
        self.lbl_value_hostname.setText(_translate("MainWindow", "BRBELRASP333"))
        self.lbl_hostname.setText(_translate("MainWindow", "HOSTNAME"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
