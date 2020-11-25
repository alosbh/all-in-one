from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import urllib.request

class Announcements:
    def load_announcements_label(self):
        try:
            url1_pixmap = self.get_pixmap('http://brbelm0itqa01/AIOServiceSTG/Images5S/Frame1.png')
            # url1_pixmap = url1_pixmap.scaled(591, 311, QtCore.Qt.KeepAspectRatio)
            self.lbl_value_announcement_01.setPixmap(url1_pixmap)
        except:
            self.lbl_value_announcement_01.setVisible(False)

        try:
            url2_pixmap = self.get_pixmap('http://brbelm0itqa01/AIOServiceSTG/Images5S/Frame2.png')
            # url2_pixmap = url2_pixmap.scaled(441, 311, QtCore.Qt.KeepAspectRatio)
            self.lbl_value_announcement_02.setPixmap(url2_pixmap)
        except:
            self.lbl_value_announcement_02.setVisible(False)
    
    def get_pixmap(self, url):
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        return pixmap