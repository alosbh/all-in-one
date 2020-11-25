from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import urllib.request

class Announcements:
    def load_announcements_label(self):
        # get_urls = 'http://brbelm0itqa01/AIOServiceSTG/Images5S/GetAll?query='
        url1_pixmap = self.get_pixmap('https://img.discogs.com/LTslyHzBFWribOAsmxQyeG90z60=/fit-in/591x311/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-8521471-1463302696-2891.jpeg.jpg')
        self.lbl_value_announcement_01.setPixmap(url1_pixmap)
        url2_pixmap = self.get_pixmap('https://i.imgur.com/jrhKjKb.jpg')
        self.lbl_value_announcement_02.setPixmap(url2_pixmap)
    
    def get_pixmap(self, url):
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        return pixmap