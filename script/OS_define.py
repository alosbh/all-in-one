import sys
import requests

#1 = windows / 0 = rasp
class OS_define:
    def __init__(self, *args, **kwargs):
        if sys.platform == "win32":
            from PyQt5.QtWebEngineWidgets import QWebEngineView
            from PyQt5.QtWebEngineCore import QWebEngineHttpRequest
        else:
            from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager
            from PyQt5.QtWebKitWidgets import QWebView
            # self.get_hostname()
            
    def get_OS_name(*args, **kwargs):
        
        if sys.platform == "win32":
            return 1
        else:
            return 0
    
    # def get_hostname(*args, **kwargs):
    #     baseUrl = 'http://<ip>:3000/api/v1.0/system/info'
    #     response = requests.get(baseUrl)
    #     print(response)
    #     return response.json()