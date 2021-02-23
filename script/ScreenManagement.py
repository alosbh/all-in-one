from Ui_Login_Screen import *
from Ui_Logged_Screen import *
from Reset import *
from GlobalParameters import GlobalParameters
from FI import FI
from labels import labels
from Raspberry import Raspberry as Rasp
from ApiManager import ApiManager as ws
from DirectLabor import DirectLabor as DL
from OS_define import OS_define
from functions_5s import functions_5s
from LPAactions_controller import *
from Announcements_controller import *
from jit_support_controller import *
from Login_controller import Login_controller
from Fpl_controller import *
from theme_controller import theme_controller
from buttons_controller import buttons_controller

import time
import sys
import os
import logging
import traceback
import urllib.request

from PyQt5.QtCore import QObject, pyqtSignal, QUrl, QThread
from PyQt5.QtGui import QPixmap, QIcon
# from PyQt5.QtWebKit import QWebSettings

global logger
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)
# Instance of the class that manages the global parameters
GlobalParameters = GlobalParameters()

# Qt signal that drives the events
class QtSignal(QObject):
        signal = pyqtSignal(str)

#Starts the QT application that manages the widgets
class ScreenManagement():
    
    global QtApplication
    def __init__(self, *args, **kwargs):
        self.QtApplication = QtWidgets.QApplication([])

#----------------------------------------------------------------------------------

# Inherits the qt Ui_ResetWindow (reset confirmation window) design and manages its setup
class Reset_Window(QtWidgets.QMainWindow, Ui_ResetWindow):

    Reset_Signal = QtSignal()

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.Reset_QtWindow = QtWidgets.QMainWindow()
        self.setupUi(self.Reset_QtWindow)
        self.Reset_QtWindow.move((1366 - 346)/2, (768 - 133)/2)
        self.pushButton.clicked.connect(self.Reset)
        self.pushButton_2.clicked.connect(self.Hide)

    def Reset(self):
        command = 'echo b > sysrq'
        os.system(command)

    def Hide(self):
        self.Reset_QtWindow.hide()

    def Show(self):
        self.Reset_QtWindow.show()
        
#----------------------------------------------------------------------------------

# Inherits the qt Ui_Login_Screen (login screen) design and manages its setup
class NonLogged_Screen(QtWidgets.QMainWindow, Ui_Login_Screen):
    
    global NonLogged_QtWindow

    Workstation_Signal = QtSignal()
    
    def __init__(self, *args, **kwargs):
        self.Workstation_Signal.signal.connect(self.Print_Workstation)
        # Creates the Qt Widget that holds the UI 
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.NonLogged_QtWindow = QtWidgets.QMainWindow()
        self.app = ScreenManagement()

    def Setup(self, Station, Raspberry, Params, Reset_Window):
        self.Station = Station
        self.Raspberry = Raspberry
        self.Reset_Window = Reset_Window
        # Setup the designer UI on the QT window Widget
        self.setupUi(self.NonLogged_QtWindow)
        self.btn_reset.clicked.connect(self.reset)

        # Fill hostname, Workstation and AIO version fields
        self.lbl_value_hostname.setText(str(Raspberry.Name))
        self.lbl_value_version.setText(str(Params.AIO_Version))

        #Checks if the station was stablished - tries again if isn't
        if(Station.Enabled != 1):
            
            if(Station.Status == 'ConnectionError'):
                
                self.lbl_value_workstation.setText(str('No WiFi'))
                
            else:
                 self.lbl_value_workstation.setText(str('Error: ' + Station.Status))


            self.thread_workstation = GetWorkstationInfo()
            self.thread_workstation.startThread(self,Station,Raspberry)
        
        else:
            self.lbl_value_workstation.setText(str(Station.Name))

    def Show(self):
        self.NonLogged_QtWindow.showFullScreen()

    def Print_Workstation(self,Workstation_Id):
        self.lbl_value_workstation.setText(str(Workstation_Id))
    
    def reset(self):
        self.Reset_Window.Show()

#----------------------------------------------------------------------------------

