from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread
import requests
import json
import time
import sys
from ast import literal_eval
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 0 = received // 1 = sent // 2 = accepted // 3 = declined // 4 = ongoing // 5 = done
class jit_support_controller():

    def support_screen_functions(self, workstation_name):
        self.btn_createticket_create.clicked.connect(lambda: self.create_ticket(workstation_name))
        self.btn_close_error.clicked.connect(lambda: self.lbl_support_error.setVisible(False))
        self.btn_cancelticket_waiting.clicked.connect(lambda: self.update_ticket_status(5))
        self.btn_cancelticket_pending.clicked.connect(lambda: self.update_ticket_status(5))
        self.btn_cancelticket_inprogress.clicked.connect(lambda: self.update_ticket_status(5))
        self.btn_initiate_pending.clicked.connect(lambda: self.update_ticket_status(4))
        self.btn_initiate_inprogress.clicked.connect(lambda: self.update_ticket_status(5))
        self.cbx_team_create.currentIndexChanged.connect(self.symptons_by_team)
        # self.watchthread = WatchStatus()
        # self.fill_cbx_teamssymptons(workstation_name)
    
# creates and fills dictionaries with teams, symptons and it's ids - adds itens to the array that is used to fill comboboxes
    def fill_cbx_teamssymptons(self, workstation_name):
        self.team_teamid_dict = {}
        self.symptons_symptonid_dict = {}
        self.fill_cbx_dict = {}

        request_teamid = requests.get(url = 'http://brbelm0itqa01/JITAPI/Team/GetAllActive', verify=False)
        response_teamid = request_teamid.json()

        for x in response_teamid:
            self.team_teamid_dict.setdefault(x['name'], x['id'])

            request_symptons_byteam = requests.get(url = 'http://brbelm0itqa01/JITAPI/Symptom/GetActiveByTeam/' + str(x['id']), verify=False)
            response_symptons_byteam = request_symptons_byteam.json()

            for y in response_symptons_byteam:
                # a API retorna um array em formato de string (???)
                return_workstation = literal_eval(y['workstation'])
                for z in return_workstation:
                    if z['text'] == workstation_name:
                        self.symptons_symptonid_dict.setdefault(y['description'],y['id'])
                        self.fill_cbx_dict.setdefault(x['name'],[]).append(y['description'])
        
        for team in self.fill_cbx_dict:
            self.cbx_team_create.addItem(team)
                        
# fills comboboxes with symptons and teams
    def symptons_by_team(self):
        self.cbx_sympton_create.clear()
        selected_team = self.cbx_team_create.currentText()

        try:
            for sympton in self.fill_cbx_dict[selected_team]:
                self.cbx_sympton_create.addItem(sympton)
        except:
            pass

# Watch server functions 
    def create_ticket(self, workstation_name):
        self.btn_initiate_pending.setEnabled(True)
        self.btn_createticket_create.setEnabled(False)
        if self.rbtn_going_create.isChecked():
            self.line_situation = '1' # ok line
        else:
            self.line_situation = '0' # stopped line
        
        headers_create = {'content-type': 'application/json'}
        url_create = 'http://brbelm0itqa01/JITAPI/Ticket/Create'
        
        self.team_id = self.team_teamid_dict.get(self.cbx_team_create.currentText())
        self.selected_sympton = self.cbx_sympton_create.currentText()
        self.symptom_id = self.symptons_symptonid_dict.get(self.selected_sympton)

        try:
            postBody_create = {'productionLineStatus': self.line_situation,
            'workstationName': workstation_name,
            'teamId': self.team_id,
            'symptomId': self.symptom_id,
            'description': self.cbx_sympton_create.currentText()
            }
            request_create = requests.post(url_create, data=json.dumps(postBody_create), headers=headers_create)

            if request_create.status_code == 201:
                self.requestID = str(request_create.json()['id'])
                self.thread_ticket_status = 1
                self.watchthread.startThread(self)
                self.subbody_waiting_2.raise_()
            else:
                self.raise_error_window()
        except:
            self.raise_error_window()
            
        time.sleep(2)
        self.btn_createticket_create.setEnabled(True)
    
# request updates the ticket status on the server side
    def update_ticket_status(self, status):
        if status == 4:
            self.btn_initiate_pending.setEnabled(False)
        headers_update = {'content-type': 'application/json'}
        url_update = 'http://brbelm0itqa01/JITAPI/Ticket/Update'
        postBody_update = {'ticketStatus': status, 'ticketId': int(self.requestID)}
        request_update = requests.post(url_update, data=json.dumps(postBody_update), headers=headers_update)

    def raise_error_window(self):
        self.lbl_support_error.setVisible(True)
        self.lbl_support_error.raise_()

# thread for checking the ticket status
class WatchStatus(QThread):
 
    def run(self):
        while(self.body_support.thread_ticket_status == 1):
            ticket_info_request = requests.get(self.url_thread)
            ticket_info_request = ticket_info_request.json()
            
            if(ticket_info_request['status'] == "Accepted"):
                # a API retorna um array em formato de string (???)
                ticket_info_request = literal_eval(ticket_info_request['user'])
                ticket_info_request = ticket_info_request.pop()
                ticket_info_request = ticket_info_request['text']
                ticket_info_request = ticket_info_request.split(' ', 1)

                self.body_support.lbl_value_support_name_pending.setText(ticket_info_request[0])
                self.body_support.subbody_pending_3.raise_()

            elif(ticket_info_request['status'] == "OnGoing"):
                self.body_support.subbody_inprogress_4.raise_()
            elif(ticket_info_request['status'] == "Done"):
                self.body_support.subbody_createticket_1.raise_()
                return

            time.sleep(2)

    def startThread(self, body_support):
        self.body_support = body_support
        self.url_thread = "http://brbelm0itqa01/JITAPI/Ticket/GetById/" + self.body_support.requestID
        self.start()