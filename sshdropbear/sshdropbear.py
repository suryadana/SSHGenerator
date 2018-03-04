import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'tools')))

from tools.captcha import Captcha

from bs4 import BeautifulSoup
import mechanize, time

class sshdropbear(object):
    def __init__(self, bot, server, group_id, user_id, admin_id):
        self.bot = bot
        self.group_id = group_id
        self.user_id = user_id
        self.admin_id = admin_id
        self.help = """
        Server SSH sshdropbear.
        Server list :
        ======= Server List =========
        Asian
            - Singapura : sg
                - Fast : fast
                    - List : 1,2,3,4,5,6,7
                - Dropbear : do
                    - List : 1,2,3,4,5,6,7
            - Japan : jp
            - India : in

        America
            - United States: usa
                - List : 1,2,3
	    - Canada: ca
        
        Eropa
            - Netherland: nl
            - United Kingdom : uk
            - Germany : de 
            - France : fr 
        
        Australia
            - Australia : au

        ==============================
        Example command request : /ssh sshdropbear sg-do2, /ssh sshdropbear sg-wkl2, /ssh sshdropbear jp
        """
        self.url_server = ""
        if server == "sg-fast1":
            self.url_server = "https://sshdropbear.net/create-ssh/server/987656799/singapore"
        elif server == "sg-fast2":
            self.url_server = "https://sshdropbear.net/create-ssh/server/987656800/singapore"
        elif server == "sg-fast3":
            self.url_server = "https://sshdropbear.net/create-ssh/server/987656808/singapore"
        elif server == "sg-fast4":
            self.url_server = "https://sshdropbear.net/create-ssh/server/987656812/singapore"
        elif server == "sg-fast5":
            self.url_server = "https://sshdropbear.net/create-ssh/server/987656813/singapore"
        elif server == "sg-fast6":
            self.url_server = "https://sshdropbear.net/create-ssh/server/987656802/singapore"
        elif server == "sg-fast7":
            self.url_server = "https://sshdropbear.net/create-ssh/server/987656803/singapore"
        elif server == "sg-do1":
            self.url_server = "https://sshdropbear.net/create-ssh/server/5145709/singapore"
        elif server == "sg-do2":
            self.url_server = "https://sshdropbear.net/create-ssh/server/5655808/singapore"
        elif server ==  "sg-do3":
            self.url_server = "https://sshdropbear.net/create-ssh/server/62546093/singapore"
        elif server == "sg-do4":
            self.url_server = "https://sshdropbear.net/create-ssh/server/455764/singapore"
        elif server == "sg-do5":
            self.url_server = "https://sshdropbear.net/create-ssh/server/455686/singapore"
        elif server == "sg-do6":
            self.url_server = "https://sshdropbear.net/create-ssh/server/45567/singapore"
        elif server == "sg-do7":
            self.url_server = "https://sshdropbear.net/create-ssh/server/45455612/singapore"
        elif server == "jp":
            self.url_server = "https://sshdropbear.net/create-ssh/server/21/japan"
        elif server == "in":
            self.url_server = "https://sshdropbear.net/create-ssh/server/22/india"
        elif server == "usa1":
            self.url_server = "https://sshdropbear.net/create-ssh/server/32/united-states"
        elif server == "usa2":
            self.url_server = "https://sshdropbear.net/create-ssh/server/987656809/united-states"
        elif server == "usa3":
            self.url_server = "https://sshdropbear.net/create-ssh/server/987656810/united-states"
	elif server == "ca":
	    self.url_server = "https://sshdropbear.net/create-ssh/server/34/canada"
        elif server == "nl":
            self.url_server = "https://sshdropbear.net/create-ssh/server/28/netherland"
        elif server == "uk":
            self.url_server = "https://sshdropbear.net/create-ssh/server/26/united-kingdom"
        elif server == "de":
            self.url_server = "https://sshdropbear.net/create-ssh/server/29/germany"
        elif server == "fr":
            self.url_server = "https://sshdropbear.net/create-ssh/server/25/france"
        elif server == "au":
            self.url_server = "https://sshdropbear.net/create-ssh/server/35/australia"
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

        browser.select_form(nr=0)
        browser.form['username'] = first_name+str(int(time.time()))[4:]
        browser.form['password'] = str(int(time.time()))[4:]
        browser.form['captcha'] = Captcha(self.bot).read_image(image)
        browser.submit()
        soup = BeautifulSoup(browser.response().get_data(), 'lxml')
        return  soup.get_text()

