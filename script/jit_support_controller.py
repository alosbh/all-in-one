from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread

import paho.mqtt.client as mqtt

from OS_define import OS_define
import string
import random
import requests
import json
import time
import sys
from ast import literal_eval
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 0 = received // 1 = sent // 2 = accepted // 3 = declined // 4 = ongoing // 5 = done
class jit_support_controller():
    def setup_support_screen(self, workstation_name):
        try:
            self.lbl_support_error.setVisible(False)
            self.workstation_name = workstation_name
            self.show_createticket_1()
            self.headers_update = {'content-type': 'application/json'}
            self.url_update = 'http://brbelm0apps99/JITAPI/Ticket/Update'

            self.setup_mqtt(workstation_name)
            self.support_screen_ui_functions(workstation_name)
            self.fill_cbx_teamssymptons(workstation_name)
            self.watchthread = WatchStatus()
            self.requestthread = ThreadCreateTicket()
            self.cancelthread = ThreadCancelTicket()
            self.initthread = ThreadInitTicket()
            self.endthread = ThreadEndTicket()
        except:
            self.btn_JIT.setText("   INDISPONIVEL")
            self.btn_JIT.clicked.disconnect()

    def support_screen_ui_functions(self, workstation_name):
        self.btn_createticket_create.clicked.connect(lambda: self.create_ticket(workstation_name))
        self.btn_close_error.clicked.connect(lambda: self.lbl_support_error.setVisible(False))
        self.btn_canceledticket_return.clicked.connect(self.show_createticket_1)
        self.btn_cancelticket_waiting.clicked.connect(self.cancel_ticket)
        self.btn_cancelticket_pending.clicked.connect(self.cancel_ticket)
        self.btn_cancelticket_inprogress.clicked.connect(self.cancel_ticket)
        self.btn_initiate_pending.clicked.connect(self.init_ticket)
        self.btn_initiate_inprogress.clicked.connect(self.finish_ticket)
        self.cbx_team_create.currentIndexChanged.connect(self.symptons_by_team)

    def raise_error_window(self):
        self.lbl_support_error.setVisible(True)
        self.lbl_support_error.raise_()
    
# creates and fills dictionaries with teams, symptons and it's ids - adds itens to the array that is used to fill comboboxes
    def fill_cbx_teamssymptons(self, workstation_name):
        self.team_teamid_dict = {}
        self.symptons_symptonid_dict = {}
        self.fill_cbx_dict = {}
        team_id_list = []

        try:
            request_team = requests.get(url = 'http://brbelm0apps99.corp.jabil.org/JITAPI/Team/GetAllActive', verify=False)
            response_team = request_team.json()
            request_symptons = requests.get(url = 'http://brbelm0apps99/JITAPI/Symptom/GetAll', verify=False)
            response_symptons = request_symptons.json()

            # cria dict q relaciona nome e id do time
            for x in response_team:
                self.team_teamid_dict.setdefault(x['name'], x['id'])

                # cria dict q relaciona nome e id do sintoma
                # cria dict q relaciona time e sintoma
                # captura id do time
                for y in response_symptons:
                    text = literal_eval(y['workstation'])
                    for z in text:
                        if z['text'] == workstation_name:
                            self.symptons_symptonid_dict.setdefault(y['description'],y['id'])
                            team_id_list.append(y['teamId'])
                            if y['teamId'] == x['id']:
                                self.fill_cbx_dict.setdefault(x['name'],[]).append(y['description'])

            team_id_list = list(set(team_id_list))

            # adiciona nome do time no cbx
            for team_info in response_team:
                for team_id in team_id_list:
                    if team_info['id'] == team_id:
                        self.cbx_team_create.addItem(team_info['name'])
        except:
            print('Posto sem sintomas cadastrados.')
                        
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
        self.show_loading()
        self.btn_createticket_create.setEnabled(False)
        
        
        if self.rbtn_going_create.isChecked():
            self.line_situation = '1' # ok line
        else:
            self.line_situation = '0' # stopped line

        self.team_id = self.team_teamid_dict.get(self.cbx_team_create.currentText())
        self.selected_sympton = self.cbx_sympton_create.currentText()
        self.symptom_id = self.symptons_symptonid_dict.get(self.selected_sympton)

        self.requestthread.startThread(self)

        self.btn_initiate_pending.setEnabled(True)
        self.btn_createticket_create.setEnabled(True)

