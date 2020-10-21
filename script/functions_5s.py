from PyQt5 import QtWidgets, QtCore
from Station import Station

class functions_5s():



    def generate_5s(self, workstation_name):
        self.dots_list = []
        # self.workstation_name = workstation_name
        self.workstation_name = "INGSCR001"
        self.create_dots_5s()
        self.btn_5s_back.raise_()
        self.btn_5s_next.raise_()
        self.horizontalWidget_3.raise_()
        self.btn_5s_next.clicked.connect(self.proxpage)
        self.btn_5s_back.clicked.connect(self.antpage)
        self.hide5s()

    def hide5s(self):
        self.horizontalWidget_3.setVisible(False)
        self.btn_5s_next.setVisible(False)
        self.btn_5s_back.setVisible(False)

    def show5s(self):
        self.body_home.setVisible(False)
        self.body_web.setVisible(True)
        self.load_5s_page()

    def load_5s_page(self):
        self.obj5s = self.thread.API.load_5s(self.workstation_name)

        if(self.obj5s != None):
            self.contador = len(self.obj5s)-1
            self.state5s=0
            self.dots_list[0].setStyleSheet("background-color:rgba(82,82,238,1);\n""border-radius:10px;\n""\n""")
            url = str(self.obj5s[self.state5s]['Path'])
            if(self.contador>0):
                self.horizontalWidget_3.setVisible(True)
                self.btn_5s_next.setVisible(True)
        else:
            url = 'http://brbelm0itqa01/AIOService/Images5S/NaoEncontrado.png'

        self.load_url_signal.signal.emit(url)

    #creates 5s dots widgets
    def create_dots_5s(self):
        self.obj5s = self.thread.API.load_5s(self.workstation_name)

        if(self.obj5s != None):
            self.dots = len(self.obj5s)
            
        for x in range(self.dots):
            self.lbl_5s_dot = QtWidgets.QLabel(self.horizontalWidget_3)
            self.lbl_5s_dot.setMinimumSize(QtCore.QSize(20, 20))
            self.lbl_5s_dot.setMaximumSize(QtCore.QSize(20, 20))
            self.lbl_5s_dot.setStyleSheet("background-color:rgba(82,82,238,0.15);\n""border-radius:10px;\n""\n""")
            self.lbl_5s_dot.setText("")
            self.lbl_5s_dot.setObjectName("lbl_5s_dot1")
            self.dots_list.append(self.lbl_5s_dot)
            self.layout_5s_dots.addWidget(self.dots_list[x])
        
    #goes foward in the 5s menu
    def proxpage(self):
        self.state5s = self.state5s+1
        self.btn_5s_back.setVisible(True)
        
        
        self.dots_list[self.state5s].setStyleSheet("background-color:rgba(82,82,238,1);\n""border-radius:10px;\n""\n""")
        self.dots_list[self.state5s-1].setStyleSheet("background-color:rgba(82,82,238,0.15);\n""border-radius:10px;\n""\n""")

        if(self.state5s==self.contador):
            self.btn_5s_next.setVisible(False)
            
        url = str(self.obj5s[self.state5s]['Path'])
        self.load_url_signal.signal.emit(url)

    #goes backward in the 5s menu
    def antpage(self):
        self.state5s = self.state5s-1
        self.btn_5s_next.setVisible(True)
        
        self.dots_list[self.state5s].setStyleSheet("background-color:rgba(82,82,238,1);\n""border-radius:10px;\n""\n""")
        self.dots_list[self.state5s+1].setStyleSheet("background-color:rgba(82,82,238,0.15);\n""border-radius:10px;\n""\n""")

        if(self.state5s==0):
            self.btn_5s_back.setVisible(False)
            
        url = str(self.obj5s[self.state5s]['Path'])
        self.load_url_signal.signal.emit(url)