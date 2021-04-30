from GlobalParameters import *

class Flask_api():
    GlobalParameters = GlobalParameters()
    def hello_world(self):
        f = open("C:/02 - www/myfile.txt", "w")
        f.write(GlobalParameters.return_version_aio())
        f.close()