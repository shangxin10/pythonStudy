# -*- coding: UTF-8 -*-
import requests
import config
from lxml import html


LOGIN_URL = "http://210.38.162.116/default2.aspx"
HEADER = {
            'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 59.0.3071.115Safari537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }




def login(username,password):
    try:
        request = requests.get(LOGIN_URL)
        content = request.text
        url = request.url

        tree = html.fromstring(content)
        viewstate = tree.xpath("//input[@name='__VIEWSTATE']/@value")
        print(viewstate)
        type = list(set(tree.xpath("//input[@name='RadioButtonList1']/@value")))[3]

        # Create payload
        payload = {
            "txtUserName": username,
            "TextBox2": password,
            "txtSecretCode": '',
            "Button1": '',
            "lbLanguage": '',
            "hidPdrs": '',
            "hidsc": '',
            "__VIEWSTATE": viewstate,
            "RadioButtonList1": type
        }

        # Create header
        HEADER['Referer'] = url;

        # Perform login
        result = requests.post(url, data = payload, headers = HEADER)
        tree = html.fromstring(result.text)

        xm = list(set(tree.xpath("//span[@id='xhxm']/text()")))[0]
        xm = xm.replace(" ","")
        xm = xm[9:-2]

        return result.url
    except Exception, e:
        return None

def loadScorePage(url):
    try:
        # Scrape url
        scoreurl = url.replace("xs_main","xscjcx") + "&gnmkdm=N121605"
        HEADER['Referer'] = url;

        result = requests.get(scoreurl, headers = HEADER)

        tree = html.fromstring(result.text)
        viewstate = tree.xpath("//input[@name='__VIEWSTATE']/@value")
        return {'viewstate':viewstate, 'url': scoreurl}
    except Exception, e:
        return None

def loadlncj(viewstate, url):
    try:
        payload = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": viewstate,
            "hidLanguage": "",
            "ddlXN": "",
            "ddlXQ": "",
            "ddl_kcxz": "",
            "btn_zcj": "历年成绩",
        }
        HEADER['Referer'] = url;
        result = requests.post(url, data = payload,headers=HEADER)
        tree = html.fromstring(result.text)
        print(result.text)
        datatable = list(set(tree.xpath("//table[@id='Datagrid1']/tr")))
        i = 0;
        lncjTable = config.lncjTable
        lncjList = [];
        for tr in datatable:
            j = 0
            dict = {}
            for td in tr.findall("td"):
                dict[lncjTable[j]] = td.text
                j = j + 1
                print dict[lncjTable[j]]
            i = i + 1
            lncjList.append(dict)
            print ""
        print(i)
    except Exception, e:
        return None