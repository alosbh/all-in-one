from PyQt5.QtCore import QObject, pyqtSignal, QUrl, QThread
from GlobalParameters import GlobalParameters
from ApiManager import ApiManager as ws
from DirectLabor import DirectLabor as DL
from OS_define import OS_define
OS_define = OS_define()
if OS_define.get_OS_name() == 1:
    pass
else:
    from RFRead_controller import RFRead_controller
import logging
import time
import requests
import json

GlobalParameters = GlobalParameters()

class QtSignal(QObject):
        signal = pyqtSignal(str)

#Thread for badge reading
class Login_controller(QThread):
    
    thread_signal = QtSignal()
    thread_signal2 = QtSignal()
    #abcd_signal = QtSignal()
    
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
        self.API = ws()
        self.DL = DL()
        self.NonLogged_Window = None
        self.Logged_Window = None

    # def get_flag():
    #     flag = Fpl_controller.get_flag()
    #     return flag

    def set_flag(onoff):
        global flag
        flag = onoff

    def run(self):
        # Logged Badge ID
        # global self.Actual_ID
        self.Actual_ID = None
        # New Badge ID read from the RF module
        # global self.Read_ID
        #Starts logount counter, so the user will be disconnected after reaching the limit of NULL readings
        cont_logout = 0
        status_workstation = self.NonLogged_Window.Station.Enabled
        
        logger=logging.getLogger() 
        logger.setLevel(logging.DEBUG)
        Login_controller.set_flag(True)

        while True:
            if flag == True:
                try:
                    if OS_define.get_OS_name() == 1:
                        self.Read_ID = 51008294
                    else:
                        self.Read_ID = RFRead_controller.RFRead() # Reads Badge ID
                except Exception as e:
                    traceback.print_exc()
                    logger.error("RFID error: " + type(e).__name__)
                    print(type(e).__name__)
                    self.Read_ID = None
                    self.NonLogged_Window.nome_posto.setText(str('Erro leitura RFID'))

                if (self.Read_ID != None and self.NonLogged_Window.Station.Enabled == 1 ): 
                    cont_logout = 0

                    # If the read id is not null, compares it to the active user. In case its different, login the new user. 
                    if (self.Actual_ID != self.Read_ID):
                        try:
                            # Api call to login a user on OJT server
                            logger.debug("Login user " + str(self.Read_ID) + "..........")
                            LoginResponse = requests.post(url='http://brbelm0apps99/RaspLoginAPI/Authentication/LoginByWorker',data={'HostName': self.host, 'Badge': self.Read_ID})
                            LoginResponse = json.loads(LoginResponse.content) 
                            # catch login status
                            status = LoginResponse['Status']
                            # status="Login realizado"
                            print("Stats1:"+status)

                        except Exception as e: 
                            logger.error("Login Error: " + type(e).__name__)
                            print(type(e).__name__)
                            status = ""

                        print("Stats2:"+status)
                        # In case of succesfull login            
                        if(status=="Login realizado"):
                            self.thread_signal2.signal.emit('about:blank')
                            self.Logged_Window.home()
                            self.Logged_Window.preload_screen()
                            self.thread_signal2.signal.emit('about:blank')
                            # Setup the Direct Labor object with actual worker data
                            self.DL.Setup(LoginResponse, self.host)
                            self.DL.load_avatar()
                            # Setup the user fields on the logged screen
                            self.Logged_Window.SetupUser(self.DL)
                            # The active ID is the newly logged ID               
                            self.Actual_ID = self.Read_ID
                            print("Actual ID apos alterar: " + str(self.Actual_ID))
                            # Show the Logged screen and hide the initial screen
                            # self.Logged_Window.Logged_QtWindow.show()
                            # self.NonLogged_Window.NonLogged_QtWindow.hide()


                else: 
                    cont_logout += 1 

                    #if the null reads has reached the limit and there is someone logged
                    if (cont_logout >= self.logout_limit):
                        cont_logout = self.logout_limit
                        if (self.Actual_ID != None):

                            try:
                                # API Call to logout the user
                                print("Logout user " + self.Actual_ID + ".........")
                                logger.debug("Logout user " + self.Actual_ID + ".........")
                                LogoutResponse = requests.post(url='http://brbelm0apps99/RaspLoginAPI/Authentication/Logout',data={'HostName': self.host, 'Badge': self.Read_ID}) 
                                LogoutResponse = json.loads(LogoutResponse.content) 
                                status = LogoutResponse['Status']

                                if((status=="Logout realizado")or (status=="Não encontrado")):
                                    # Show home screen
                                    self.NonLogged_Window.Show() 
                                    #Hide the logged screen
                                    self.Logged_Window.Logged_QtWindow.hide()
                                    self.Actual_ID = None
                                    self.Logged_Window.home()

                            except Exception as e:
                                print("Couldnt do logout. Error: " + type(e).__name__)
                                logger.error("Couldnt do logout. Error: " + type(e).__name__)    


                            # Clear the webviewer on the logged screen
                            self.thread_signal.signal.emit('about:blank')
                            time.sleep(1)

                # Wait for next thread iteration           
                time.sleep(self.thread_time) 
            else:         
                time.sleep(self.thread_time)