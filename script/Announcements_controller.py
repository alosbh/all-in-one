from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from Async_login_routine import *
import urllib.request

class Announcements_controller():
    def load_announcements_label(self):
        try:
            self.lbl_value_announcement_01.setVisible(True)
            self.lbl_value_announcement_01.setPixmap(self.get_pixmap_painel())
        except:
            self.lbl_value_announcement_01.setVisible(False)
        
        try:
            self.lbl_value_announcement_02.setVisible(True)
            self.lbl_value_announcement_02.setPixmap(self.get_pixmap_lean())
        except:
            self.lbl_value_announcement_02.setVisible(False)
        
        try:
            self.lbl_value_announcement_03.setVisible(True)
            self.lbl_value_announcement_03.setPixmap(self.get_pixmap_toolbox())
        except:
            self.lbl_value_announcement_03.setVisible(False)
        
        try:
            self.lbl_value_announcement_04.setVisible(True)
            self.lbl_value_announcement_04.setPixmap(self.get_pixmap_environment())
        except:
            self.lbl_value_announcement_04.setVisible(False)