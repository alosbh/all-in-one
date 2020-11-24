from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request

class Announcements:
    #def get_announcements_url():
        #requisicao pra pegar o url das imagens
    
    def load_announcements_label():
        baseurl = 'http://brbelm0apps01/UserImage/' + self.ID_trim + '.jpg'

        try:
            url = urllib.request.urlopen(baseurl)
        except:
            url = urllib.request.urlopen('http://brbelm0apps01/UserImage/Default.jpg')

        data = url.read()

        # Load image and convert to 32-bit ARGB (adds an alpha channel):
        image = QImage.fromData(data, 'jpg')
        image.convertToFormat(QImage.Format_ARGB32)

        # Crop image to a square:
        imgsize = min(image.width(), image.height())
        rect = QRect(
        (image.width() - imgsize) / 2,
        (image.height() - imgsize) / 2,
        imgsize,
        imgsize,
        )
        image = image.copy(rect)