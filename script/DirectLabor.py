# -*- coding: utf-8 -*-


from ApiManager import *
from pprint import pprint
import sys
import logging
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
        self.ws = ApiManager()


    # Setup User Attributes and Metrics
    def Setup(self, LoginResponse, hostname):
        
        self.Name = LoginResponse["UserName"]
        name_array = self.Name.split(" ")
        name_len = len(name_array)
        self.Name = name_array[0] + " " + name_array[name_len-1]

        self.ID_trim = LoginResponse["UserRegistration"]
        self.Load_Metrics(hostname)


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