import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'tools')))

from tools.captcha import Captcha

from bs4 import BeautifulSoup
import mechanize, time, re

class skyssh(object):
    def __init__(self, bot, server, group_id, user_id, admin_id):
        self.bot = bot
        self.group_id = group_id
        self.user_id = user_id
        self.admin_id = admin_id
        self.help = """
        Server SSH skyssh.
        Server list :
        ======= Server List =========
        Asian
            - Singapura : sg
                - Premium : sg
                    - List : 1,2,3 (disable)
                - SGDO : do
                    - List : 1,2,3,4,5,6,7,8,9,10
            - Japan : jp
        America
            - United States : usa
                - List : 1,2,3
            - Canada : ca
        
        Europa
            - Netherland : nl
            - United Kingdom : uk
            - Germany : de
            - France : fr
        
        Australia
            - Australia : au

        ==============================
        Example command request : /ssh skyssh sg-do2, /ssh skyssh sg2
        """
        self.url_server = ""
        #if server == "sg1":
            #self.url_server = "https://skyssh.com/create-ssh/server/94/singapore"
        #elif server == "sg2":
            #self.url_server = "https://skyssh.com/create-ssh/server/95/singapore"
        #elif server == "sg3":
            #self.url_server = "https://skyssh.com/create-ssh/server/92/singapore"
        if server == "sg-do1":
            self.url_server = "https://skyssh.com/create-ssh/server/94/singapore"
        elif server == "sg-do2":
            self.url_server = "https://skyssh.com/create-ssh/server/95/singapore"
        elif server == "sg-do3":
            self.url_server = "https://skyssh.com/create-ssh/server/92/singapore"
        elif server == "sg-do4":
            self.url_server = "https://skyssh.com/create-ssh/server/91/singapore"
        elif server == "sg-do5":
            self.url_server = "https://skyssh.com/create-ssh/server/90/singapore"
        elif server == "sg-do6":
            self.url_server = "https://skyssh.com/create-ssh/server/89/singapore"
        elif server == "sg-do7":
            self.url_server = "https://skyssh.com/create-ssh/server/88/singapore"
        elif server == "sg-do8":
            self.url_server = "https://skyssh.com/create-ssh/server/87/singapore"
        elif server ==  "sg-do9":
            self.url_server = "https://skyssh.com/create-ssh/server/86/singapore"
        elif server == "sg-do10":
            self.url_server = "https://skyssh.com/create-ssh/server/85/singapore"
        elif server == "jp":
            self.url_server = "https://skyssh.com/create-ssh/server/84/japan"
        elif server == "usa1":
            self.url_server = "https://skyssh.com/create-ssh/server/81/united-states"
        elif server == "usa2":
            self.url_server = "https://skyssh.com/create-ssh/server/80/united-states"
        elif server == "usa3":
            self.url_server = "https://skyssh.com/create-ssh/server/79/united-states"
        elif server == "ca":
            self.url_server = "https://skyssh.com/create-ssh/server/75/canada"
        elif server == "nl":
            self.url_server = "https://skyssh.com/create-ssh/server/78/netherland"
        elif server == "uk":
            self.url_server = "https://skyssh.com/create-ssh/server/76/united-kingdom"
        elif server == "de":
            self.url_server = "https://skyssh.com/create-ssh/server/82/germany"
        elif server == "fr":
            self.url_server = "https://skyssh.com/create-ssh/server/83/france"
        elif server == "au":
            self.url_server = "https://skyssh.com/create-ssh/server/77/australia"
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
        #browser.form.attrs['action'] = Besthelper().get_url(soup)
        browser.submit()
        soup = BeautifulSoup(browser.response().get_data(), 'lxml')
        return  soup.get_text()

