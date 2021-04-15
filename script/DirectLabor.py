# -*- coding: utf-8 -*-


from ApiManager import *
import sys
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QBitmap, QColor,QPainter,QImage,QBrush,QWindow
from PyQt5.QtCore import Qt, QRect
import urllib.request
import requests
import json

global logger
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)

class DirectLabor:

    def __init__(self, RaspberryObject ="None"):
        self.Name = ""
        self.ID = ""
        self.ID_trim = ""
        self.RouteId = ""
        self.Area = ""
        self.Productivity = ""
        self.Yield = ""
        self.GoodIdeas = ""
        self.JabilCoins = ""
        self.NickName = ""
        self.Enabled = ""
        self.OtherControls = ""
        self.productName = ""
        self.Validated = False
        self.picture = None
        self.ws = ApiManager()


    # Setup User Attributes and Metrics
    def Setup(self, LoginResponse, hostname):
        self.Name = LoginResponse["UserName"]
        name_array = self.Name.split(" ")
        name_len = len(name_array)
        self.Name = name_array[0] + " " + name_array[name_len-1]

        self.ID_trim = LoginResponse["UserRegistration"]
        self.Load_Metrics(hostname)
        
        # get used id
        baseUrl = "http://brbelm0apps02/AIOService/Jmd/GetUserDetailsByRegistration/" + str(self.ID_trim)
        userdid = requests.get(baseUrl)
        userdid = userdid.json()['idUser']
        self.ID = userdid

        # loading user image
        pixmap = self.load_avatar()
        self.picture= pixmap
        


    def Load_Metrics(self, hostname):
        
        # Starts the API manager
        ws = ApiManager()

        # Api call to get actual user metrics on the workstation
        Metrics = ws.Request(ws.AIO_Dashboard, "GetActualUserAttributes", hostname)
        
        try:
        # Parse out Yield and Productivity from the Metrics
            self.Yield = str(round(float(Metrics[0]["Attributes"][3]["Percent"]), 1))
            self.Productivity = str(round(float(Metrics[0]["Attributes"][4]["Percent"]), 1))
            self.GoodIdeas = str(0)
            self.JabilCoins = str(0)
            logger.debug("Successfully loaded user metrics")
        except Exception as e:
            logger.error("Couldnt load user metrics. Error:" + type(e).__name__)


    def load_avatar(self):
        baseurl = 'http://brbelm0apps01/UserImage/' + self.ID_trim + '.jpg'

        try:
            url = urllib.request.urlopen(baseurl)
        except:
            url = urllib.request.urlopen('http://brbelm0apps01/UserImage/Default.jpg')

        data = url.read()

        # Load image and convert to 32-bit ARGB (adds an alpha channel):
        image = QImage.fromData(data, 'jpg')
        image.convertToFormat(QImage.Format_ARGB32)

        # Crop image to a square:
        imgsize = min(image.width(), image.height())
        rect = QRect(
        (image.width() - imgsize) / 2,
        (image.height() - imgsize) / 2,
        imgsize,
        imgsize,
        )
        image = image.copy(rect)

        # Create the output image with the same dimensions and an alpha channel
        # and make it completely transparent:
        out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)

        # Create a texture brush and paint a circle with the original image onto
        # the output image:
        brush = QBrush(image)        # Create texture brush
        painter = QPainter(out_img)  # Paint the output image
        painter.setBrush(brush)      # Use the image texture brush
        painter.setPen(Qt.NoPen)     # Don't draw an outline
        painter.setRenderHint(QPainter.Antialiasing, True)  # Use AA
        painter.drawEllipse(0, 0, imgsize, imgsize)  # Actually draw the circle
        painter.end()                # We are done (segfault if you forget this)

        # Convert the image to a pixmap and rescale it.  Take pixel ratio into
        # account to get a sharp image on retina displays:
        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)
        size = 131 * pr
        pm = pm.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        return pm