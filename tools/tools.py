from bs4 import BeautifulSoup
import re

class Besthelper(object):
    def __init__(self):
        self.absolute_url = ""
    def get_url(self, soup):
        url_submit = "https://bestvpnssh.com"
        regx_response = re.findall(r'.*?\"(.*)".*', soup.get_text())
        for x in regx_response:
             if "c-user.php" in x:
                 url_submit += x
                 break
        self.absolute_url = url_submit
        print self.absolute_url
        return self.absolute_url

class Tools(object):
    def __init__(self):
        pass