# -*- coding: utf-8 -*-

from Station import Station
from Raspberry import Raspberry
from ScreenManagement import *
from functions_5s import functions_5s
# import RPi.GPIO as GPIO
import os
import datetime

global Raspberry
Raspberry = Raspberry()
# Instance of the Raspberry hardware itself and its parameters


# Instance of the Workstation related to the Raspberry
global Station
Station = Station(Raspberry)

# Starts the screen management class
ScreenManagement = ScreenManagement()

# Instance of the Initial Screen, when the worker is not logged in.
global NonLogged_Screen
NonLogged_Screen = NonLogged_Screen()

# Instance of the Logged Screen and its features, when the worker is logged.
global Logged_Screen
Logged_Screen = Logged_Screen()

global Reset_Window
Reset_Window = Reset_Window()

global functions_5s
functions_5s = functions_5s()



def main():
        #Handling of the GPIO ports, to disable their warnings and reset all used ports.        
        # GPIO.setwarnings(False)
        # GPIO.cleanup()
   
        #Setup of the home screen UI and show it on startupprint
        NonLogged_Screen.Setup(Station,Raspberry,GlobalParameters,Reset_Window)
        NonLogged_Screen.Show()

        #Setup of the logged screen UI
        
        Logged_Screen.Setup(Station,Raspberry,GlobalParameters,NonLogged_Screen,Reset_Window)
     
        #Starts the QT application that manages the screens.
        ScreenManagement.QtApplication.exec_()


# Run main() function
if __name__ == "__main__":
        main()