# mqtt server functions
    def setup_mqtt(self, workstation_name):
        self.user = 'None'
        if OS_define.get_OS_name() == 1:
            letters = string.ascii_lowercase
            print ( ''.join(random.choice(letters) for i in range(10)) )
            client_name = ( ''.join(random.choice(letters) for i in range(10)) )

            print("Client MQTT: " + client_name)
            self.client = mqtt.Client(client_id = client_name,clean_session=False)
        else:
            
            self.client = mqtt.Client(client_id = workstation_name,clean_session=False)
        self.client.connect("BRBELM0MAT81.corp.jabil.org")
        self.client.on_message=self.on_message
        self.client.loop_start()

    def on_message(self, client, userdata, message):
        print("message received " ,str(message.payload.decode("utf-8")))
        
        print("topic received " ,str(message.topic))
        d = json.loads(message.payload)
        if(self.mqtt_topic==str(message.topic)):
            if (d["id"] == self.requestID):
                self.show_waiting_2()

                print("Esse é exatamente meu ticket")

       
        elif(self.mqtt_update==str(message.topic)):
        

            print("Eh topico de atualizar")
            
            self.user = d["UserName"]

            if (d["TicketId"] == self.requestID and d["Status"] == "Accepted"):
                url_getWatchbyUserID = 'http://brbelm0apps99/JITAPI/Smartwatch/GetbyUserId/' + str(d["userID"])
                request_getWatchIP = requests.get(url=url_getWatchbyUserID,verify=False)
                response_watchbyUserId = request_getWatchIP.json()
                mqtt_headers_update = {'content-type': 'application/json'}
                mqtt_url_update = 'http://brbelm0apps99/JITAPI/Ticket/Confirm'
                mqtt_postBody_update = {'ticketId': int(d["TicketId"]), 'ip': response_watchbyUserId['ip']}
                request_update = requests.post(mqtt_url_update, data=json.dumps(mqtt_postBody_update), headers=mqtt_headers_update)
                
                self.lbl_value_support_name_pending.setText(d["UserName"].split(' ', 1)[0])
                self.show_pending_3()
            
            elif (d["TicketId"] == self.requestID and d["Status"] == "OnGoing"):
                self.show_inprogress_4()
            elif (d["TicketId"] == self.requestID and d["Status"] == "Done"):
                self.show_createticket_1()
            elif (d["TicketId"] == self.requestID and d["Status"] == "Canceled") and d["UserName"] != "None":
                postBody_update = {'ticketStatus': 6, 'ticketId': int(self.requestID)}
                request_update = requests.post(self.url_update, data=json.dumps(postBody_update), headers=self.headers_update)
                self.lbl_value_canceledticket_name.setText(self.user)
                # self.show_canceledticket_5()
                self.show_createticket_1()
            elif (d["TicketId"] == self.requestID and d["Status"] == "Canceled") and d["UserName"] == "None":
                self.show_createticket_1()
                # self.show_canceledticket_5()
            else:
                self.lbl_value_canceledticket_name.setText(self.user)
                # self.show_createticket_1()

        print("message topic=",message.topic)
        print("message qos=",message.qos)
        print("message retain flag=",message.retain)

# update ticket status on the server side
    def init_ticket(self):

        self.show_loading()
        self.initthread.startThread(self)


    def finish_ticket(self):
        self.show_loading()
        self.endthread.startThread(self)


    def cancel_ticket(self):
        self.show_loading()

        self.cancelthread.startThread(self)

       

