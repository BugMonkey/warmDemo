from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'


class madeInChinaParser(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        self.cookie = None
        self.rq = requests.Session()

    # 获取首页所需条件 验证码 cookies等 准备登陆
    def main_page(self):
        # http://win.madeinchina.cn/saas/land.html

        self.login(self.getRequest('http://win.madeinchina.cn/saas/land.html'))

    def getRequest(self, url):

        response = self.rq.get(url, headers=self.headers)
        self.cookie = response.cookies
        print(self.cookie)
        # 获取验证码

        img = self.rq.get('http://win.madeinchina.cn/ValidateCode.aspx', cookies=self.cookie, headers=self.headers)

        if img.status_code == 200:
            with open('logo.jpg', 'wb') as f:
                for chunk in img:
                    f.write(chunk)
            image = Image.open('logo.jpg')
            code = pytesseract.image_to_string(image)
            print(code)
            return code


    def login(self, inputcode):

        # type=1&inputCode=dvww&Email=791281557%40qq.com&pwd=JOSCOLILY%40914501
        login_map = {'type': '1', 'inputCode': inputcode, 'Email': '791281557%40qq.com', 'pwd': 'JOSCOLILY%40914501'}
        login_response = self.rq.post('http://win.madeinchina.cn/saas/LoginControl.aspx', headers=self.headers,
                                      cookies=self.cookie, params=login_map)

        print(self.cookie, login_response.headers)
        self.rq .cookies=self.cookie
        self.rq .headers= login_response.headers
        self.querry(self.cookie, login_response.headers)

    '''
'__EVENTARGUMENT': '', '__LASTFOCUS': '',
                     '__VIEWSTATE': '/wEPDwUKMTI2ODIxOTc0MQ9kFgICAw9kFgYCAQ8WAh4EVGV4dAUWPGI+5pCc57Si5p2h5Lu277yaPC9iPmQCAw8QZBAVIwnpgInmi6nnnIEG5a6'
                                    'J5b69BuWMl+S6rAbnpo/lu7oG55SY6IKDBuW5v+S4nAblub/opb8G6LS15beeBua1t+WNlwbmsrPljJcG5rKz5Y2XCem7kem+meaxnwb'
                                    'muZbljJcG5rmW5Y2XBuWQieaelwbmsZ/oi48G5rGf6KW/Bui+veWugQnlhoXokpnlj6QG5a6B5aSPBumdkua1twblsbHk'
                                    'uJwG5bGx6KW/BumZleilvwbkuIrmtbcG5Zub5bedBuWkqea0pQbopb/ol48G5paw55aGBuS6keWNlwbmtZnmsZ8G'
                                    '6YeN5bqGBummmea4rwbmvrPpl6gG5Y+w5rm+FSMBMAQxMDAyBDEwOTgEMTEwMwQxMTgxBDI2MTQEMTI3NwQxM'
                                    'zgyBDE0NzQEMTUxMQQxNjcwBDE4MTYEMTkwOAQyMDAyBDIxMTgEMjE3NwQyMjU4BDIzNjEEMjQzNAQyNTM2BDI1Nj'
                                    'EEMjg0NwQyNzI4BDI5NzMEMjYxMAQzMDc4BDMyNTYEMzI5MAQzMzcxBDM1NTkEMzQ3OAQzMjYyBDk5OTcEOTk5OAQ'
                                    '5OTk5FCsDI2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnFgECD2QCBA8QZBAVDgnpgInmi6n'
                                    'luIIG5bi45beeBua3ruWuiQnov57kupHmuK8G5Y2X5LqsBuWNl+mAmgboi4/lt54G5a6/6L+BBuazsOW3ngbml6D'
                                    'plKEG5b6Q5beeBuebkOWfjgbmiazlt54G6ZWH5rGfFQ4BMAQyMjQzBDIxOTYEMjE5MAQyMTc4BDIyMzAEMjI1MQ'
                                    'QyMjAyBDIyMjQEMjI0NwQyMTgyBDIyMDgEMjIxOAQyMjM4FCsDDmdnZ2dnZ2dnZ2dnZ2dnZGRkBOfgZpiy4VU3Ya'
                                    'OCWZILyFoZ1+Yk1rLXeMzUL6A01bk=',
'''

    def querry(self, cookies, headers):
        # Referer: http://win.madeinchina.cn/YellowPages01_revise.aspx
        headers['Referer'] = 'http://win.madeinchina.cn/menu.html'
        self.rq.post('http://win.madeinchina.cn/YellowPages01_revise.aspx')
        headers['Referer'] = 'http://win.madeinchina.cn/YellowPages01_revise.aspx'
        query_map = {'corpkey': '', 'drpProvince': '2177',
                     'drpCity': '2224', 'begintme': '2013-03-25'
            , 'endtme': '2018-03-25', 'Button1': '搜索客户', 'textfield2': ''}
        print(headers)
        login_response = self.rq.post('http://win.madeinchina.cn/YellowPages01_revise.aspx', params=query_map)
        print(login_response.status_code)
        print(BeautifulSoup(login_response.content, 'html.parser', from_encoding='utf-8'))


if __name__ == "__main__":
    parser = madeInChinaParser()
    parser.main_page()
