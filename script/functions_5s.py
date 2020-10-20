from ScreenManagement import Logged_Screen

class functions_5():

    def __init__(self, *args, **kwargs):
        self.Logged_Screen = Logged_Screen()

    def show5s(self):
        self.body_home.setVisible(False) #))homepage
        self.body_web.setVisible(True)
        self.obj5s = self.thread.API.load5s('orig')

        if(self.obj5s != None):
            self.contador = len(self.obj5s)-1
            self.state5s=0
            url = str(self.obj5s[self.state5s]['Path'])
            #url = self.obj5s[self.state5s]
            # if(self.contador>0):
                # self.lbl_value_5s_total.setText(str(self.contador+1))
                # self.lbl_value_5s_actual.setText("1")
                # self.controllers5sON()
        else:
            url = 'http://brbelm0itqa01/AIOService/Images5S/NaoEncontrado.png'
            
        self.load_url_signal.signal.emit(url)
    
    def controllers5sON(self):
        #self.lbl_value_5s_total.setVisible(True)
        #self.lbl_value_5s_actual.setVisible(True)
        #self.lbl_5sbar.setVisible(True)
        self.Logged_Screen.btn_5s_back.setVisible(True)
        self.Logged_Screen.btn_5s_next.setVisible(True)

    def controllers5sOFF(self):
        #self.lbl_value_5s_total.setVisible(False)
        #self.lbl_value_5s_actual.setVisible(False)
        #self.lbl_5sbar.setVisible(False)
        self.btn_5s_next.setVisible(False)
        self.btn_5s_back.setVisible(False)
        
    #goes foward in the 5s menu
    def proxpage(self):
        self.state5s = self.state5s+1
        self.btn_5s_back.setVisible(True)
        self.lbl_value_5s_actual.setText(str(self.state5s+1))
        
        if(self.state5s==self.contador):
            self.btn_5s_next.setVisible(False)
            
        url = str(self.obj5s[self.state5s]['Path'])
        self.load_url_signal.signal.emit(url)

    #goes backward in the 5s menu
    def antpage(self):
        self.state5s = self.state5s-1
        self.btn_5s_next.setVisible(True)
        self.lbl_value_5s_actual.setText(str(self.state5s+1))
        
        if(self.state5s==0):
            self.btn_5s_back.setVisible(False)
            
        url = str(self.obj5s[self.state5s]['Path'])
        self.load_url_signal.signal.emit(url)