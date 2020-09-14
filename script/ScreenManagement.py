#from Ui_NonLogged_Screen import *
from nonloggedscr import *
from Ui_Logged_Screen import *
from Reset import *
from Chamado import *
from GlobalParameters import GlobalParameters
from FI import FI
from labels import labels

# import MFRC522
import time
from shutil import copyfile
import urllib.request
import os
from PyQt5 import QtWidgets

from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

from ApiManager import ApiManager as ws
from DirectLabor import DirectLabor as DL
import logging
import traceback
from WebService import *

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

#Class that inherits the qt UI design and manages its setup
class NonLogged_Screen(QtWidgets.QMainWindow, Ui_Matricula):
    
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
        #self.Reset.clicked.connect(self.reset)
        #self.Reset.clicked.connect(self.Reset_Window.Show()) #;; vai funcionar? #)) chamava o metodo aqui dentro de reset

        # Fill hostname, Workstation and AIO version fields
        self.nome_host.setText(str(Raspberry.Name))
        self.version.setText(str(Params.AIO_Version))

        #Checks if the station was stablished - tries again if isn't
        if(Station.Enabled != 1):
            
            if(Station.Status == 'ConnectionError'):
                
                self.nome_posto.setText(str('No WiFi'))
                
            else:
                 self.nome_posto.setText(str('Error: ' + Station.Status))


            self.thread_workstation = GetWorkstationInfo()
            self.thread_workstation.startThread(self,Station,Raspberry)
        
        else:
            self.nome_posto.setText(str(Station.Name))

    def Show(self):
        self.NonLogged_QtWindow.showFullScreen()

    def Print_Workstation(self,Workstation_Id):
        self.nome_posto.setText(str(Workstation_Id))
    
    # def reset(self):
    #     self.Reset_Window.Show()

#----------------------------------------------------------------------------------

class Logged_Screen(QtWidgets.QMainWindow, Ui_Logged_Screen):
    
    # Instance of the signal to act on button's click
    button_signal = QtSignal()

    global Logged_QtWindow

    def __init__(self, *args, **kwargs):

        # Creates the Qt Widget that holds the UI 
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.Logged_QtWindow = QtWidgets.QMainWindow()

        # Instance of the main thread, that keeps looking for RF readings and active user
        self.thread = MainThread()

        # Connects the signal sent from the thread to display the url on the webviewer
        self.thread.thread_signal.signal.connect(self.load_url)
        self.thread.thread_signal2.signal.connect(self.Show)

        # Connects the signal sent from the buttons to display the url on the webviewer
        self.button_signal.signal.connect(self.load_url)

          #     self.thread.send2thread_signal.sig.connect(self.load_url)
    #     self.send2button_signal.sig.connect(self.load_url)

        self.loading_status = 1

        self.ActualFIPage = 1
        


    def Setup(self, Station, Raspberry, Params, NonLogged_Window, Reset_Window, Support_Window):
        
        # Setup the designer UI on the QT window Widget
        self.setupUi(self.Logged_QtWindow)
        # Links the buttons to their respective methods
        self.button_handle()
        self.body_web.loadFinished.connect(self.finish_loading) #;; ???
        # enables the webviewer
        self.load_url('about:blank')
        self.body_web.setVisible(False) #))web
        self.body_home.setVisible(True) #)) homepage
        #self.webSettings.setObjectCacheCapacities(0, 0, 0)
        # Fill the workstation Name
        self.Station = Station
        self.lbl_value_workstation.setText(str(self.Station.Name)) #))posto_id
        self.lbl_value_version.setText(str(GlobalParameters.AIO_Version)) #))aio
        self.Reset_Window = Reset_Window
        self.Support_Window = Support_Window
        self.Support_Window.posto = self.Station.Name
        self.Support_Window.index = self.Station.Index
        self.Support_Window.populateMotivos()

        self.thread_loading = WaitForPageLoad()

        # Starts the main thread and set its parameters
        self.thread.start()

        self.thread.host = Raspberry.Name
        self.thread.objStation = Station

        # Serves the thread the screen objects, so it can hide, show and manage the windows when needed.
        self.thread.NonLogged_Window = NonLogged_Window
        self.thread.Logged_Window = self

    #Method called in the MainThread - fills labor user fields
    def SetupUser(self, DL):
        #self.operador_id.setText(DL.Name) #))nao tem id na tela nova
        self.lbl_value_yield.setText(DL.Yield) #))yield1
        self.lbl_value_productivity.setText(DL.Productivity) #))produtividade
        self.lbl_value_goodideas.setText('-') #))boasideias
        self.lbl_value_jabilcoins.setText('-') #))jabilcoins

    # Method to show the window widget 
    def Show(self):
        self.lbl_value_workstation.setText(self.Station.Name) #))posto_id
        print("NOME DA MINHA WORKSTTION EH:" + self.Station.Name)
        self.Logged_QtWindow.showFullScreen()
   