# Inherits the qt Ui_Logged_Screen (main screen) design and manages its setup
class Logged_Screen(QtWidgets.QMainWindow, Ui_Logged_Screen, functions_5s, buttons_controller, jit_support_controller, LPAactions_controller, Announcements_controller, Fpl_controller, theme_controller):
    
    # Instance of the signal to act on button's click
    load_url_signal = QtSignal()

    global Logged_QtWindow

    def __init__(self, *args, **kwargs):

        # Creates the Qt Widget that holds the UI 
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.Logged_QtWindow = QtWidgets.QMainWindow()

        # Instance of the main thread, that keeps looking for RF readings and active user
        self.thread = Login_controller()

        # Connects the signal sent from the thread to display the url on the webviewer
        self.thread.thread_signal.signal.connect(self.load_url)
        self.thread.thread_signal2.signal.connect(self.Show)

        # Connects the signal sent from the buttons to display the url on the webviewer
        self.load_url_signal.signal.connect(self.load_url)

        self.loading_status = 1

        self.ActualFIPage = 1

    def Setup(self, Station, Raspberry, Params, NonLogged_Window, Reset_Window):
        self.setupUi(self.Logged_QtWindow)
        self.build_body_web()
        self.Station = Station
        self.DL = DL()
        self.Raspberry = Raspberry
        self.build_sidebar_buttons(self.Raspberry.Name, self.Station.Name, self.Station.RouteName)
        self.generate_5s(self.Station.Name)
        #self.setup_support_screen(self.Station.Name)

        # Fills labels with workstation values
        self.lbl_value_workstation.setText(str(self.Station.Name)) 
        self.lbl_value_version.setText(str(GlobalParameters.AIO_Version)) 
        self.lbl_value_line.setText(str(self.Station.RouteName))
        self.lbl_value_product.setText(str(self.Station.ProductName))
        self.lbl_value_client.setText(str(self.Station.ClientName))
        
        # Setting up reset window
        self.Reset_Window = Reset_Window

        # Starts the main thread and set its parameters
        self.thread.start()
        self.thread.host = Raspberry.Name
        self.thread.objStation = Station
        # Serves the thread the screen objects, so it can hide, show and manage the windows when needed.
        self.thread.NonLogged_Window = NonLogged_Window
        self.thread.Logged_Window = self

    def build_body_web(self):
        #setting up body_web - windows/raspberry
        #1 = windows / 0 = rasp
        self.operational_system = OS_define.get_OS_name()
        if self.operational_system == 1:
            from PyQt5.QtWebEngineWidgets import QWebEngineView
            from PyQt5.QtWebEngineCore import QWebEngineHttpRequest
            self.body_web = QWebEngineView(self.main)
        else:
            from PyQt5.QtWebKitWidgets import QWebView
            self.body_web = QWebView(self.main)
        self.body_web.setGeometry(QtCore.QRect(0, 0, 1121, 661))
        self.body_web.setObjectName("body_web")
        self.webSettings = self.body_web.settings()
        self.body_web.setVisible(False) 

    def preload_screen(self):
        self.preload_setup_fpl()
        self.btn_actionsLPA.hide()
        self.lbl_value_yield.setText('-')
        self.lbl_value_productivity.setText('-')
        self.lbl_value_goodideas.setText('-')
        self.lbl_value_jabilcoins.setText('-')

    # Method called in the MainThread - fills labor user fields
    def SetupUser(self, DL):
        print('Loading user ...')
        self.LPAactions_functions(self.Station.Name)
        self.load_announcements_label()
        self.lbl_value_name.setText(DL.Name)
        # self.lbl_value_yield.setText(DL.Yield)
        # self.lbl_value_productivity.setText(DL.Productivity)
        self.lbl_user_avatar.setPixmap(DL.picture)
        self.setup_fpl(DL.Name, DL.ID_trim)
        print('User loaded.')
        print('Functions working.')
        
    # Method to show the window widget 
    def Show(self):
        self.lbl_value_workstation.setText(self.Station.Name)
        self.Logged_QtWindow.showFullScreen()

    def reset(self):
        self.Reset_Window.Show()

    def suporte(self):
        self.body_home.setVisible(False)
        self.body_web.setVisible(False)
        self.body_support.setVisible(True)
        self.hide5s()

    def home(self):
        self.body_home.setVisible(True)
        self.body_web.setVisible(False)
        self.body_support.setVisible(False)
        self.hide5s()

    #Method to load an url on the webviewer
    def load_url(self, url):
        self.body_web.load(QUrl('about:blank'))
        time.sleep(1)
        self.loading_status = 0
        self.body_web.load(QUrl(url))
        self.body_home.setVisible(False) 
        self.body_web.setVisible(True)
        self.body_support.setVisible(False)
        self.body_web.show()

    def finish_loading(self):
        self.loading_status = 1
        logger.error("logger: terminou de carregar")
        print("print: terminou de carregar")
        self.FI_button.setEnabled(True)

    def load_ORMonitor(self):
        CustomAddr = self.thread.API.custom_button(self.Station.Area,self.Station.AreaTrim, self.Station.RouteMin, self.Station.Index)
        self.load_url_signal.signal.emit(CustomAddr)

    def load_stopwatcher(self):
        self.hide5s()
        url = "http://brbelm0itqa01/Stopwatch?workstationId="+ str(self.Station.Id) + "&userId=" + str(self.thread.DL.ID)
        print("############")
        print(url)
        print("############")
        self.load_url_signal.signal.emit(url)

    def jiga_list(self):
        self.hide5s()
        JigaAddr = self.thread.API.load_Jiga(self.thread.objStation.RouteId) 
        print(JigaAddr)
        self.load_url_signal.signal.emit(JigaAddr)
        
    def load_lpa(self):
        self.hide5s()
        LpaAddr = self.thread.API.load_LPA(self.thread.DL.ID_trim,self.thread.objStation.Id, self.thread.objStation.RouteId)
        self.load_url_signal.signal.emit(LpaAddr)
        
    def load_bi(self):
        self.hide5s()
        BIAddr = self.thread.API.load_BI(self.thread.DL.ID_trim,self.thread.objStation.Id) 
        self.load_url_signal.signal.emit(BIAddr)

    def load_fi(self):
        if self.operational_system == 1:    
            self.body_web.setZoomFactor(1) 
            FIAddr = self.thread.API.load_FI(self.Station.Name) 
            self.body_web.load(FIAddr)

        else:
            from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager

            self.urlFI = QUrl()
            self.urlFI.setScheme("http")
            self.urlFI.setHost("brbelm0apps01")
            self.urlFI.setPath("/FICreator/FiViewer/SlideShow")
            self.req = QNetworkRequest()
            self.req.setUrl(self.urlFI)
            self.req.setHeader(QNetworkRequest.ContentTypeHeader,('application/json'))
            self.nam  = QNetworkAccessManager()

            params = {"workstation":self.Station.Name,"prodashSync":True,"time":20}
            self.byteparam = bytes(json.dumps(params),'utf-8')
            self.body_web.load(self.req,QNetworkAccessManager.PostOperation,self.byteparam)
        
        self.body_home.setVisible(False) 
        self.body_web.setVisible(True) 
        self.body_support.setVisible(False) 
        self.hide5s()

#----------------------------------------------------------------------------------------
#Thread - tries to connect to station with the Raspberry info 
#----------------------------------------------------------------------------------------
class GetWorkstationInfo(QThread):
 
    def run(self):
        contadorThread = 0
        
        while(self.status != 1):
            # if(contadorThread<10):
            print("Attempt to get Station info: " + str(contadorThread))

            self.status = self.Station.GetStationInfo(self.Raspberry.Name)

            if(self.status != 1):
                time.sleep(30)

        self.Screen.Workstation_Signal.signal.emit(str(self.Station.Name))

    def startThread(self,Screen,Station,Raspberry):
        self.status = 0
        self.Screen = Screen
        self.Station = Station
        self.Raspberry = Raspberry
        self.start()