import sys

#1 = windows / 0 = rasp
class OS_define:
    def __init__(self):
            self.OS_define_name = ''
        
    def get_OS_name(self):
        
        if sys.platform == "win32":
            return 1
        else:
            return 0