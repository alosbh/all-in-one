from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
import time
import sys
import new_resource_image
import resource_image

class RotateThread(QtCore.QThread):
 
    def method(self):
        
        if (self.controller.hover or self.controller2.hover):
            self.angle += 8
            self.obj.setRotation(self.angle)

    def startThread(self,obj,controller,controller2):
        self.controller = controller
        self.controller2 = controller2
        self.obj = obj
        self.angle = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.method)
        self.timer.start(50)


class Botao(QtWidgets.QPushButton):
    def __init__(self):
        super(Botao,self).__init__()
        self.setGeometry(QtCore.QRect(0, 0, 75, 71))
        self.setStyleSheet("border-image: url(:/Badge/5sbadge.png);background:transparent")
        self.hover = False
    def enterEvent(self,event):
        self.hover = True
    def leaveEvent(self,event):
        self.hover = False

class Tag5s(QtWidgets.QPushButton):
    def __init__(self,win):
        super(Tag5s,self).__init__(win)
        
        
        self.hover = False
    def enterEvent(self,event):
        self.hover = True
    def leaveEvent(self,event):
        self.hover = False





