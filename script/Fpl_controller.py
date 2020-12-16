from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QUrl, QThread
from Login_controller import Login_controller
from DirectLabor import DirectLabor as DL
from OS_define import OS_define
OS_define = OS_define()
if OS_define.get_OS_name() == 1:
    pass
else:
    from RFRead_controller import RFRead_controller
import requests
import json
import time
import sys

class Fpl_controller():
    def setup_fpl(self, DLname, DLid):
        global DL_Name
        DL_Name = DLname
        self.DLid = DLid
        self.thread_vt = thread_vt()
        self.body_FPL.hide()
        self.body_FPL_error.hide()
        self.get_all_documents(1)
        
# pega info dos documentos e adiciona em arrays para gerar widgets na janela
    def get_all_documents(self, flag):
        self.valid_documents_dict = {}
        self.invalid_documents_dict = {}

        physicalWorkstationId = str(self.Station.Id)
        traineeRegistration = str(self.DLid)
        url_alldocs = 'http://brbelm0mat81/ojt/api/Trainings?physicalWorkstationId='+ physicalWorkstationId +'&traineeRegistration=' + traineeRegistration
        print(url_alldocs)
        request_alldocs = requests.get(url_alldocs)
        
        print(request_alldocs.status_code)
        if request_alldocs.status_code == 200:
            i = 0
            response_alldocs = request_alldocs.json()
            response_alldocs = response_alldocs['documents']
            for document in response_alldocs:
                if document['isTrained'] == True:
                    self.valid_documents_dict.setdefault(document['infoCardNumber'],document['infoCardId'])
                else:
                    i += 1
                    self.invalid_documents_dict.setdefault(document['infoCardNumber'],document['infoCardId'])
            if not self.invalid_documents_dict:
                self.btn_validate_training.hide()
                self.lbl_ok_FPL_00.show()
                self.lbl_ok_FPL_00.raise_()
                self.lbl_invalid_trainings.hide()
                self.lbl_value_number_invalidFPL.hide()
                print('blue')
                self.set_blue()
            else:
                self.btn_validate_training.show()
                self.lbl_nok_FPL_01.raise_()
                self.lbl_ok_FPL_00.hide()
                self.lbl_invalid_trainings.show()
                self.lbl_value_number_invalidFPL.show()
                print('red')
                self.set_red()

            self.lbl_value_number_invalidFPL.setText(str(i))
            self.create_lbl_ckb()
            
            if flag == 1:
                self.fpl_btn_functions()
        else:
            print('erro')
            self.set_blue()
            self.error_FPL()

    def fpl_btn_functions(self):
        self.btn_FPL.clicked.connect(self.body_FPL.show)
        self.btn_close_FPL.clicked.connect(self.body_FPL.hide)
        self.btn_validate_training.clicked.connect(self.show_validate_window)
        self.btn_proceed_startvalidation.clicked.connect(self.validate_training)
        self.btn_ok_successvalidation.clicked.connect(self.turnon_loginlogout)
        self.btn_return_fail.clicked.connect(self.fail_return)

# metodos de controle de tela
    def fail_return(self):
        self.lbl_nok_FPL_01.raise_()
        Login_controller.set_flag(True)
        
    def show_validate_window(self):
        self.lbl_startvalidation_FPL_02.show()
        self.lbl_startvalidation_FPL_02.raise_()
    
    def error_FPL(self):
        self.body_FPL.hide()
        self.lbl_value_number_invalidFPL.hide()
        self.btn_FPL.clicked.connect(self.body_FPL_error.show)
        self.btn_close_FPL_error.clicked.connect(self.body_FPL_error.hide)

# manipula labels e checkboxes
    def create_lbl_ckb(self):
        self.ckb_docname = {}
        self.array_ckb_FPL = [self.ckb_FPL_0, self.ckb_FPL_1, self.ckb_FPL_2, self.ckb_FPL_3, self.ckb_FPL_4, self.ckb_FPL_5, self.ckb_FPL_6, self.ckb_FPL_7]
        self.array_lbl_FPL = [self.lbl_FPL_0, self.lbl_FPL_1, self.lbl_FPL_2, self.lbl_FPL_3, self.lbl_FPL_4, self.lbl_FPL_5, self.lbl_FPL_6, self.lbl_FPL_7]
        self.array_btn_ckb_FPL = [self.btn_ckb_FPL_0, self.btn_ckb_FPL_1, self.btn_ckb_FPL_2, self.btn_ckb_FPL_3, self.btn_ckb_FPL_4, self.btn_ckb_FPL_5, self.btn_ckb_FPL_6, self.btn_ckb_FPL_7]
        self.array_btn_lbl_FPL = [self.btn_lbl_FPL_0, self.btn_lbl_FPL_1, self.btn_lbl_FPL_2, self.btn_lbl_FPL_3, self.btn_lbl_FPL_4, self.btn_lbl_FPL_5, self.btn_lbl_FPL_6, self.btn_lbl_FPL_7]
        i = 0
        j = 0

        # muda nomes dos lbls e ckbs
        for document in self.invalid_documents_dict:
            self.ckb_docname.setdefault(self.array_ckb_FPL[i], self.invalid_documents_dict[document])
            self.array_ckb_FPL[i].setText(document)
            self.array_ckb_FPL[i].show()
            i += 1
        for document in self.valid_documents_dict:
            self.array_lbl_FPL[j].setText(document)
            self.array_lbl_FPL[j].show()
            j += 1

        # esconde os lbls, ckbs e btns sem uso
        for ckb in range(8 - i):
            self.array_ckb_FPL[i].hide()
            self.array_btn_ckb_FPL[i].hide()
            i += 1
        
        for lbl in range(8 - j):
            self.array_lbl_FPL[j].hide()
            self.array_btn_lbl_FPL[j].hide()
            j += 1
    
