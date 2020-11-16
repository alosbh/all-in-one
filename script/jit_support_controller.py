from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread
import requests
import json
import time
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class jit_support_controller():

    def support_screen_functions(self, workstation_name):
        # 0 = received // 1 = sent // 2 = accepted // 3 = declined // 4 = ongoing // 5 = done
        self.btn_createticket_create.clicked.connect(lambda: self.create_ticket(workstation_name))
        self.btn_cancelticket_waiting.clicked.connect(lambda: self.update_ticket_status(5))
        self.btn_cancelticket_pending.clicked.connect(lambda: self.update_ticket_status(5))
        self.btn_cancelticket_inprogress.clicked.connect(lambda: self.update_ticket_status(5))
        self.btn_initiate_pending.clicked.connect(lambda: self.update_ticket_status(4))
        self.btn_initiate_inprogress.clicked.connect(lambda: self.update_ticket_status(5))
        self.watchthread = WatchStatus()
        self.fill_cbx_teamssymptons()
    
    def fill_cbx_teamssymptons(self):
        # creates and fills dictionary teams and symptons, adds itens to the 'teams' combobox
        self.sympstons_dict = {}

        request_teamid = requests.get(url = 'http://brbelm0itqa01/JITAPI/Team/GetAllActive', verify=False)
        response_teamid = request_teamid.json()
        for x in response_teamid:
            self.cbx_team_create.addItem(x['name'])
            request_symptons_byteam = requests.get(url = 'http://brbelm0itqa01/JITAPI/Symptom/GetActiveByTeam/' + str(x['id']), verify=False)
            response_symptons_byteam = request_symptons_byteam.json()
            for y in response_symptons_byteam:
                if x['name'] in self.sympstons_dict:
                    self.sympstons_dict[x['name']].append(y['description'])
                else:
                    self.sympstons_dict[x['name']] = [y['description']]
        
        self.cbx_team_create.currentIndexChanged.connect(self.sympstons_by_team)

    def sympstons_by_team(self):
        self.cbx_sympton_create.clear()
        selected_team = self.cbx_team_create.currentText()
        try:
            for sympton in self.sympstons_dict[selected_team]:
                self.cbx_sympton_create.addItem(sympton)
        except:
            pass
    
# Watch server functions 
    def create_ticket(self, workstation_name):
        if self.rbtn_going_create.isChecked():
            self.line_situation = '1' # ok line
        else:
            self.line_situation = '0' # stopped line

        headers_create = {'content-type': 'application/json'}
        url_create = 'http://brbelm0itqa01/AioWatch/Create'
        postBody_create = {'workstationName': workstation_name, 'productionLineStatus': self.line_situation, 'description':self.cbx_sympton_create.currentText()}
        request_create = requests.post(url_create, data=json.dumps(postBody_create), headers=headers_create)
        self.requestID = str(request_create.json()['additionalData']['id'])

        self.thread_ticket_status = 1
        self.watchthread.startThread(self)

        self.subbody_waiting_2.raise_()
    
    def update_ticket_status(self, status):
        # request updates the ticket status on the server side
        headers_update = {'content-type': 'application/json'}
        url_update = 'http://brbelm0itqa01/AioWatch/Update'
        postBody_update = {'id': self.requestID,'ticketStatus': status}
        request_update = requests.post(url_update, data=json.dumps(postBody_update), headers=headers_update)

# thread for checking the ticket status
class WatchStatus(QThread):
 
    def run(self):

        while(self.body_support.thread_ticket_status == 1):
            getrequest = requests.get(self.url_thread)
            
            if(getrequest.json()['additionalData']['status'] == "Accepted"):
                self.body_support.subbody_pending_3.raise_()
                self.body_support.lbl_value_support_name_pending.setText(getrequest.json()['additionalData']['userName'])
            elif(getrequest.json()['additionalData']['status'] == "OnGoing"):
                self.body_support.subbody_inprogress_4.raise_()
            elif(getrequest.json()['additionalData']['status'] == "Done"):
                self.body_support.subbody_createticket_1.raise_()

            time.sleep(4)

    def startThread(self, body_support):
        self.body_support = body_support
        self.url_thread = "http://brbelm0itqa01/AioWatch/GetById?id=" + self.body_support.requestID
        self.start()