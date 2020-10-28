# -*- coding: utf-8 -*-
#Sytem Libs
import platform
import socket
import logging
import requests
import sys
import json
import os
from time import sleep

global logger
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)

class Raspberry:

    def __init__(self):

        try:
            # Get Hostname
            # self.Name = platform.node()
            #Get system Info
            self.System = platform.system()
            self.SystemVersion = platform.version()
            self.SystemRelease = platform.release()  
            self.Validated = False
            self.GetSystemInfo()


            # Get Hostname by request
            print('--------------')
            # url = "https://pi-login.docker.corp.jabil.org/api/v1.0/auth/ip?value=10.57.39.13"
            # body={}
            # headers={}
            # headers={"username": "",
            #         "password": "",
            #         "Content-Type": "application/json"}
            # request = requests.post(url, data=body, headers=headers, verify = False)
            # response = json.loads(request.content)
            # print(response)
            # token = response['token']

            # sleep(1)
            
            # request = requests.get(url, headers={'Authorization': 'Bearer ' + token})

            ip = os.environ.get('SYSCON_IP')
            
            
            print('--------------**********************')
            url = "http://" + ip + "/api/v1.0/system/info"
            print("requst url: " + url)
            request = requests.get(url)
            response = json.loads(request.content)
            
            print("RESPONSE:")
            print(request)
            print(response)
            
           
            
            print('--------------')

            logger.debug("Successfully created Raspberry object " + self.Name )

        except Exception as e:

            logger.error("Error creating Raspberry object. Exception: " + type(e).__name__ )
            print("deu errado")
            sys.exit()

    def GetSystemInfo(self):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.MAC = ""
        
    def getRaspName(self):
        return self.Name