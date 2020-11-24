from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import urllib.request

class Announcements:
    #def get_announcements_url():
        #requisicao pra pegar o url das imagens
    
    def load_announcements_label(self):
        url = 'http://brbelm0itqa01/AIOServiceSTG/Images5S/GetAll?query=' + get_announcements_url  
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        
        return pixmap