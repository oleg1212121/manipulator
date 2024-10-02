import time
import requests
from Manipulations.Logger.Logger import Logger
from Manipulations.Simulations.TimeFiller import TimeFiller
from Settings.settings import *


class CheckSlots:

    def __init__(self):
        self.logger = Logger()
        self.filler = TimeFiller()
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "ru",
            "Priority": "u=1, i",
            "Referer": "https://visa.vfsglobal.com/",
            "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Content-type": "application/json;charset=UTF-8",
            "Origin": "https://visa.vfsglobal.com",
            "authority": "lift-api.vfsglobal.com",
            "method": "POST",
            "path": "/appointment/CheckIsSlotAvailable",
            "scheme": "https",
            "Authorize": "",
            "Route": "blr/ru/pol",
            # "X-Amzn-Trace-Id": "Root=1-66e1cc80-1f9de6f92fe78ae063c3ac73",
            # "cache-control": "max-age=0",
            # "sec-fetch-dest": "document",
            # "sec-fetch-mode": "navigate",
            # "sec-fetch-site": "same-origin",
            # "sec-fetch-user": "?1",
            # "upgrade-insecure-requests": "1",
            # "Clientsource": "ovhxckqdibGBKux3yCzFq8FyEN/9dC1QhXu4VY3ZeC4uq8nphYcCe9k6eIUrLbKMRwI/hWpAvBqEVLMapQ/RIPJjDkefpbIjsSAoARFoRPGKO7gRgeeyUNBdLpSZ+kTuzeTLeyDIh8VqKlgwjUNbvNpADCU8VinatS+cHMl+Eu8=",
            # "Cookie": "_ga=GA1.1.580570736.1726158864; _cfuvid=.fABjefm0VOYtFgVoj6DVwVze20TgkElz.aaqtYE_EY-1726225943881-0.0.1.1-604800000; __cf_bm=BWejEUoEweCaNVcZqzsbUJ9uHBW1HteSey5xPeIMSbs-1726567702-1.0.1.1-jmidR9ds92mRcMo3stI1VOUGa8bm_IBmLUd09YLa4BbJiHaD1q3dM4IQRBtFrZwMMRKqVwvISSi2MQj.6mvROA; cf_clearance=dXIcoYTTnyM_mkVzF.Y.T46ceiPpXUS2F0BURWWOF4M-1726567703-1.2.1.1-QqFt_NxKC7LPYmegilMmK76ie0cnWU.nbPzH8zkyLy52ZOtVzUOUdjyBV6Rgtnr_MszE4u0GDZQsq7zyOJ0_1FIadr8gA0dan8WXCoVR0XFyQ4MzihgdnYpOw4GJLdMoRuj0oAYEkshGN9W0Fa0tUGArTNGMdIrG4Ey73YJU4y12hFYw9lloJLolbvgN.zhsfN8lkqv7fRUIC4WiakANoast5TtIq.OUlJrREcae59GrGdvbGEawCv9MhYN4zTbeuQGLOi0SycrthdXvGeDQRJxoAjN8.VYAmAMnh9vb7aHyfwZFzxWiZsCQ6S_LlUphsq63LhGRayo6ucoXRQ1F2RqEKW8sROisP1IJSJf4PRNYwJ2H7RwycWLPNsniRwJG; OptanonAlertBoxClosed=2024-09-17T10:08:29.625Z; dtCookie=-20$QJ3AE7D83O9U03OC4CF156JDR03KL693; rxVisitor=172656771150496KQC8GCMFFEECONF6EGEF06IUE533CI; dtSa=-; dtLatC=5; rxvt=1726569581878|1726567711504; dtPC=-20$367781562_171h-vSRUADHQBACQUGMHLVUNBVRJLUTJRMMRE-0; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Sep+17+2024+13%3A09%3A42+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202408.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=faa1dad5-81e3-4d9c-b698-a714edd2152f&interactionCount=4&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&intType=1&AwaitingReconsent=false&geolocation=BY%3BHM; lt_sn=cef0100b-91f4-41da-9e79-77cf9b69b5ce; _ga_Z8LKRKHHG4=GS1.1.1726567704.3.1.1726567835.6.0.0",
            # "Content-length": "152",
            # "Host": "httpbin.org",
        }
        self.proxies = {
            'http': proxy_url3,
            'https': proxy_url3,
        }
        self.payload = {
            "countryCode": "blr",
            "loginUser": "aleksandrwow.12131@gmail.com",
            "missionCode": "pol",
            "payCode": "",
            "roleName": "Individual",
            "vacCode": "POL-MIN",
            "visaCategoryCode": "CW",
        }

    def process(self, token=None, email=None):
        self.logger.log('Checking slots started')

        if not token or not email:
            raise Exception('MISSED TOKEN OR EMAIL')

        self.headers['Authorize'] = token
        self.payload['loginUser'] = email

        for i in range(0,10):
            try:
                print(f"try request number - {i}")
                response = requests.post(vfs_slots_url, headers=self.headers, json=self.payload)
                print('Response HTTP Status Code: ', response.status_code)
                print('Response HTTP Response Body: ', response.text)
                # {"earliestDate": null, "earliestSlotLists": [], "error": {"code": 1035, "description": "No slots available"}}
                time.sleep(random.randint(10, 13))
            except:
                print('Request failed')


