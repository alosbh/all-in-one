#from Ui_NonLogged_Screen import *
from nonloggedscr import *
from Ui_Logged_Screen import *
from Reset import *

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

        self.Reset.clicked.connect(self.reset)

        # Fill hostname, Workstation and AIO version fields
  
        self.nome_host.setText(str(Raspberry.Name))
        self.version.setText(str(Params.AIO_Version))


        if(Station.Enabled != 1):
            
            if(Station.Status == 'ConnectionError'):
                
                self.nome_posto.setText(str('No WiFi'))
                


            else:
                 self.nome_posto.setText(str('Error: ' + Station.Status))

            self.thread_workstation = GetWorkstationInfo()
            self.thread_workstation.startThread(self,Station,Raspberry)
        

        else:
            self.nome_posto.setText(str(Station.Name))


    def reset(self):

        
        self.Reset_Window.Show()


    # Show the window on the screen
    def Show(self):
        self.NonLogged_QtWindow.showFullScreen()

    def Print_Workstation(self,Workstation_Id):
        self.nome_posto.setText(str(Workstation_Id))


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

        # Connects the signal sent from the buttons to display the url on the webviewer
        self.button_signal.signal.connect(self.load_url)

          #     self.thread.send2thread_signal.sig.connect(self.load_url)
    #     self.send2button_signal.sig.connect(self.load_url)

        self.loading_status = 1

        self.ActualFIPage = 1
        


    def Setup(self, Station, Raspberry, Params, NonLogged_Window, Reset_Window):
        
        
        # Setup the designer UI on the QT window Widget
        self.setupUi(self.Logged_QtWindow)
        
        # Links the buttons to their respective methods
        self.button_handle()
        
        self.Reset_Window = Reset_Window
        
        self.web.loadFinished.connect(self.finish_loading)
        # enables the webviewer
        self.load_url('about:blank')
        self.web.setVisible(False)
        
        self.homepage.setVisible(True)
        global LabelsObject        
        LabelsObject = labels()

        
        self.labels=[self.Titulo,self.ReleaseNotes,self.LPA_Label,self.FI_Label,self.BI_Label,self.SCTC_Label,self.Custom_Label]
        try:
           self.Custom_Label.setText(LabelsObject.data['Labels'][4][str(Station.Area)][int(Station.Index)])
           self.custom_button.setText(LabelsObject.data['Buttons'][4][str(Station.Area)][int(Station.Index)])
         
        except:
           self.Custom_Label.setText(LabelsObject.data['Labels'][4]['GENERAL'])
           self.custom_button.setText(LabelsObject.data['Buttons'][4]['GENERAL'])

        self.webSettings.clearMemoryCaches()
        self.webSettings.setObjectCacheCapacities(0, 0, 0)
      
        #self.web.show()

        # Fill the workstation Name
        self.Station = Station
        self.posto_id.setText(str(self.Station.Name))
        self.aio.setText(str("All in One " + GlobalParameters.AIO_Version))
        
        


        self.thread_loading = WaitForPageLoad()

        # Starts the main thread and set its parameters
        self.thread.start()

        self.thread.host = Raspberry.Name
        self.thread.objStation = Station

        
        
     


        # Serves the thread the screen objects, so it can hide, show and manage the windows when needed.
        self.thread.NonLogged_Window = NonLogged_Window
        self.thread.Logged_Window = self

        

        

    def SetupUser(self, DL):

        # Set the labor user fields

        self.operador_id.setText(DL.Name)
        self.yield1.setText(DL.Yield)
        self.produtividade.setText(DL.Productivity)
        self.boasideias.setText('-')
        self.jabilcoins.setText('-')

    # Method to show the window widget 
    def Show(self):
        self.posto_id.setText(self.Station.Name)
        print("NOME DA MINHA WORKSTTION EH:" + self.Station.Name)
        self.Logged_QtWindow.showFullScreen()
   
    
    def button_handle(self):


        self.botao5s.label.clicked.connect(self.show5s)
        self.tag5s.clicked.connect(self.show5s)
        self.next5s.clicked.connect(self.proxpage)
        self.previous5s.clicked.connect(self.antpage)

        self.firight.clicked.connect(self.next_fi)
        self.fileft.clicked.connect(self.previous_fi)

        self.Reset_Button.clicked.connect(self.reset)
        
        self.jabil.clicked.connect(self.home)
        

        # Links the buttons to their respective methods
        self.FI_button.clicked.connect(self.load_fi)
        self.BI_button.clicked.connect(self.load_bi)
        self.LPA_button.clicked.connect(self.load_lpa)
        self.jiga_button.clicked.connect(self.jiga_list)
        self.custom_button.clicked.connect(self.custom_button_load)

        

        # Create the button labels object, to toggle them on/off when needed
        self.lbl_LPA = self.lat_verde_2
        self.lbl_FI = self.lat_verde_3
        self.lbl_BI = self.lat_verde_4
        self.lbl_JL = self.lat_verde_5
        self.lbl_CB = self.lat_verde_6
        self.lbl_OBJ = [self.lbl_LPA,self.lbl_FI,self.lbl_BI,self.lbl_JL,self.lbl_CB]
          
    def Toggle_textosOFF(self):
        for i in self.labels:
            i.setVisible(False)
            
    def Toggle_textosON(self):
        for i in self.labels:
            i.setVisible(True)
            


    # Method to turn a button label green and others gray
    def Toggle_Label(self,label):
        for i in self.lbl_OBJ:
            if(i==label):
                i.setStyleSheet("background-color: rgb(0, 166, 90);")
            else:
                i.setStyleSheet("background-color: rgb(30, 40, 44);")

    def TurnOFF_Label(self):
        
        self.Reset_Button.setVisible(False)

        for i in self.lbl_OBJ:
  
            i.setStyleSheet("background-color: rgb(30, 40, 44);")


    def reset(self):

        

        self.Reset_Window.Show()
        # command = 'echo b > sysrq'
        # print('Button Command: ' + command)
        # os.system(command)

    def home(self):

        logger.error("cloquei para voltar a tela inicial")

        self.web.setVisible(False)
        self.web_2.setVisible(False)
        self.homepage.setVisible(True)

        self.firight.setVisible(False)
        self.fileft.setVisible(False)
        self.Reset_Button.setVisible(False)
        

        self.TurnOFF_Label()
        self.Toggle_textosON()
        self.controllers5sOFF()

    
    def controllers5sON(self):
        self.pagtotal.setVisible(True)
        self.pagtual.setVisible(True)
        self.barra.setVisible(True)
        
        self.next5s.setVisible(True)

    def controllers5sOFF(self):
        self.pagtotal.setVisible(False)
        self.pagtual.setVisible(False)
        self.barra.setVisible(False)
        self.previous5s.setVisible(False)
        self.next5s.setVisible(False)

    def show5s(self):

        
        self.homepage.setVisible(False)
        self.Toggle_textosOFF()

        self.obj5s = self.thread.API.load5s(self.Station.Name)
        self.contador = len(self.obj5s)-1
        self.state5s=0
        
        
        if(self.contador>=0):
            url = str(self.obj5s[self.state5s]['Path'])
            
            if(self.contador>0):
                self.pagtotal.setText(str(self.contador+1))
                self.pagtual.setText("1")
                self.controllers5sON()
                

            
        else:
            url = 'http://brbelm0itqa01/AIOService/Images5S/NaoEncontrado.png'
            
        
        self.button_signal.signal.emit(url)
        
        

    def proxpage(self):

        

        self.state5s = self.state5s+1

        



        self.previous5s.setVisible(True)
        
        self.pagtual.setText(str(self.state5s+1))

        
        if(self.state5s==self.contador):
            
            
            self.next5s.setVisible(False)
            
        url = str(self.obj5s[self.state5s]['Path'])
        self.button_signal.signal.emit(url)

    def antpage(self):

        
        self.state5s = self.state5s-1
        


        self.next5s.setVisible(True)
        
        self.pagtual.setText(str(self.state5s+1))

        
        if(self.state5s==0):
            
            
            self.previous5s.setVisible(False)
            
        url = str(self.obj5s[self.state5s]['Path'])
        self.button_signal.signal.emit(url)







                    

    # Method to loag an url on the webviewer
    def load_url(self, url):
        #self.web.setUrl(QUrl(url))

        self.webSettings.clearMemoryCaches()
        self.web.load(QUrl('about:blank'))
        time.sleep(1)
        self.loading_status = 0
        self.web.load(QUrl(url))
        self.web.show()



    def finish_loading(self):
        self.loading_status = 1





    def custom_button_load(self):
        self.Reset_Button.setVisible(False)
        self.firight.setVisible(False)
        self.fileft.setVisible(False)

        
        self.Toggle_textosOFF()
        # Toggle the label on
        self.Toggle_Label(self.lbl_CB)


        self.web.setZoomFactor(0.8)
        self.web.setVisible(True)
        self.web_2.setVisible(False)
        
        self.homepage.setVisible(False)
        self.controllers5sOFF()
        # Loads the tooling URL
        CustomAddr = self.thread.API.custom_button(self.Station.Area, self.Station.RouteName, self.Station.Index) 

        # Send the url via signal to the socket   
        self.button_signal.signal.emit(CustomAddr)

    def jiga_list(self):
        self.Reset_Button.setVisible(False)
        self.firight.setVisible(False)
        self.fileft.setVisible(False)

        
        self.Toggle_textosOFF()
        
        # Toggle the label on
        self.Toggle_Label(self.lbl_JL)


        self.web.setZoomFactor(1)
        self.web.setVisible(True)
        self.web_2.setVisible(False)
        
        self.homepage.setVisible(False)
        self.controllers5sOFF()
        # Loads the tooling URL
        JigaAddr = self.thread.API.load_Jiga(self.thread.objStation.RouteId) 

        # Send the url via signal to the socket   
        self.button_signal.signal.emit(JigaAddr)
        
        


    def load_lpa(self):
        self.web.setZoomFactor(1)
        self.firight.setVisible(False)
        self.fileft.setVisible(False)
        
        # Toggle the label on
        self.Toggle_Label(self.lbl_LPA)

        self.web.setVisible(True)       
        self.web_2.setVisible(False)
       
        self.homepage.setVisible(False)
        self.controllers5sOFF()
        self.Toggle_textosOFF()

        # Loads the LPA URL
        LpaAddr = self.thread.API.load_LPA(self.thread.DL.ID_trim,self.thread.objStation.Id, self.thread.objStation.RouteId)
        # Send the url via signal to the socket   
        #self.button_signal.signal.emit(LpaAddr)
        self.thread_loading.startThread(self.button_signal,LpaAddr,self)

        
        #self.Reset_Button.setVisible(True)
        

    def load_bi(self):
        self.web.setZoomFactor(1)
        self.Reset_Button.setVisible(False)
        self.firight.setVisible(False)
        self.fileft.setVisible(False)
  
        # Toggle the label on
        self.Toggle_Label(self.lbl_BI)
        # Loads the BI URL
        BIAddr = self.thread.API.load_BI(self.thread.DL.ID_trim) 


        

        self.web.setVisible(True)
        self.web_2.setVisible(False) 

        self.homepage.setVisible(False)
        self.controllers5sOFF()
        self.Toggle_textosOFF()
        # Send the url via signal to the socket 
        #self.thread_loading.startThread(self.button_signal,BIAddr,self)
        self.button_signal.signal.emit(BIAddr)
        
 


    def previous_fi(self):

        self.ActualFIPage = self.ActualFIPage -1

        if(self.ActualFIPage == 1):
            self.fileft.setVisible(False)

        self.web_2.setStyleSheet('border-image: url(:/Imgs/'+ self.FItrim + str(self.ActualFIPage) +'.png);')

        if(not(self.firight.isVisible())):
            self.firight.setVisible(True)
            






    def next_fi(self):

        self.ActualFIPage = self.ActualFIPage +1

        if(self.ActualFIPage == self.FIPagesCount):
            self.firight.setVisible(False)
            

        self.web_2.setStyleSheet('border-image: url(:/Imgs/'+ self.FItrim + str(self.ActualFIPage) +'.png);')

        if(not(self.fileft.isVisible())):
            self.fileft.setVisible(True)

        

    def load_fi(self):
        self.web.setZoomFactor(1)
        self.Reset_Button.setVisible(False)
        self.firight.setVisible(False)
        self.fileft.setVisible(False)
  
        # Toggle the label on
        self.Toggle_Label(self.lbl_FI)
        # Loads the BI URL
        FIAddr = self.thread.API.load_FI(self.Station.Name) 


        

        self.web.setVisible(True)
        self.web_2.setVisible(False) 

        self.homepage.setVisible(False)
        self.controllers5sOFF()
        self.Toggle_textosOFF()
        # Send the url via signal to the socket 
        #self.thread_loading.startThread(self.button_signal,BIAddr,self)
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

