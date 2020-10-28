class WebService:

    def __init__(self, yamlObject):
        self.__baseUrl = yamlObject['baseUrl'];
        self.__yamlContents = yamlObject;    
