import asyncio
import json
from aiohttp import ClientSession

class Async_login_routine():
    async def async_calls(self):
        async with ClientSession() as session:
            await asyncio.gather(self.something_fast(session), self.something_fast_5(session))

    async def something_fast(self, session):
        response = await session.request(method="GET", url='http://httpbin.org/delay/5')
        #response = response.json()
        print('----------------------------------------------')
        response.raise_for_status()
        html = await response.text()
        resp = json.loads(html)
        print(resp)
        print('----------------------------------------------')
    
    async def something_fast_5(self, session):
        self.something_fast_resp
        response = await session.request(method="GET", url='http://httpbin.org/delay/5')
        #response = response.json()
        print('----------------------------------------------')
        response.raise_for_status()
        html = await response.text()
        self.something_fast_resp = json.loads(html)
        #print(resp)
        print('----------------------------------------------')
    
    # async def get_pixmap(self, url, session=):
    #     data = urllib.request.urlopen(url).read()
    #     pixmap = QPixmap()
    #     pixmap.loadFromData(data)
    #     return pixmap