# screen control functions to avoid labels glitching
    
    def show_loading(self):
        self.subbody_loading_gif.show()
        self.subbody_canceledticket_5.hide()
        self.subbody_inprogress_4.hide()
        self.subbody_pending_3.hide()
        self.subbody_waiting_2.hide()
        self.subbody_createticket_1.hide()

    def show_createticket_1(self):
        self.subbody_loading_gif.hide()
        self.subbody_canceledticket_5.hide()
        self.subbody_inprogress_4.hide()
        self.subbody_pending_3.hide()
        self.subbody_waiting_2.hide()
        self.subbody_createticket_1.show()

    def show_waiting_2(self):
        self.subbody_loading_gif.hide()
        self.subbody_canceledticket_5.hide()
        self.subbody_inprogress_4.hide()
        self.subbody_pending_3.hide()
        self.subbody_waiting_2.show()
        self.subbody_createticket_1.hide()

    def show_pending_3(self):
        self.subbody_loading_gif.hide()
        self.subbody_canceledticket_5.hide()
        self.subbody_inprogress_4.hide()
        self.subbody_pending_3.show()
        self.subbody_waiting_2.hide()
        self.subbody_createticket_1.hide()

    def show_inprogress_4(self):
        self.subbody_loading_gif.hide()
        self.subbody_canceledticket_5.hide()
        self.subbody_inprogress_4.show()
        self.subbody_pending_3.hide()
        self.subbody_waiting_2.hide()
        self.subbody_createticket_1.hide()
    
    def show_canceledticket_5(self):
        self.subbody_loading_gif.hide()
        self.subbody_canceledticket_5.show()
        self.subbody_inprogress_4.hide()
        self.subbody_pending_3.hide()
        self.subbody_waiting_2.hide()
        self.subbody_createticket_1.hide()




class ThreadCancelTicket(QThread):

    def run(self):
        # requests.get("https://httpbin.org/delay/1")
        
        try:
            postBody_update = {'ticketStatus': 6, 'ticketId': int(self.body_support.requestID)}
            print(postBody_update)
            request_update = requests.post(self.body_support.url_update, data=json.dumps(postBody_update), headers=self.body_support.headers_update)
            if request_update.status_code == 200:
                updatemqtt = {'TicketId': self.body_support.requestID , 'UserName': 'None', 'Status': 'Canceled'}
                mqtt_string = json.dumps(updatemqtt)
                self.body_support.client.publish(self.body_support.mqtt_update, mqtt_string, qos=1)
                self.body_support.client.unsubscribe("atualizar/" + str(self.body_support.team_id))
            else:
                print("Erro cancelar:" + str(request_update.json()))
                self.body_support.show_createticket_1()
                # self.body_support.raise_error_window()
        except Exception as e:
            print (e)
            # self.body_support.raise_error_window()
            self.body_support.show_createticket_1()
        
    def startThread(self, body_support):
        print("BELEZA INICIEI A THREAD CANCELAR..........")
        self.body_support = body_support
        self.start()


class ThreadEndTicket(QThread):

    def run(self):
        # requests.get("https://httpbin.org/delay/1")
        
        try:
            postBody_update = {'ticketStatus': 5, 'ticketId': int(self.body_support.requestID)}
            print(postBody_update)
            request_update = requests.post(self.body_support.url_update, data=json.dumps(postBody_update), headers=self.body_support.headers_update)
            if request_update.status_code == 200:

                updatemqtt = {'TicketId': self.body_support.requestID , 'UserName': self.body_support.user, 'Status': 'Done'}
                mqtt_string = json.dumps(updatemqtt)
                self.body_support.client.publish(self.body_support.mqtt_update, mqtt_string, qos=1)
                self.body_support.client.unsubscribe("atualizar/" + str(self.body_support.team_id))
            else:
                print("Erro iniciar:" + str(request_update.json()))
                self.body_support.raise_error_window()
        except Exception as e:
            print (e)
            self.body_support.raise_error_window()
        
    def startThread(self, body_support):
        print("BELEZA INICIEI A THREAD FINALIZAR..........")
        self.body_support = body_support
        self.start()

class ThreadInitTicket(QThread):

    def run(self):
        # requests.get("https://httpbin.org/delay/1")
        
        try:
            postBody_update = {'ticketStatus': 4, 'ticketId': int(self.body_support.requestID)}
            print(postBody_update)
            request_update = requests.post(self.body_support.url_update, data=json.dumps(postBody_update), headers=self.body_support.headers_update)
            if request_update.status_code == 200:

                updatemqtt = {'TicketId': self.body_support.requestID , 'UserName': self.body_support.user, 'Status': 'OnGoing'}
                mqtt_string = json.dumps(updatemqtt)
                self.body_support.client.publish(self.body_support.mqtt_update, mqtt_string, qos=1)
                
            else:
                print("Erro iniciar:" + str(request_update.json()))
                self.body_support.raise_error_window()
        except Exception as e:
            print (e)
            self.body_support.raise_error_window()
        
    def startThread(self, body_support):
        print("BELEZA INICIEI A THREAD INICIAR..........")
        self.body_support = body_support
        self.start()


