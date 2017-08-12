import requests
from lxml import html
from urllib import urlencode

USERNAME = "131110305"
PASSWORD = "zsx941015"
TYPE="%D1%A7%C9%FA"
LOGIN_URL = "http://210.38.162.116/default2.aspx"
URL = "https://bitbucket.org/dashboard/repositories"

def main():
    session_requests = requests

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
    type = list(set(tree.xpath("//input[@name='RadioButtonList1']/@value")))[3]
    print(type)

    # Create payload
    payload = {
        "txtUserName": USERNAME,
        "TextBox2": PASSWORD,
        "__VIEWSTATE": authenticity_token,
        "RadioButtonList1": type
    }

    print(dict(referer=LOGIN_URL))
    # Perform login
    result = session_requests.post(result.url, data = payload, headers = dict(referer = LOGIN_URL))

    print(result.text)
    # Scrape url
    # result = session_requests.get(URL, headers = dict(referer = URL))
    # tree = html.fromstring(result.content)
    # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")
    #
    # print(bucket_names)

if __name__ == '__main__':
    main()