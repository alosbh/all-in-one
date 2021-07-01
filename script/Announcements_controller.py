from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import urllib.request

class Announcements_controller:
    def load_announcements_label(self):
        try:
            self.lbl_value_announcement_01.setVisible(True)
            url1_pixmap = self.get_pixmap('http://brbelm0apps99/AIOServiceSTG/Images5S/Painel.png')
            self.lbl_value_announcement_01.setPixmap(url1_pixmap)
        except:
            self.lbl_value_announcement_01.setVisible(False)

        try:
            self.lbl_value_announcement_02.setVisible(True)
            url2_pixmap = self.get_pixmap('http://brbelm0apps99/AIOServiceSTG/Images5S/Toolbox.png')
            self.lbl_value_announcement_02.setPixmap(url2_pixmap)
        except:
            self.lbl_value_announcement_02.setVisible(False)
        
        # try: CONFLITO COM ACHIEVMENTS
        #     self.lbl_value_announcement_03.setVisible(False)
        #     # url3_pixmap = self.get_pixmap('http://brbelm0apps99/AIOServiceSTG/Images5S/Lean.png')
        #     # self.lbl_value_announcement_03.setPixmap(url3_pixmap)
        # except:
        #     self.lbl_value_announcement_03.setVisible(False)

        try:
            self.lbl_value_announcement_04.setVisible(False)
            # url4_pixmap = self.get_pixmap('http://brbelm0apps99/AIOServiceSTG/Images5S/Environment.png')
            # self.lbl_value_announcement_04.setPixmap(url4_pixmap)
        except:
            self.lbl_value_announcement_04.setVisible(False)
    
    def get_pixmap(self, url):
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        return pixmap