class ThreadCreateTicket(QThread):

    def run(self):
        
        # requests.get("https://httpbin.org/delay/1")
        
        #### REQUEST HTTP
        headers_create = {'content-type': 'application/json'}
        url_create = 'http://brbelm0apps99/JITAPI/Ticket/Create'
        
        try:
            postBody_create = {'productionLineStatus': self.body_support.line_situation,
            'workstationName': self.body_support.workstation_name,
            'teamId': self.body_support.team_id,
            'symptomId': self.body_support.symptom_id,
            'description': self.body_support.cbx_sympton_create.currentText()
            }
            request_create = requests.post(url_create, data=json.dumps(postBody_create), headers=headers_create)
            
            if request_create.status_code == 201:
                self.body_support.requestID = str(request_create.json()['id'])
                self.body_support.calltime = str(request_create.json()['receivedTime'])
                self.body_support.calltime = self.body_support.calltime[:-17]
                self.body_support.calltime = self.body_support.calltime[11:]
                
                payloadmqtt = {'id': self.body_support.requestID ,
                                'risk': self.body_support.line_situation,
                                'workstation': self.body_support.workstation_name,
                                'calltime': self.body_support.calltime,
                                'description': self.body_support.cbx_sympton_create.currentText()
                                }
                self.body_support.mqtt_string = json.dumps(payloadmqtt)
                self.body_support.mqtt_topic = "receber/"+ str(self.body_support.team_id)
                self.body_support.mqtt_update = "atualizar/"+ str(self.body_support.team_id)
                self.body_support.client.subscribe(self.body_support.mqtt_topic, qos=1)
                self.body_support.client.subscribe(self.body_support.mqtt_update, qos=1)
                self.body_support.client.publish(self.body_support.mqtt_topic, self.body_support.mqtt_string, qos=1)
                
                
                self.body_support.thread_ticket_status = 1
                # self.body_support.watchthread.startThread(self.body_support)
                # self.body_support.show_waiting_2()
            else:
                print(request_create)
                self.body_support.raise_error_window()
        except Exception as e:

            print (e)
            self.body_support.raise_error_window()
            
    def startThread(self, body_support):
        print("BELEZA INICIEI A THREAD..........")
        self.body_support = body_support
        


        self.start()
# thread for checking the ticket status
class WatchStatus(QThread):
 
    def run(self):
        while(self.body_support.thread_ticket_status == 1):

            # print("Status do Ticket")
            # print(str(self.body_support.thread_ticket_status))

            # print(self.url_thread)
            ticket_info_request = requests.get(self.url_thread)
            ticket_info_request = ticket_info_request.json()
            # print("Resposta da API")
            # print(ticket_info_request)
            
            if(ticket_info_request['status'] == "Accepted"):
                # a API retorna um array em formato de string (???)
                ticket_info_request = literal_eval(ticket_info_request['user'])
                ticket_info_request = ticket_info_request.pop()
                ticket_info_request = ticket_info_request['text']
                ticket_info_request = ticket_info_request.split(' ', 1)

                self.body_support.lbl_value_support_name_pending.setText(ticket_info_request[0])
                self.body_support.show_pending_3()

            elif ticket_info_request['status'] == "OnGoing":
                self.body_support.show_inprogress_4()
            elif ticket_info_request['status'] == "Done":
                self.body_support.show_createticket_1()
                return
            elif ticket_info_request['status'] == "Canceled":
                self.body_support.show_canceledticket_5()
                return

            time.sleep(2)

    def startThread(self, body_support):
        self.body_support = body_support
        self.url_thread = "http://brbelm0apps99/JITAPI/Ticket/GetById/" + self.body_support.requestID
        self.start()