from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import MFRC522
import json
import time

class FPL_controller():
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
    
#     def show_validate_window(self):
    # def RFRead(self):

    #     Read_ID = None

    #          # Instantiate the RFID reader class
    #     reader = MFRC522.MFRC522()

    #          # Get the badge id from the RFID reader
    #     Read_ID = reader.JABIL_Matricula() 

    #          # close the SPI slot 
    #     reader.close_SPI()

    #     return Read_ID

    def validate_training(self):
        #self.logout_activated == 0
        for attempts in range(10):
            self.lbl_testeteste.setText(self.RFRead())
            print(attempts)
            time.sleep(0.5)

        #self.logout_activated == 1
        #testetesteid = self.RFRead()
        # self.logout_activated == 1
        #self.lbl_testeteste.setText('Terminou')
        #self.lbl_testeteste.setText(testetesteid)



        # verifica todos os checkbox
        # monta body
        # request validacao
        # if ok
        # self.lbl_successvalidation_FPL._raise()
        # else