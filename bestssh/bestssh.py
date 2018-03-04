import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'tools')))

from tools.captcha import Captcha
from tools.tools import Besthelper

from bs4 import BeautifulSoup
import mechanize, time, re

class bestssh(object):
    def __init__(self, bot, server, group_id, user_id, admin_id):
        self.bot = bot
        self.group_id = group_id
        self.user_id = user_id
        self.admin_id = admin_id
        self.help = """
        Server SSH bestssh.
        Server list :
        ======= Server List =========
        Asian
            - Singapura : sg
                - Public : only 'sg' (/ssh bestssh sg)
                - Premium : sg
                    - List : 1,2,3,4,5
                - SGDO : do
                    - List : 1,2,3,4,5,6
                - Fast : fs
                    - List : 1,2,3,4,5,6

        ==============================
        Example command request : /ssh bestssh sg-do2, /ssh bestssh sg-fs2, /ssh bestssh sg, /ssh bestssh sg2
        """
        self.url_server = ""
        if server == "sg":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/52/singapore"
        elif server == "sg1":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/3/singapore"
        elif server == "sg2":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/4/singapore"
        elif server == "sg3":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/5/singapore"
        elif server == "sg4":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/7/singapore"
        elif server == "sg5":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/12/singapore"
        elif server == "sg-do1":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/13/singapore"
        elif server == "sg-do2":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/14/singapore"
        elif server == "sg-do3":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/15/singapore"
        elif server == "sg-do4":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/47/singapore"
        elif server == "sg-do5":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/48/singapore"
        elif server == "sg-do6":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/49/singapore"
        elif server == "sg-fs1":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/36/singapore"
        elif server == "sg-fs2":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/37/singapore"
        elif server ==  "sg-fs3":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/40/singapore"
        elif server == "sg-fs4":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/41/singapore"
        elif server == "sg-fs5":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/43/singapore"
        elif server == "sg-fs6":
            self.url_server = "https://bestvpnssh.com/create-account/ssh/44/singapore"
        else:
            bot.sendMessage(user_id, "Please check your request.")
            bot.sendMessage(user_id, self.help)
    def generate(self, first_name):
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        headers = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1'),
        ]

        browser.addheaders = headers

        image, browser = Captcha(self.bot).get_image(browser, self.url_server)
        soup = BeautifulSoup(browser.response().get_data(), 'lxml')
        browser.select_form(nr=0)
        browser.form['username'] = first_name+str(int(time.time()))[4:]
        browser.form['password'] = str(int(time.time()))[4:]
        browser.form['captcha'] = Captcha(self.bot).read_image(image)
        browser.form.attrs['action'] = Besthelper().get_url(soup)
        browser.submit()
        soup = BeautifulSoup(browser.response().get_data(), 'lxml')
        return  soup.get_text()

