import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'tools')))

from tools.captcha import Captcha

from bs4 import BeautifulSoup
import mechanize, time

class sshudp(object):
    def __init__(self, bot, server, group_id, user_id, admin_id):
        self.bot = bot
        self.group_id = group_id
        self.user_id = user_id
        self.admin_id = admin_id
        self.help = """
        Server SSH sshudp.
        Server list :
        ======= Server List =========
        Asian
            - Singapura : sg
                - List : 1,2,3,4
        America
            - United States: usa
                - List : 1,2
            - Canada : ca
                - List : 1,2
        Europa
            - Netherland : nl
            - United Kingdom : uk
                - List : 1,2
            - Germany : de

        ==============================
        Example command request : /ssh sshudp sg2, /ssh sshudp usa2
        """
        self.url_server = ""
        if server == "sg1":
            self.url_server = "http://sshudp.com/home/server/singapore1"
        elif server == "sg2":
            self.url_server = "http://sshudp.com/home/server/singapore2"
        elif server == "sg3":
            self.url_server = "http://sshudp.com/home/server/singapore3"
        elif server == "sg4":
            self.url_server = "http://sshudp.com/home/server/singapore4"
        elif server == "usa1":
            self.url_server = "http://sshudp.com/home/server/usa1"
        elif server == "usa2":
            self.url_server = "http://sshudp.com/home/server/usa2"
        elif server == "ca1":
            self.url_server = "http://sshudp.com/home/server/canada1"
        elif server == "ca2":
            self.url_server = "http://sshudp.com/home/server/canada2"
        elif server == "uk1":
            self.url_server = "http://sshudp.com/home/server/uk1"
        elif server == "uk2":
            self.url_server = "http://sshudp.com/home/server/uk2"
        elif server == "nl":
            self.url_server = "http://sshudp.com/home/server/netherlands"
        elif server == "de":
            self.url_server = "http://sshudp.com/home/server/germany"
        else:
            bot.sendMessage(user_id, "Please check your request.")
            bot.sendMessage(user_id, self.help)

    def generate(self, first_name):
        browser = mechanize.Browser()
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        headers = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1'),
        ]

        browser.addheaders = headers

        browser.open(self.url_server)

        browser.select_form(nr=0)
        browser.form['username'] = first_name+str(int(time.time()))[4:]
        browser.form['password'] = str(int(time.time()))[4:]
        browser.submit()
        soup = BeautifulSoup(browser.response().get_data(), 'lxml')
        return  soup.get_text()