#======================== faz tudo
    def button_handle(self):

        # Links the buttons to their respective methods
        # self.botao5s.label.clicked.connect(self.show5s)
        # self.tag5s.clicked.connect(self.show5s)
        # self.next5s.clicked.connect(self.proxpage)
        # self.previous5s.clicked.connect(self.antpage)
        self.btn_homepage.clicked.connect(self.home)
        self.btn_SCTC.clicked.connect(self.jiga_list) #))jiga_button
        #self.Reset.clicked.connect(self.reset)
        #self.Reset_Button.clicked.connect(self.Reset_Window.Show()) #;; onde fica?
        self.btn_instruction_sheet.clicked.connect(self.load_fi) #))FI_button
        self.btn_goodideas.clicked.connect(self.load_bi) #))BI_button
        self.btn_lpa.clicked.connect(self.load_lpa) #))LPA_button
        #self.custom_button.clicked.connect(self.custom_button_load)

    # def reset(self):
    #     self.Reset_Window.Show()

    def suporte(self):
        self.Support_Window.Show()

    def home(self):
        logger.error("Returning to initial screen")

        self.body_home.setVisible(True) #))homepage
        self.body_web.setVisible(False) #))web
        #self.Reset_Button.setVisible(False)
        #self.controllers5sOFF()

    # def show5s(self):
    #     self.body_home.setVisible(False) #))homepage
    #     self.obj5s = self.thread.API.load5s(self.Station.Name)
    #     self.contador = len(self.obj5s)-1
    #     self.state5s=0
        
    #     if(self.contador>=0):
    #         url = str(self.obj5s[self.state5s]['Path'])
            
    #         if(self.contador>0):
    #             self.pagtotal.setText(str(self.contador+1))
    #             self.pagtual.setText("1")
    #             self.controllers5sON()

    #     else:
    #         url = 'http://brbelm0itqa01/AIOService/Images5S/NaoEncontrado.png'
            
    #     self.button_signal.signal.emit(url)
    
    # def controllers5sON(self):
    #     self.pagtotal.setVisible(True)
    #     self.pagtual.setVisible(True)
    #     self.barra.setVisible(True)
    #     self.next5s.setVisible(True)

    # def controllers5sOFF(self):
    #     self.pagtotal.setVisible(False)
    #     self.pagtual.setVisible(False)
    #     self.barra.setVisible(False)
    #     self.previous5s.setVisible(False)
    #     self.next5s.setVisible(False)
        
    # #goes foward in the 5s menu
    # def proxpage(self):
    #     self.state5s = self.state5s+1
    #     self.previous5s.setVisible(True)
    #     self.pagtual.setText(str(self.state5s+1))
        
    #     if(self.state5s==self.contador):
    #         self.next5s.setVisible(False)
            
    #     url = str(self.obj5s[self.state5s]['Path'])
    #     self.button_signal.signal.emit(url)

    # #goes backward in the 5s menu
    # def antpage(self):
    #     self.state5s = self.state5s-1
    #     self.next5s.setVisible(True)
    #     self.pagtual.setText(str(self.state5s+1))
        
    #     if(self.state5s==0):
    #         self.previous5s.setVisible(False)
            
    #     url = str(self.obj5s[self.state5s]['Path'])
    #     self.button_signal.signal.emit(url)


    #Method to load an url on the webviewer
    def load_url(self, url):
        self.body_web.load(QUrl('about:blank')) #))web
        time.sleep(1)
        self.loading_status = 0
        self.body_web.load(QUrl(url)) #))web
        self.body_web.show() #))web

    def finish_loading(self):
        self.loading_status = 1

    def custom_button_load(self):
        #self.Reset_Button.setVisible(False)
        self.body_web.setZoomFactor(0.8) #))web
        self.body_home.setVisible(False) #))homepage
        self.body_web.setVisible(True) #))web
        #self.controllers5sOFF()
        # Loads the tooling URL
        CustomAddr = self.thread.API.custom_button(self.Station.Area,self.Station.AreaTrim, self.Station.RouteName, self.Station.Index) 

        # Send the url via signal to the socket   
        self.button_signal.signal.emit(CustomAddr)

    def jiga_list(self):
        #self.Reset_Button.setVisible(False)
        self.body_web.setZoomFactor(1)
        self.body_home.setVisible(False) #))homepage
        self.body_web.setVisible(True)#))web
        #self.controllers5sOFF()

        # Loads the tooling URL
        JigaAddr = self.thread.API.load_Jiga(self.thread.objStation.RouteId) 

        # Send the url via signal to the socket   
        self.button_signal.signal.emit(JigaAddr)
        
    def load_lpa(self):
        self.body_web.setZoomFactor(1)
        self.body_home.setVisible(False) #))homepage
        self.body_web.setVisible(True)#))web
        #self.controllers5sOFF()

        # Loads the LPA URL
        LpaAddr = self.thread.API.load_LPA(self.thread.DL.ID_trim,self.thread.objStation.Id, self.thread.objStation.RouteId)

        # Send the url via signal to the socket   
        self.button_signal.signal.emit(LpaAddr)
        #self.thread_loading.startThread(self.button_signal,LpaAddr,self)
        #self.Reset_Button.setVisible(True)
        

    def load_bi(self):
        self.body_web.setZoomFactor(1)
        #self.Reset_Button.setVisible(False)
  
        # Loads the BI URL
        BIAddr = self.thread.API.load_BI(self.thread.DL.ID_trim) 

        self.body_home.setVisible(False) #))homepage
        self.body_web.setVisible(True)#))web
        #self.controllers5sOFF()

        # Send the url via signal to the socket 
        #self.thread_loading.startThread(self.button_signal,BIAddr,self)
        self.button_signal.signal.emit(BIAddr)
        

    def load_fi(self):
        self.body_web.setZoomFactor(1) #))web
        #self.Reset_Button.setVisible(False)
  
        # Loads the BI URL
        FIAddr = self.thread.API.load_FI(self.Station.Name) 

        self.body_home.setVisible(False) #))homepage
        self.body_web.setVisible(True) #))web
        #self.controllers5sOFF()
        # Send the url via signal to the socket 
        # self.thread_loading.startThread(self.button_signal,BIAddr,self)
        self.button_signal.signal.emit(FIAddr)

    


