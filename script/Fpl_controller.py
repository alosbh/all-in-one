from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QUrl, QThread
from RFRead_controller import RFRead_controller
from Login_controller import Login_controller
import requests
import json
import time

class Fpl_controller():
    def fpl_btn_functions(self):
        self.btn_close_FPL.clicked.connect(lambda: self.body_FPL.setVisible(False))
        self.btn_close_startvalidation.clicked.connect(lambda: self.lbl_startvalidation_FPL_02.setVisible(False))
        self.btn_validate_training.clicked.connect(self.show_validate_window)
        self.btn_proceed_startvalidation.clicked.connect(self.validate_training)
        self.btn_ok_successvalidation.clicked.connect(self.turnon_login)

    def show_validate_window(self):
        self.lbl_startvalidation_FPL_02.setVisible(True)
        self.lbl_startvalidation_FPL_02.raise_()
        

# pega info dos documentos
#     def get_all_documents(self):
#         # request

#         for document in request:
#             if document['valid'] == 1:
#                 self.valid_documents_dict.setdefault(document['name'],document['url'])
#             else:
#                 self.invalid_documents_dict.setdefault(document['name'],document['url'])

#         if range(self.invalid_documents_dict) > 0:
#             self.btn_validate_training.setVisible(True)
#             self.lbl_allgood.setVisible(False)
#             self.lbl_invalid_trainings.setVisible(True)
#         else:
#             self.btn_validate_training.setVisible(False)
#             self.lbl_allgood.setVisible(True)
#             self.lbl_invalid_trainings.setVisible(False)

#         self.btn_close_OJT.clicked(self.body_FPL.setVisible(False))
#         self.btn_validate_training(self.validate_training)
#         self.create_lbl_ckb()

#     def create_lbl_ckb(self):
#         font = QtGui.QFont()
#         font.setFamily("Inter UI")
#         font.setPointSize(10)
#         font.setBold(False)
#         font.setWeight(50)

#         # cria ckbx para documentos não validados e botões de redirecionamento
#         for document in self.invalid_documents_dict
#             # --cria checkbox blablabla--
#             self.layout_OJT_docnames.addWidget()
#             self.ckb_docname.setdefault(self.ckb, document)

#             # --cria button blablabla--
#             self.layout_OJT_redirectbtns.addWidget()
#             self.button.clicked.connect(lambda: self.load_OJT(self.invalid_documents_dict[document]))

#         # cria lbls para documentos validos e botões de redirecionamento
#         for document in self.valid_documents_dict
#             # --cria label blablabla--
#             self.layout_OJT_docnames.addWidget()

#             # --cria button blablabla--
#             self.layout_OJT_redirectbtns.addWidget()
#             self.button.clicked.connect(lambda: self.load_OJT(self.valid_documents_dict[document]))
    
# # checa todos os documentos invalidos, se ckbx estiver marcado adiciona a um array que vai ser usado pra um request que valida documentos
#     def ckb_checked_status(self, ckb_number):
#         for ckb in self.ckb_docname:
#             if ckb.isChecked():
#                 validated_doc.append(self.ckb_docname[ckb])

#     def load_OJT(self, url):
#         # request e exibição do body_web com o documento OJT
    
    def validate_training(self):
        Login_controller.set_flag(False)
        self.thread_vt = thread_vt()
        self.thread_vt.vt.connect(self.update_window)
        self.thread_vt.start_thread(1)
    
    def turnon_login(self):
        self.thread_vt.start_thread(2)

    def update_window(self, rfid, window):
        self.lbl_testeteste.setText(rfid)
        if window == 'success':
            print('-------------------------MOSTRANDO JANELA SUCCESSSSSSSSS-------------------------')
            self.lbl_successvalidation_FPL_03.setVisible(True)
            self.lbl_successvalidation_FPL_03.raise_()
            print('blz to aqui')
        elif window == 'logout':
            print('-------------------------MOSTRANDO JANELA LOGOUUUUT-------------------------')
            print('ue to aqui pq?')
            Login_controller.set_flag(True)
            self.lbl_ok_FPL_00.setVisible(True)
            self.lbl_ok_FPL_00.raise_()

class thread_vt(QThread):
    vt = QtCore.pyqtSignal(str, str)
    
    def run(self):
        for attempts in range(40):
            read = RFRead_controller.RFRead()
            # read = 'asd'
            print(')))))))))))))))))))))))))))))))))))))))))' + str(read))

            if attempts == 0:
                first_read = read
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + first_read)

            if read != first_read and read != None:
                print('entrei============================')
                if self.whatdo == 1:
                    print('-------------------------SUCESS-------------------------')
                    self.vt.emit(str(read), 'success')
                    return
                if self.whatdo == 2:
                    print('-------------------------LOGOUT-------------------------')
                    self.vt.emit(str(read), 'logout')
                    return

            
            time.sleep(0.5)
        
    def start_thread(self, whatdo):
        self.whatdo = whatdo
        self.start()