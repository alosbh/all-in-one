from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QUrl
import requests
import json

class LPAactions_controller():
    def LPAactions_functions(self, workstation_name):
        url_LPAactions = 'http://brbelm0itqa01/AIOServiceSTG/Lpa/GetOpenActionsByPost/?parameters=GENSMTARI001'# + workstation_name
        request_LPAactions = requests.get(url_LPAactions)
        response_LPAactions = request_LPAactions.json()

        if response_LPAactions < 1:
            self.btn_actionsLPA.hide()
            self.lbl_value_number_actionsLPA.hide()
        else:
            self.lbl_value_number_actionsLPA.setText(str(response_LPAactions))
            self.btn_actionsLPA.clicked.connect(lambda: self.redirect_LPAactions(workstation_name))


    def redirect_LPAactions(self, workstation_name):
        url_LPAactions = 'http://brbelm0itqa01/LPASTG/Lpa/GetOpenActionsByPost/GENSMTARI001'# + workstation_name
        self.body_web.load(QUrl(url_LPAactions))
        self.body_web.setVisible(True)