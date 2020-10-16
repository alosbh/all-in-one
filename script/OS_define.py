import sys

#1 = windows / 0 = rasp
class OS_define:
    def __init__(self, *args, **kwargs):
        if sys.platform == "win32":
            from PyQt5.QtWebEngineWidgets import QWebEngineView
            from PyQt5.QtWebEngineCore import QWebEngineHttpRequest
        else:
            from PyQt5.QtNetwork import QNetworkRequest
            
    def get_OS_name(*args, **kwargs):
        
        if sys.platform == "win32":
            return 1
        else:
            return 0