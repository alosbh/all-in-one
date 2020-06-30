import os
import subprocess
import logging
from subprocess import Popen
from Raspberry import Raspberry



global logger
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)



class Mount:

    def __init__(self):

        self.path = "/home/Logs"
        self.Raspberry = Raspberry()
        self.mountdir()
        

    def mountdir(self):
        
        if not os.path.exists(self.path):
            try:
                os.makedirs(self.path)
            except OSError:
                pass

        
        try:

            p = subprocess.Popen('mount -t cifs -o username=BELRASP01,password=J@bilB3l01 //10.57.16.51/Jabiltest/AIO/AIOGIT/AIO.Americas.BEL/Logs ' + self.path,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
            p.wait()
            (stdout, stderr) = p.communicate()
            rc = p.returncode

            
            if rc != 0:
                logger.error(stderr)
                print(stderr)
                
            else:
                print("Successfull mounted Virtual Drive")
                logger.debug("Successfull mounted Virtual Drive")

        


        except Exception as e:

            print("Could not run subprocess. Error: " + type(e).__name__)
            logger.error("Could not run subprocess. Error: " + type(e).__name__)

        
        if not os.path.exists(self.path + "/" + str(self.Raspberry.Name)):
            try:
                os.makedirs(self.path + "/" + str(self.Raspberry.Name))
            except OSError:
                print("Couldnt create new folder for log.")
                pass


            
         