class MainThread(QThread): #Thread de leitura dos crachás
    
    thread_signal = QtSignal()
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

            self.NonLogged_Window.mainthread_icon_off.setVisible(not(self.NonLogged_Window.mainthread_icon_off.isVisible()))
            self.Logged_Window.mainthread_icon.setVisible(not(self.Logged_Window.mainthread_icon.isVisible()))
            
            
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

                if (Actual_ID != Read_ID):
                    

                    try:
                        # Api call to login a user on OJT server
                        
                        logger.debug("Login user " + str(Read_ID) + "..........")
                        print("Login user " + str(Read_ID) + "..........")

                        LoginResponse = self.API.Request(self.API.OJT, "LoginByWorker", {'HostName': self.host, 'Badge': Read_ID});

                        # catch login status
                        status = LoginResponse['Status']

                    except Exception as e: 
                        traceback.print_exc()
                        logger.error("Login Error: " + type(e).__name__)
                        print(type(e).__name__)
                        status = ""
                    
                    # In case of succesfull login            
                    if(status=="Login realizado"):
                        
                        # Setup the Direct Labor object with actual worker data
                        self.DL.Setup(LoginResponse, self.host)
                        # Setup the user fields on the logged screen
                        self.Logged_Window.SetupUser(self.DL)
                        # The active ID is the newly logged ID               
                        Actual_ID = Read_ID
                        # Show the Logged screen and hide the initial screen
                        self.Logged_Window.Show()
                        self.NonLogged_Window.NonLogged_QtWindow.hide()


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
                        self.Logged_Window.TurnOFF_Label()
                        time.sleep(1)

                        
            # Wait for next thread iteration           
            time.sleep(self.thread_time) 



class GetWorkstationInfo(QThread):
 

    def run(self):

        contadorThread = 0
        
        while(self.status != 1):

            # if(contadorThread<10):
            print("Attempt to get Station info: " + str(contadorThread))

                
            self.status = self.Station.GetStationInfo(self.Raspberry.Name)

            # contadorThread = contadorThread + 1
            # else:
            #     command = 'echo b > sysrq'
                
            #     os.system(command)

            
            if(self.status != 1):
                time.sleep(30)

        self.Screen.Workstation_Signal.signal.emit(str(self.Station.Name))

        

        

    def startThread(self,Screen,Station,Raspberry):
        self.status = 0
        self.Screen = Screen
        self.Station = Station
        self.Raspberry = Raspberry
        self.start()


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
            self.Screen.web.reload()
            
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
