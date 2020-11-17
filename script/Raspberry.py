# -*- coding: utf-8 -*-
#Sytem Libs
import platform
import socket
import logging
import requests
import sys
import json
import os
from OS_define import *

global logger
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)

class Raspberry:

    def __init__(self):

        try:
            # Get Hostname
            #Get system Info
            self.System = platform.system()
            self.SystemVersion = platform.version()
            self.SystemRelease = platform.release()  
            self.Validated = False
            self.GetSystemInfo()

            self.OS_define = OS_define()
            OS = self.OS_define.get_OS_name()

            # Get Hostname by request
            if OS == 1:
                self.Name = 'BRBELME024'
            else:
                self.request_rasp_hostname()
            
            logger.debug("Successfully created Raspberry object " + self.Name )

        except Exception as e:
            logger.error("Error creating Raspberry object. Exception: " + type(e).__name__ )

    def request_rasp_hostname(self):
        ip = os.environ.get('SYSCON_IP')
        url = "http://" + ip + "/api/v1.0/system/info"
        request = requests.get(url)
        
        if request.status_code == 200:
            response = json.loads(request.content)
            hostname = response['hostname']
            self.Name = hostname
            self.Name = "brbelraspbusterdev3"
        else:
            self.request_rasp_hostname()
        
    def GetSystemInfo(self):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.MAC = ""
        
    def getRaspName(self):
        return self.Name