# coemeca a thread para leitura do cracha e confirmacao - desliga o loop que mantem login e logout ativo
    def validate_training(self):
        if self.thread_vt.isRunning() == False:
            self.btn_proceed_startvalidation.setEnabled(False)
            self.ckb_checked_status()
            Login_controller.set_flag(False)
            self.thread_vt.vt.connect(self.update_window)
            self.thread_vt.start_thread(1)

# liga o loop que mantem login e logout ativo
    def turnon_loginlogout(self):
        self.thread_vt.start_thread(2)

# se ckbx estiver marcado adiciona a um array que vai ser usado no request que valida documentos
    def ckb_checked_status(self):
        global docarray
        self.validated_doc = []
        for ckb in self.ckb_docname:
            if ckb.isChecked():
                self.validated_doc.append(self.ckb_docname[ckb])
        docarray = self.validated_doc

# metodos para passar variaveis pra thread
    def get_docarray():
        return docarray
    
    def get_dlname():
        return DL_Name

# decide qual janela vai subir
    def update_window(self, window):
        self.btn_proceed_startvalidation.setEnabled(True)
        if window == 'success':
            self.lbl_successvalidation_FPL_03.show()
            self.lbl_successvalidation_FPL_03.raise_()
        elif window == 'fail':
            self.lbl_failvalidation_FPL_04.show()
            self.lbl_failvalidation_FPL_04.raise_()
        elif window == 'logout':
            Login_controller.set_flag(True)
            self.get_all_documents(2)
            self.body_FPL.hide()

# pega o cracha no leitor(dl) no momento do clique. quando mudar, pega o que foi inserido(responsavel) e faz o request de validacao. depois liga o login/logout novamente
class thread_vt(QThread):
    vt = QtCore.pyqtSignal(str)
    
    def run(self):
        if OS_define.get_OS_name() == 0:
            for attempts in range(20):
                read = RFRead_controller.RFRead()
                if attempts == 0:
                    first_read = read

                if attempts == 19:
                    print('fail')
                    self.vt.emit('fail')
                    return

                if read != first_read and read != None:
                    if self.whatdo == 1:
                        try:
                            docarray = Fpl_controller.get_docarray()
                            dlname = Fpl_controller.get_dlname()
                            url_validatedocs = 'http://brbelm0mat81/ojt/ojt-service/trainings'
                            headers_validate = {'content-type': 'application/json'}
                            body_validate = {'TraineeName': dlname,
                            'traineeRegistration': first_read[1:],
                            'trainerRegistration': read[1:],
                            'documentInfoCardIds': docarray}
                            request_validatedocs = requests.post(url_validatedocs, data=json.dumps(body_validate), headers=headers_validate)
                            print(body_validate)
                            print(request_validatedocs)

                            if request_validatedocs.status_code == 201:
                                self.vt.emit('success')
                                return
                            else:
                                self.vt.emit('fail')
                                return
                        except:
                            self.vt.emit('fail')
                            return
                    elif self.whatdo == 2:
                        self.vt.emit('logout')
                        return
                time.sleep(0.5)
        
    def start_thread(self, whatdo):
        self.whatdo = whatdo
        self.start()










# JEITO CERTO DE FAZER MAS QUE NAO DA CERTO POR ENQUANTO - DEIXA AQUI
# # criar labels, checkbox e botoes para todos os documentos nos arrays criados anteriormente
#     def create_lbl_ckb(self):
#         self.ckb_docname = {}

#         font = QtGui.QFont()
#         _translate = QtCore.QCoreApplication.translate
#         font.setFamily("Inter UI")
#         font.setPointSize(10)
#         font.setBold(False)
#         font.setWeight(50)

#         # cria widgets para documentos nao validados
#         for document in self.invalid_documents_dict:
#             self.ckb_docvalue_FPL = QtWidgets.QCheckBox(self.verticalLayoutWidget)
#             self.ckb_docvalue_FPL.setStyleSheet("background-color: rgb(255, 255, 255);\n""border-color: white")
#             self.ckb_docvalue_FPL.setObjectName("ckb_docvalue_FPL")
#             self.ckb_docvalue_FPL.setText(_translate("MainWindow", document))
#             self.layout_OJT_docnames.addWidget(self.ckb_docvalue_FPL)
#             self.ckb_docname.setdefault(self.ckb_docvalue_FPL, self.invalid_documents_dict[document])
#             # # --cria button blablabla--
#             # self.layout_OJT_redirectbtns.addWidget()
#             # self.button.clicked.connect(lambda: self.load_OJT(self.invalid_documents_dict[document]))

#         # cria widgets para documentos validos
#         for document in self.valid_documents_dict:
#             self.lbl_docvalue_FPL = QtWidgets.QLabel(self.verticalLayoutWidget)
#             self.lbl_docvalue_FPL.setStyleSheet("background-color: rgb(255, 255, 255);\n""border-color: white")
#             self.lbl_docvalue_FPL.setObjectName("lbl_docvalue_FPL")
#             self.lbl_docvalue_FPL.setText(_translate("MainWindow", document))
#             self.layout_OJT_docnames.addWidget(self.lbl_docvalue_FPL)
#             # # --cria button blablabla--
#             # self.layout_OJT_redirectbtns.addWidget()
#             # self.button.clicked.connect(lambda: self.load_OJT(self.valid_documents_dict[document]))

#         # manda os lbls e ckbx para cima
#         spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#         self.layout_OJT_docnames.addItem(spacerItem)