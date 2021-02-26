# -*- coding: utf-8 -*-

#Sytem Libs
import platform
import socket

#API Communication Libs
import json
import requests

#All In One Classes
from Raspberry import Raspberry

import traceback
import sys
#GlobalPath Class

from ApiManager import ApiManager

import logging
global logger
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)


class Station:

    def __init__(self, RaspberryObject ="None"):
        self.Id = ""
        self.Name = ""
        self.RouteId = ""
        self.RouteName = ""
        self.RouteMin = ""
        self.Area = ""
        self.NickName = ""
        self.Enabled = ""
        self.Status = ""
        self.OtherControls = ""
        self.ProductName = ""
        self.ClientName = ""
        self.Validated = False
        self.Index = None

        if RaspberryObject == "None":
            logger.error("Invalid Raspberry object")
            raise Exception("O segundo parametro é obrigatorio.")
          
        if isinstance(RaspberryObject, Raspberry):
            self.Enabled = self.GetStationInfo(RaspberryObject.Name)

        elif isinstance(RaspberryObject, str):
            logger.error("Invalid Raspberry object")
            raise Exception("Invalid Raspberry object.")

        
#tries to connect to station with the Raspberry info and fill station info - 1=success 0=fail
    def GetStationInfo(self, RaspberryName):
        self.__IP = socket.gethostbyname(socket.gethostname())
        self.__MAC = ""
        
        
        global ws        
        ws = ApiManager()
        

        try:
            jsonData = ws.Request(ws.AIO, 'GetEquipmentByHostname', RaspberryName)

            lineName = ws.load_lineName(jsonData['Id'])
            lineName = lineName[0]
            
            returnStatus = ws.GetSingleValueFromJsonObject(jsonData,"Status", False)
            
            self.Id = ws.GetSingleValueFromJsonObject(jsonData,"Id", False)
            self.Name = ws.GetSingleValueFromJsonObject(jsonData,"Name", False)
            self.Area = self.Name[:6]
            self.AreaTrim = self.Name[:3]
            self.RouteMin = self.Name[:9]
            self.RouteName = lineName['Name']
            self.RouteId = ws.GetSingleValueFromJsonObject(jsonData,"LineId", False)
            self.Enabled = ws.GetSingleValueFromJsonObject(jsonData,"Status", False)
            self.Status = 'Success'
            logger.debug("Successfully created Station object " + str(self.Name) )
            self.Enabled = 1

            self.Index = int(self.Name[-2:])

            return 1

        except Exception as e:
            if(jsonData=='ConnectionError'):
                self.Status = 'ConnectionError'
                self.Enabled = 0
                logger.error("Error creating Station object. Exception: " + type(e).__name__ )

            elif(type(e).__name__ == 'ValueError'):
                print('Erro index: ' + type(e).__name__ )
                self.Status = 'Success'
                self.Enabled = 1
                return 1
                
            else:
                print('Unknow exception: ' + type(e).__name__ )
                self.Status = type(e).__name__
                self.Enabled = 0
                logger.error("Error creating Station object. Exception: " + type(e).__name__ )

            return 0
    def get_product_info(self):
        request_lineInfo = ws.Request(ws.AIO_Dashboard, "GetByLine", str(self.RouteId))

        if (request_lineInfo is None):
            self.ProductName = 'No product'
            self.ClientName = 'No client'
        else:
            self.ProductName = request_lineInfo['Product']
            self.ClientName = request_lineInfo['ProductionGroup']
