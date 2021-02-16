from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QUrl
import requests
import json

class LPAactions_controller():
    def LPAactions_functions(self, workstation_name):
        url_LPAactions = 'http://brbelm0apps02.corp.jabil.org/AIOService/Lpa/GetOpenActionsByPost/?parameters=' + workstation_name
        request_LPAactions = requests.get(url_LPAactions)
        response_LPAactions = request_LPAactions.json()
        if response_LPAactions == 0:
            self.btn_actionsLPA.hide()
            self.lbl_value_number_actionsLPA.hide()
        else:
            self.btn_actionsLPA.setVisible(True)
            self.lbl_value_number_actionsLPA.setVisible(True)
            self.lbl_value_number_actionsLPA.setText(str(response_LPAactions))
            self.btn_actionsLPA.clicked.connect(lambda: self.redirect_LPAactions(workstation_name))


    def redirect_LPAactions(self, workstation_name):
        url_LPAactions = 'http://brbelm0apps01.corp.jabil.org/LPAEletronico/lpa/GetOpenActionsByPost/' + workstation_name
        self.body_web.load(QUrl(url_LPAactions))
        self.body_web.setVisible(True)