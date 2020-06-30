class WebService:

    def __init__(self, yamlObject):
        # print (dir(yamlObject))
        self.__baseUrl = yamlObject['baseUrl'];
        self.__yamlContents = yamlObject;    
