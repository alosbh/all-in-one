from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QUrl
import requests
import json

class LPAactions_controller():
    workstation_namePP = None

    def LPAactions_functions(self, workstation_name):
        self.workstation_namePP = workstation_name
        url_LPAactions = 'http://localhost:3090/AIOService/Lpa/GetOpenActionsByPost/?parameters=' + workstation_name
        request_LPAactions = requests.get(url_LPAactions)
        response_LPAactions = request_LPAactions.json()
        if response_LPAactions == 0:
            self.btn_actionsLPA.hide()
            self.lbl_value_number_actionsLPA.hide()
        else:
            self.btn_actionsLPA.setEnabled(True)
            self.btn_actionsLPA.setVisible(True)
            self.lbl_value_number_actionsLPA.setVisible(True)
            self.lbl_value_number_actionsLPA.setText(str(response_LPAactions))
            self.btn_actionsLPA.clicked.connect(self.redirect_LPAactions)


    def redirect_LPAactions(self):
        url_LPAactions = 'http://brbelm0apps01/LPAEletronico/lpa/GetOpenActionsByPost/' + self.workstation_namePP
        self.body_web.load(QUrl(url_LPAactions))
        self.body_web.setVisible(True)