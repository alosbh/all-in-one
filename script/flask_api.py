from flask import Flask
from GlobalParameters import *
from PyQt5.QtCore import QObject, pyqtSignal, QUrl, QThread

app = Flask(__name__)

class Flask_api(QThread):
    GlobalParameters = GlobalParameters()
    @app.route('/')
    def hello_world():
        return GlobalParameters.return_version_aio()
    
    def run(self):
        app.run()