# def RFRead(): #Função de leitura e autenticação dos crachás Jabil
    
#     Read_ID = None

#          # Instantiate the RFID reader class
#     reader = MFRC522.MFRC522()

#          # Get the badge id from the RFID reader
#     Read_ID = reader.JABIL_Matricula() 

#          # close the SPI slot 
#     reader.close_SPI()

#     return Read_ID

#----------------------------------------------------------------------------------------
#Thread for badge reading
#----------------------------------------------------------------------------------------
class MainThread(QThread):
    
    thread_signal = QtSignal()
    thread_signal2 = QtSignal()
    global API
    global NonLogged_Window
    global Logged_Window
    global thread_time
    global logout_limit
    global DL
    
    def __init__(self, *args, **kwargs):
        super().__init__()

        # Loads thread sleep time and logout counter on null RF reads.
        self.thread_time = GlobalParameters.BadgeReader_ThreadTime/1000 
        self.logout_limit = GlobalParameters.BadgeReader_MininumGoodReads

        # Starts the API manager
        self.API = ws()

        # Starts the Direct Labor class management
        self.DL = DL()

        # Hostname and Workstation Parameters
        self.host = "brbelrasp"
        
        # Screen Objects
        self.NonLogged_Window = None
        self.Logged_Window = None
        
        
    def run(self):
        # Logged Badge ID
        global Actual_ID
        Actual_ID = None
        # New Badge ID read from the RF module
        global Read_ID
        #Starts logount counter, so the user will be disconnected after reaching the limit of NULL readings
        cont_logout = 0
        status_workstation = self.NonLogged_Window.Station.Enabled

        logger=logging.getLogger() 
        logger.setLevel(logging.DEBUG)
        
        while(True):

            # self.NonLogged_Window.mainthread_icon_off.setVisible(not(self.NonLogged_Window.mainthread_icon_off.isVisible()))
            # self.Logged_Window.mainthread_icon.setVisible(not(self.Logged_Window.mainthread_icon.isVisible()))
            
            try:
                Read_ID = 51008294
                # Read_ID = (RFRead()) # Reads Badge ID
            except Exception as e:
                traceback.print_exc()
                logger.error("RFID error: " + type(e).__name__)
                print(type(e).__name__)
                Read_ID = None
                self.NonLogged_Window.nome_posto.setText(str('Erro leitura RFID'))


            if (Read_ID != None and self.NonLogged_Window.Station.Enabled == 1 ): 

                
                cont_logout = 0

                # If the read id is not null, compares it to the active user. In case its different, login the new user. 
                print("Actual ID: " + str(Actual_ID))
                print("Read ID: " + str(Read_ID))
                if (Actual_ID != Read_ID):
                    

                    try:
                        # Api call to login a user on OJT server
                        logger.debug("Login user " + str(Read_ID) + "..........")
                        print("Login user ID " + str(Read_ID) + "..........")

                        LoginResponse = self.API.Request(self.API.OJT, "LoginByWorker", {'HostName': self.host, 'Badge': Read_ID});

                        # catch login status
                        status = LoginResponse['Status']
                        # status="Login realizado"
                        print("Stats1:"+status)

                    except Exception as e: 
                        traceback.print_exc()
                        logger.error("Login Error: " + type(e).__name__)
                        print(type(e).__name__)
                        status = ""
                        
                    print("Stats2:"+status)
                    # In case of succesfull login            
                    if(status=="Login realizado"):
                        # Setup the Direct Labor object with actual worker data
                        self.DL.Setup(LoginResponse, self.host)
                        # Setup the user fields on the logged screen
                        self.Logged_Window.SetupUser(self.DL)
                        # The active ID is the newly logged ID               
                        Actual_ID = Read_ID
                        print("Actual ID apos alterar: " + str(Actual_ID))
                        # Show the Logged screen and hide the initial screen
                        self.thread_signal2.signal.emit('about:blank')
                        # self.Logged_Window.Logged_QtWindow.show()
                        # self.NonLogged_Window.NonLogged_QtWindow.hide()


            else: 
                cont_logout += 1 
                
                #if the null reads has reached the limit and there is someone logged
                if (cont_logout >= self.logout_limit):
                    cont_logout = self.logout_limit
                    if (Actual_ID != None):
                        
                        try:
                            # API Call to logout the user
                            print("Logout user " + Actual_ID + ".........")
                            logger.debug("Logout user " + Actual_ID + ".........")
                            LogoutResponse = self.API.Request(self.API.OJT, "Logout", {'HostName': self.host, 'Badge': Actual_ID});
                            status = LogoutResponse['Status']

                            if((status=="Logout realizado")or (status=="Não encontrado")):
                                # Show home screen
                                self.NonLogged_Window.Show() 
                                #Hide the logged screen
                                self.Logged_Window.Logged_QtWindow.hide()
                                Actual_ID = None
                                self.Logged_Window.home()
                            
                        except Exception as e:
                            print("Couldnt do logout. Error: " + type(e).__name__)
                            logger.error("Couldnt do logout. Error: " + type(e).__name__)    


                        # Clear the webviewer on the logged screen
                        self.thread_signal.signal.emit('about:blank')
                        time.sleep(1)
  
            # Wait for next thread iteration           
            time.sleep(self.thread_time) 

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

#----------------------------------------------------------------------------------------
#Thread -
#----------------------------------------------------------------------------------------
class WaitForPageLoad(QThread):
    def run(self):
        self.Screen.loading_status = 0
        print('Loading URL:' + self.url)
        self.signal.signal.emit(self.url)
        
        timer_load = 0
        load_limit = 5

        while((timer_load < load_limit)  and (self.Screen.loading_status != 1)):
            time.sleep(1)
            timer_load = timer_load + 1 
            
        timer_load = 0

        self.Screen.Reset_Button.setVisible(True)

        while(self.Screen.loading_status != 1):
            
            print("Recarregando ........Status:" + str(self.Screen.loading_status))
            self.Screen.body_web.reload() #))web
            
            while((timer_load < load_limit ) and (self.Screen.loading_status != 1)):
                time.sleep(1)
                timer_load = timer_load + 1 

                print(str(timer_load) + '...........')

            timer_load = 0
            
        timer_load = 0

        print("Loading complete. Status:" + str(self.Screen.loading_status))

    def startThread(self,signal,url,Screen):
        self.signal = signal
        self.url = url
        self.Screen = Screen
        self.start()