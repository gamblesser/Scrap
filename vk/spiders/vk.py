import scrapy
import json
import re
from scrapy.http import Request as Req
from bs4 import BeautifulSoup as BS
from time import sleep
class VkSpider(scrapy.Spider):
    name = 'vk'
    allowed_domains = ['vk.com']
    cookies ={
    "Host raw": "http://.vk.com/",
    "Name raw": "tmr_reqNum",
    "Path raw": "/",
    "Content raw": "2385",
    "Expires": "15-05-2022 16:17:48",
    "Expires raw": "1652620668",
    "Send for": "Any type of connection",
    "Send for raw": "false",
    "HTTP only raw": "false",
    "SameSite raw": "no_restriction",
    "This domain only": "Valid for subdomains",
    "This domain only raw": "false",
    "Store raw": "firefox-default",
    "First Party Domain": ""
}
    headers = {'Host': 'vk.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Requested-With': 'XMLHttpRequest',
'Origin': 'https://vk.com',
'Authorization': 'Basic, ,\XzoxNDQ5ZTkwYzMxMDc4YTNjN2I3ZjliYzdjNDIyNTJmODBmMmNhMTQ1MzgyMzYzZTRmY2I4YzVmMmYwMmFjZDdmZTMwODc2MWRiYTg0NzczOWJhZDdj',
'Connection': 'keep-alive',
'Referer': 'https://vk.com/vbazetrpg',
'Cookie': 'remixlang=0; remixstid=1089598452_2RnoPP9z3AGRW7u4JPF4sjLQuCzBPOXl7fOcJfWnBj0; remixflash=0.0.0; remixscreen_width=1600; remixscreen_height=900; remixscreen_dpr=1; remixscreen_depth=24; remixscreen_orient=1; remixscreen_winzoom=1; remixdt=0; tmr_reqNum=2381; tmr_lvid=469cf46fbe06b948b9c6701308781aed; tmr_lvidTS=1620425248186; tmr_detect=0%7C1623849472124; remixuas=91334ce89719a96211ed013b101a1fe7; remixua=41%7C-1%7C307%7C2467969836; remixseenads=0; remixrefkey=81437699ca28a7481b; remixmdevice=1600/900/1/!!-!!!!; remixcolor_scheme_mode=auto; remixsid=68b78955b96c0cd71e3fdb6928766ea7a95481c4285e58920c3d3f1c38d7e; remixgp=8ac705a39a78190e0f35532a145d4b18; remixcurr_audio=432939041_456239017',
'TE': 'Trailers',
}  

    def start_requests(self):
        offset =0

        yield Req(url=f'https://vk.com/al_wall.php?act=get_wall&al=1&fixed=&offset={offset}&onlyCache=false&owner_id=-86021764&type=own&wall_start_from={offset}',
            headers =self.headers,
            cookies=self.cookies,
            cb_kwargs=dict(offset=offset),
            method='POST')

    def parse(self, response,offset):
        offset +=10
        try:
            body = json.loads(str(response.body,'windows-1251'))
            body = BS(body['payload'][1][0])
            if (body.find('div').find(class_='no_posts_cover')):
                return
            body = body.select('.wall_post_text')
            for elem in body:
                

                for elem1 in elem:
                    aTegs = []
                    if elem1.name =='br':


                        for elem3 in elem1.previous_siblings:




                            if elem3.name =='a':



                                if re.match('#',elem3.get_text()):
                                        elem3 = elem3.get_text().replace('#','',)
                                        aTegs.append(elem3)

                        
                        aTegs = aTegs[::-1]               
                        yield {'data':aTegs[2].lower()}

                        break
        except Exception as e:

            print('ОШИБКА',e)
        yield Req(f'https://vk.com/al_wall.php?act=get_wall&al=1&fixed=&offset={offset}&onlyCache=false&owner_id=-86021764&type=own&wall_start_from={offset}',headers =self.headers,cookies=self.cookies,cb_kwargs=dict(offset=offset),method='POST')


        
