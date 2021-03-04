from ApiManager import ApiManager
from aiohttp import ClientSession
from PyQt5.QtGui import QPixmap

import asyncio
import json

class Async_login_routine():
    async def async_calls(self, DL_id):
        async with ClientSession() as session:
            await asyncio.gather(self.product_info(session), self.pixmap_painel(session), self.pixmap_lean(session), self.pixmap_toolbox(session), 
            self.pixmap_environment(session), self.fpl_documents(session, DL_id), self.LPA_actions(session), self.load_metrics(session))

    async def load_metrics(self, session):
        url_metrics = 'http://brbelm0itqa01/AIOService_AIODashboard/Prodash/GetActualUserAttributes/' + self.Raspberry.Name
        try:
            response = await session.request(method="GET", url=url_metrics)
            response.raise_for_status()
            html = await response.text()
            resp = json.loads(html)
            self.Yield = str(round(float(Metrics[0]["Attributes"][3]["Percent"]), 1))
            self.Productivity = str(round(float(Metrics[0]["Attributes"][4]["Percent"]), 1))
        except:
            self.Yield = 0
            self.Productivity = 0

    async def fpl_documents(self, session, DL_id):
        url_alldocs = 'http://brbelm0mat81/ojt/api/Trainings?physicalWorkstationId='+ str(self.Station.Id) +'&traineeRegistration=' + str(DL_id)
        try: 
            response = await session.request(method="GET", url=url_alldocs)
            print('1651652----------------------------------------------')
            if response.status == 200:
                response.raise_for_status()
                html = await response.text()
                self.fpl_all_docs = json.loads(html)
            else:
                self.fpl_all_docs = None
        except:
            self.fpl_all_docs = None
        print('1651652----------------------------------------------')

    async def LPA_actions(self, session):
        url_LPAactions = 'http://brbelm0apps02/AIOService/Lpa/GetOpenActionsByPost/?parameters=' + self.Station.Name
        try: 
            response = await session.request(method="GET", url=url_LPAactions)
            print('111111----------------------------------------------')
            response.raise_for_status()
            html = await response.text()
            self.lpa_actions = json.loads(html)
        except:
            self.lpa_actions = 0
        print('111111----------------------------------------------')

    async def product_info(self, session):
        request_lineInfo = await session.request(method="GET", url='http://brbelm0itqa01/AIOService_AIODashboard/Prodash/GetByLine/' + str(self.Station.RouteId))
        print('5----------------------------------------------')

        html = await request_lineInfo.text()
        resp = json.loads(html)

        if (resp is None):
            self.ProductName = 'No product'
            self.ClientName = 'No client'
        else:
            self.ProductName = resp['Product']
            self.ClientName = resp['ProductionGroup']
        print('5----------------------------------------------')
    
    # async def DL_picture(self, session, DL_id):
    #     url_picture = 'http://brbelm0apps01/UserImage/' + DL_id + '.jpg'
    #     print('99999----------------------------------------------')
    #     try:
    #         response = await session.request(method="GET", url=url_picture)
    #         self.DL_picture_data = await response.read()
    #     except:  
    #         default = await session.request(method="GET", url='http://brbelm0apps01/UserImage/Default.jpg')
    #         self.DL_picture_data = await default.read()
    #     print('99999----------------------------------------------')

    async def pixmap_painel(self, session):
        response = await session.request(method="GET", url='http://brbelm0itqa01/AIOServiceSTG/Images5S/Painel.png')
        print('10----------------------------------------------')
        try:
            resp = await response.read()
            pixmap = QPixmap()
            pixmap.loadFromData(resp)
            self.pixmap_painel = pixmap
        except:
            self.pixmap_painel = None
        print('10----------------------------------------------')

    async def pixmap_lean(self, session):
        response = await session.request(method="GET", url='http://brbelm0itqa01/AIOServiceSTG/Images5S/Lean.png')
        print('100----------------------------------------------')
        try:
            resp = await response.read()
            pixmap = QPixmap()
            pixmap.loadFromData(resp)
            self.pixmap_lean = pixmap
        except:
            self.pixmap_lean = None
        print('100----------------------------------------------')

    async def pixmap_toolbox(self, session):
        response = await session.request(method="GET", url='http://brbelm0itqa01/AIOServiceSTG/Images5S/Toolbox.png')
        print('1000----------------------------------------------')
        try:
            resp = await response.read()
            pixmap = QPixmap()
            pixmap.loadFromData(resp)
            self.pixmap_toolbox = pixmap
        except:
            self.pixmap_toolbox = None
        print('1000----------------------------------------------')
    
    async def pixmap_environment(self, session):
        response = await session.request(method="GET", url='http://brbelm0itqa01/AIOServiceSTG/Images5S/Environment.png')
        print('10000----------------------------------------------')
        try:
            resp = await response.read()
            pixmap = QPixmap()
            pixmap.loadFromData(resp)
            self.pixmap_environment = pixmap
        except:
            self.pixmap_environment = None
        print('10000----------------------------------------------')

    def get_yield(self):
        return self.Yield

    def get_productivity(self):
        return self.Productivity

    def get_fpl_all_docs(self):
        return self.fpl_all_docs
    
    def get_lpa_actions(self):
        return self.lpa_actions

    def get_client_name(self):
        return self.ClientName

    def get_product_name(self):
        return self.ProductName

    def get_pixmap_lean(self):
        return self.pixmap_lean

    def get_pixmap_painel(self):
        return self.pixmap_painel
    
    def get_pixmap_toolbox(self):
        return self.pixmap_toolbox

    def get_pixmap_environment(self):
        return self.pixmap_environment