# -*- coding: utf-8 -*-
#Sytem Libs
import platform
import socket
import logging
import requests
import sys
import json
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
            
            url = "http://10.57.39.13:3000/api/v1.0/system/info"

            # request = requests.get(url, headers={'Authorization': 'Bearer ' + token})
            print('1')
            request = requests.get(url)
            print('2')
            response = json.loads(request.content)
            self.Name = response['hostname']
            print(self.Name)
            print('--------------')
            sys.exit()

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