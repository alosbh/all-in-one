from PyQt5 import QtCore, QtGui, QtWidgets
import json
import requests
import sys

array_urls = ([])

class buttons_controller():

    def build_sidebar_buttons(self, hostname, workstation, route):
        try:
            array_buttons = ['LPA','FI', 'SCTC', 'Posto 5s', 'JIT suporte', 'Boas Ideias']

            self.define_icons()
            # array_buttons = []

            # # request active tags by hostname
            # url = 'http://brbelm0apps02/AIOService/Estation/GetTagByEquipment/' + workstation
            # request = requests.get(url, verify = False)
            # response = json.loads(request.content)

            # # if tag is active append to array
            # # if there is none active, a default array is created
            # for botao in response:
            #     if botao['IsActive'] == True:
            #         array_buttons.append(botao['Name'])

            if not array_buttons:
                array_buttons = ['LPA','FI', 'SCTC', 'Posto 5s', 'JIT suporte', 'Boas Ideias']

        except:
            print("erro")
            array_buttons = ['LPA','FI', 'SCTC', 'Posto 5s', 'JIT suporte', 'Boas Ideias']

        # workstations with stopwatcher fucntion
        print(array_buttons)
        # stopwatch_array = ['GEWBOXPSA001', 'GEWBOXPSA002', 'GEWBOXTBSUBM', 'GEWBOXPSC001', 'GEWBOXPSCLEAN', 'GEWBOXPSPACK']
        stopwatch_array = ['GE Wind', 'GE WIND CONVERTER', 'GE WIND Top Box']
        OR_monitor_array = ['INGCUSLIB001', 'INGCUSPAM001', 'INGCUSHOR001', 'INGCUSMIN001', 'INGCUSDIA001', 'INGCUSREW001']
        print("Linha: " + route)
        if route not in stopwatch_array:
            pass
        else:
            array_buttons.append('Stopwatcher')

        if workstation not in OR_monitor_array:
            pass
        else:
            array_buttons.append('OR Monitor')

        self.general_buttons()
        self.create_buttons(array_buttons)
    
    # iterate previous array to create buttons on the side bar
    def create_buttons(self, array):
        y_position = 12
        for button_name in array:
            y_position = y_position + 40
            if button_name == 'LPA':
                self.btn_lpa = QtWidgets.QPushButton(self.sidebar_apps)
                self.draw_buttons(self.btn_lpa, y_position)
                self.btn_lpa.setObjectName("btn_lpa")
                self.btn_lpa.setIcon(self.icon_LPA)
                self.btn_lpa.setText("   LPA")
                self.btn_lpa.clicked.connect(self.load_lpa)
            elif button_name == 'LPA Valinhos':
                self.btn_LPA_valinhos = QtWidgets.QPushButton(self.sidebar_apps)
                self.draw_buttons(self.btn_LPA_valinhos, y_position)
                self.btn_LPA_valinhos.setObjectName("btn_lpavalinhos")
                self.btn_LPA_valinhos.setIcon(self.icon_LPA)
                self.btn_LPA_valinhos.setText("   LPA Valinhos")
            elif button_name == 'SCTC':
                self.btn_SCTC = QtWidgets.QPushButton(self.sidebar_apps)
                self.draw_buttons(self.btn_SCTC, y_position)
                self.btn_SCTC.setObjectName("btn_SCTC")
                self.btn_SCTC.setIcon(self.icon_SCTC)
                self.btn_SCTC.setText("   Ferramentas SCTC")
                self.btn_SCTC.clicked.connect(self.jiga_list)
            elif button_name == 'OR Monitor':
                self.btn_OR = QtWidgets.QPushButton(self.sidebar_apps)
                self.draw_buttons(self.btn_OR, y_position)
                self.btn_OR.setObjectName("btn_OR")
                self.btn_OR.setIcon(self.icon_FI)
                self.btn_OR.setText("   OR Monitor")
                self.btn_OR.clicked.connect(self.load_ORMonitor)
            elif button_name == 'Boas Ideias':
                self.btn_goodideas = QtWidgets.QPushButton(self.sidebar_apps)
                self.draw_buttons(self.btn_goodideas, y_position)
                self.btn_goodideas.setObjectName("btn_goodideas")
                self.btn_goodideas.setIcon(self.icon_goodideas)
                self.btn_goodideas.setText("   Boas Ideias")
                self.btn_goodideas.clicked.connect(self.load_bi)
            elif button_name == 'FI':
                self.btn_instruction_sheet = QtWidgets.QPushButton(self.sidebar_apps)
                self.draw_buttons(self.btn_instruction_sheet, y_position)
                self.btn_instruction_sheet.setObjectName("btn_instruction_sheet")
                self.btn_instruction_sheet.setIcon(self.icon_FI)
                self.btn_instruction_sheet.setText("   Ficha de Instrução")
                self.btn_instruction_sheet.clicked.connect(self.load_fi)
            elif button_name == 'Posto 5s':
                self.btn_5s = QtWidgets.QPushButton(self.sidebar_apps)
                self.draw_buttons(self.btn_5s, y_position)
                self.btn_5s.setObjectName("btn_5s")
                self.btn_5s.setIcon(self.icon_5s)
                self.btn_5s.setText("   Posto Ideal 5s")
                self.btn_5s.clicked.connect(self.show5s)
            elif button_name == 'JIT suporte':
                self.btn_JIT = QtWidgets.QPushButton(self.sidebar_apps)
                self.draw_buttons(self.btn_JIT, y_position)
                self.btn_JIT.setObjectName("btn_JIT")
                self.btn_JIT.setIcon(self.icon_watch)
                self.btn_JIT.setText("   Suporte")
                self.btn_JIT.clicked.connect(self.suporte)
            elif button_name == 'Dashboard Reparo':
                self.btn_reparo = QtWidgets.QPushButton(self.sidebar_apps)
                self.draw_buttons(self.btn_reparo, y_position)
                self.btn_reparo.setObjectName("btn_reparo")
                self.btn_reparo.setIcon(self.icon_SCTC)
                self.btn_reparo.setText("   Dashboard Reparo")
            elif button_name == 'Stopwatcher':
                self.btn_stopwatcher = QtWidgets.QPushButton(self.sidebar_apps)
                self.draw_buttons(self.btn_stopwatcher, y_position)
                self.btn_stopwatcher.setObjectName("btn_stopwatcher")
                self.btn_stopwatcher.setIcon(self.icon_stopwatch)
                self.btn_stopwatcher.setText("     Stopwatcher")
                self.btn_stopwatcher.clicked.connect(self.load_stopwatcher)
    
    # creates slots for general buttons
    def general_buttons(self):
        self.btn_homepage.clicked.connect(self.home)
        self.btn_reset.clicked.connect(self.reset)
    
    # sets buttons stylesheet
    def draw_buttons(self, button, y_position):
        font = QtGui.QFont()
        font.setFamily("Inter UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        button.setFont(font)
        button.setGeometry(QtCore.QRect(0, y_position, 234, 41))
        button.setIconSize(QtCore.QSize(22, 22))
        button.raise_()

    # defines icons to be used in each button
    def define_icons(self):
        self.icon_LPA = QtGui.QIcon()
        self.icon_LPA.addPixmap(QtGui.QPixmap(":/Img/lista.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_SCTC = QtGui.QIcon()
        self.icon_SCTC.addPixmap(QtGui.QPixmap(":/Img/chave-inglesa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_goodideas = QtGui.QIcon()
        self.icon_goodideas.addPixmap(QtGui.QPixmap(":/Img/ideia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_FI = QtGui.QIcon()
        self.icon_FI.addPixmap(QtGui.QPixmap(":/Img/estrategia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_5s = QtGui.QIcon()
        self.icon_5s.addPixmap(QtGui.QPixmap(":/Img/posto-de-trabalho.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_watch = QtGui.QIcon()
        self.icon_watch.addPixmap(QtGui.QPixmap(":/Img/bxs-watch-alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_stopwatch = QtGui.QIcon()
        self.icon_stopwatch.addPixmap(QtGui.QPixmap(":/Img/stopwatch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
