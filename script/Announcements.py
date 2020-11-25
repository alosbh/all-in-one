from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import urllib.request

class Announcements:
    def load_announcements_label(self):
        # get_urls = 'http://brbelm0itqa01/AIOServiceSTG/Images5S/GetAll?query='
        url1_pixmap = self.get_pixmap('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjG1dKKvgTCV1DATkPJx2a_JWhl_rEIsLCqQ&usqp=CAU')
        self.lbl_value_announcement_01.setPixmap(url1_pixmap)
        url2_pixmap = self.get_pixmap('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjG1dKKvgTCV1DATkPJx2a_JWhl_rEIsLCqQ&usqp=CAU')
        self.lbl_value_announcement_02.setPixmap(url2_pixmap)
    
    def get_pixmap(self, url):
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        return pixmap