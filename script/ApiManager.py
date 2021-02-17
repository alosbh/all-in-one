# -*- coding: utf-8 -*-
import os
import importlib
import yaml
#Imports das bibliotecas: Comunicação com Webservers
import json
import requests
from requests.exceptions import ConnectionError
from WebService import *
import re as regex
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
import time
from OS_define import OS_define
from datetime import datetime
from pathlib import Path
import sys
import platform
import logging
global logger
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)


class ApiManager:
    
    script_location = Path(__file__).absolute().parent

    def __init__(self, FilePath = script_location / 'Apis.yml'):

        with open(FilePath, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

        self.OJT = WebService(cfg['OJT'])
        self.AIO = WebService(cfg['AIO'])
        self.AIO_Dashboard = WebService(cfg['AIO_Dashboard'])
        #self.JMD = WebService(cfg['JMD'])

        
    def Request(self, webServiceObject, functionName, parameterObject):

        
        if isinstance(webServiceObject, WebService):

            for prop in webServiceObject._WebService__yamlContents:
                
                for key in webServiceObject._WebService__yamlContents[prop]:
                    if (prop=='baseUrl'):
                        continue

                    if (regex.match(functionName, key, regex.I|regex.M)):   
                        endPoint = webServiceObject._WebService__baseUrl+prop+"/"+key+"/";
                        
                        

                        RequestType = webServiceObject._WebService__yamlContents[prop][key]['Type']; 
                        ArgumentsCount = webServiceObject._WebService__yamlContents[prop][key]['ArgumentsCount']; 
                    

                        print("##########")
                        print ("link: " + endPoint+str(parameterObject))

                        try:
                            if (regex.match(RequestType, 'Post', regex.I|regex.M)):
                                response = requests.post(endPoint, parameterObject)
                                print(response.elapsed.total_seconds())
                                print("##########")
                                
                                
                                return response.json();

                            elif (regex.match(RequestType, 'Get', regex.I|regex.M)):
                                response = requests.get(endPoint+parameterObject)
                                
                                if (response.status_code==200):
                                    print(response.elapsed.total_seconds())
                                    print("##########")
                                    return response.json()
                                
                                elif (returnData.status_code==404):
                                    
                                    print("API Call " + endPoint+parameterObject + " returned a status code " + returnData.status_code)

                                else:
                                    print("API Call " + endPoint+parameterObject + " returned a status code " + returnData.status_code)
                                    


                                return returnData;
                                pass

                            else:
                                
                                raise Exception("API Type parameter undefined.")

                        except ConnectionError as e:
                            
                            print("No internet connection to perform Api Call " + endPoint + parameterObject +  " Error:" + type(e).__name__)
                            importlib.reload(requests)



                            return type(e).__name__
                        

                        except Exception as e:
                        #except:
                            
                            print("Exception while calling API " + endPoint + " Type: " + type(e).__name__)


                        # returnData = requests.post(endPoint, "")
                        # return returnData;
                        return
            
            raise Exception("Undefined API Function: " + functionName)
        
        else:
            
            raise Exception("Given object is not a WebService object");
        
        return "Problem"

    def GetSingleValueFromJsonObject(self, jsonObject, key, raiseException):
        result = jsonObject.get(key, "Not found");
        
        if (raiseException):
            raise Exception ("A chave: " +key +" não existe dentro do objeto")
        return result;


    def load_LPA(self,BadgeID,Workstep,RouteID):

        baseUrl = 'http://brbelm0apps01/LPAEletronico/Lpa/Login?registration='
        
        if (str(RouteID)=="187" or str(RouteID)=="168" or str(RouteID)=="23" or str(RouteID)=="13" or str(RouteID)=="20" or str(RouteID)=="26" or str(RouteID)=="197"):
            baseUrl = baseUrl + str(BadgeID) + '&idworkline=' + str(RouteID)
        
        elif(str(RouteID)=="152" or str(RouteID)=="153" or str(RouteID)=="200" or str(RouteID)=="208" or str(RouteID)=="205"):

            baseUrl = 'http://brbelm0apps01/LPAVLS/Lpa/Login?registration='
            baseUrl = baseUrl + str(BadgeID) + '&idworkstep=' + str(Workstep)

        else:
            baseUrl = baseUrl + str(BadgeID) + '&idworkstep=' + str(Workstep)

        print("LPA URL addres: " + baseUrl)
        
        return baseUrl

    def load_Jiga(self,lineId):
        baseUrl = 'http://brbelm0apps01/SCTC/Dashboard/ToolingDashboard.aspx?areaId=3&lineId='
        baseUrl = baseUrl + str(lineId)
        return baseUrl

    def load_BI(self,BadgeID,StationID):

        print("workstation id:" + str(StationID))
        userIdurl = "http://brbelm0apps02/AIOService/Jmd/GetUserDetailsByRegistration/" + BadgeID
        r = requests.get(userIdurl)
        response = r.json()
        userId = response['idUser']
        
        baseUrl = 'http://brbelm0apps01/GoodIdeas/GoodIdea/NewIdea?registration=' + str(BadgeID) + '&menuCollapse=true'
        
        print("BI URL addres: " + baseUrl)
        
        return baseUrl

    def load_lineName(self,stationId):
        baseUrl = 'http://brbelm0apps02/JMDDataServices/workstation/'
        baseUrl = baseUrl + str(stationId) + '/productionlines'
        response = requests.get(baseUrl)
        return response.json()

    def load_FI(self,Workstation):

        from PyQt5.QtWebEngineCore import QWebEngineHttpRequest

        self.url = QUrl()
        self.req = QWebEngineHttpRequest()

        self.url.setScheme("http")
        self.url.setHost("brbelm0apps01")
        self.url.setPath("/FICreator/FIViewer/SlideShow")

        self.req.setUrl(self.url)
        self.req.setMethod(QWebEngineHttpRequest.Post)
        self.req.setHeader(QByteArray(b'Content-Type'),QByteArray(b'application/json'))

        parametros = {"workstation": Workstation, "prodashSync": True, "time": 5}

        self.req.setPostData(bytes(json.dumps(parametros), 'utf-8')) 
        
        return self.req

    def load_5s(self,Workstation):

        
        baseUrl = 'http://brbelm0itqa01/AIOServiceSTG/Images5S/GetAll?query='
        baseUrl = baseUrl + str(Workstation)
        print("###########")
        logger.error(baseUrl)
        try:
            response = requests.get(baseUrl)
            logger.error(response.json())
            return response.json();
        except Exception as e:
            print("Erro API 5s:: " + type(e).__name__)
            logger.error("Erro API 5s:: " + type(e).__name__)
            return


    def custom_button(self,Area,AreaTrim,Route,Index):

        if(Area=="INGCUS" and Index==1):
            baseUrl="http://10.57.16.42/CNCSWebApiPersona/OrMonitor?hostName="
            baseUrl = baseUrl + str(Route)
            print("OR MONITOR URL: " + baseUrl)
            logger.error("OR MONITOR URL: " + baseUrl)

        elif(AreaTrim=="REP"):
            baseUrl="http://brbelm0itqa01/TestPortal/pages/MesWipReport.aspx"
            logger.error("LINK TEST WIP REPARO: " + baseUrl)
        
        else:
            baseUrl = 'about:blank'

        return baseUrl