# -*- coding: UTF-8 -*-
import requests
from lxml import html

USERNAME = "131110305"
PASSWORD = "zsx941015"

LOGIN_URL = "http://210.38.162.116/default2.aspx"


def main():
    request = requests.get(LOGIN_URL)
    content = request.text
    url = request.url


    tree = html.fromstring(content)
    viewstate = tree.xpath("//input[@name='__VIEWSTATE']/@value")
    print(viewstate)
    type = list(set(tree.xpath("//input[@name='RadioButtonList1']/@value")))[3]

    # Create payload
    payload = {
        "txtUserName": USERNAME,
        "TextBox2": PASSWORD,
        "txtSecretCode": '',
        "Button1": '',
        "lbLanguage": '',
        "hidPdrs": '',
        "hidsc": '',
        "__VIEWSTATE": viewstate,
        "RadioButtonList1": type
    }

    # Create header
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 59.0.3071.115Safari537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Referer': url
    }


    # Perform login
    result = requests.post(url, data = payload, headers = headers)
    tree = html.fromstring(result.text)
    # print(result.text)

    xm = list(set(tree.xpath("//span[@id='xhxm']/text()")))[0]
    xm = xm.replace(" ","")
    xm = xm[9:-2]
    print(xm)


    # Scrape url
    scoreurl = url.replace("default2","xscjcx") + "?xh=" + USERNAME + "&xm=" + xm + "&gnmkdm=N121605"
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 59.0.3071.115Safari537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Referer': result.url
    }

    result = requests.get(scoreurl, headers = headers)
    # print(result.text)
    tree = html.fromstring(result.text)
    viewstate = tree.xpath("//input[@name='__VIEWSTATE']/@value")

    print(viewstate)
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
    result = requests.post(scoreurl, data = payload, headers = headers)
    tree = html.fromstring(result.text)
    print(result.text)
    datatable = list(set(tree.xpath("//table[@id='Datagrid1']/tr")))
    i = 0;
    for tr in datatable:
        for td in tr.findall("td"):
            print td.text,
        i = i + 1
        print ""
    print(i)
    # # Scrape url
    # result = session_requests.get(URL, headers = dict(referer = URL))

    # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")
    #
    # print(bucket_names)


if __name__ == '__main__':
    main()