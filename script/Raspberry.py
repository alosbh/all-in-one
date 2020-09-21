# -*- coding: utf-8 -*-
#Sytem Libs
import platform
import socket
import logging

global logger
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)

class Raspberry:

    def __init__(self):

        try:

            # Get Hostname
            self.Name = platform.node();
            #Get system Info
            self.System = platform.system();
            self.SystemVersion = platform.version();
            self.SystemRelease = platform.release();    
            self.Validated = False;
            self.GetSystemInfo();

            logger.debug("Successfully created Raspberry object " + self.Name )

        except Exception as e:

            logger.error("Error creating Raspberry object. Exception: " + type(e).__name__ )


        

    def GetSystemInfo(self):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.MAC = ""
