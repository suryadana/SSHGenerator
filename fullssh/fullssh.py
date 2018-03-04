import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'tools')))

from tools.captcha import Captcha

from bs4 import BeautifulSoup
import mechanize, time

class fullssh(object):
    def __init__(self, bot, server, group_id, user_id, admin_id):
        self.bot = bot
        self.group_id = group_id
        self.user_id = user_id
        self.admin_id = admin_id
        self.help = """
        Server SSH fullssh.
        Server list :
        ======= Server List =========
        Asian
            - Singapura : sg
                - Dropbear Fast : dof
                    - List : 1,2,3,4
        
        America
            - United States : usa
                - List : 1,2
            - Canada : ca
        
        Eropa
            - Netherland: nl
            - United Kingdom : uk
            - Germany : de 
            - France : fr 
                - List : 1,2
        
        Australia
            - Australia : au

        ==============================
        Example command request : /ssh fullssh sg-dof2, /ssh fullssh usa2, /ssh fullssh au
        """
        self.url_server = ""
        if server == "sg-dof1":
            self.url_server = "https://fullssh.com/create-account/ssh/78/singapore"
        elif server == "sg-dof2":
            self.url_server = "https://fullssh.com/create-account/ssh/77/singapore"
        elif server == "sg-dof3":
            self.url_server = "https://fullssh.com/create-account/ssh/79/singapore"
        elif server == "sg-dof4":
            self.url_server = "https://fullssh.com/create-account/ssh/80/singapore"
        elif server == "usa1":
            self.url_server = "https://fullssh.com/create-account/ssh/23/united-states"
        elif server == "usa2":
            self.url_server = "https://fullssh.com/create-account/ssh/26/united-states"
        elif server == "ca":
            self.url_server = "https://fullssh.com/create-account/ssh/37/canada"
        elif server == "nl":
            self.url_server = "https://fullssh.com/create-account/ssh/13/netherland"
        elif server == "uk":
            self.url_server = "https://fullssh.com/create-account/ssh/14/united-kingdom"
        elif server ==  "fr1":
            self.url_server = "https://fullssh.com/create-account/ssh/20/france"
        elif server == "fr2":
            self.url_server = "https://fullssh.com/create-account/ssh/20/france"
        elif server == "de":
            self.url_server = "https://fullssh.com/create-account/ssh/16/germany"
        elif server == "au":
            self.url_server = "https://fullssh.com/create-account/ssh/38/australia"
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
        print browser.form.attrs
        browser.submit()
        soup = BeautifulSoup(browser.response().get_data(), 'lxml')
        return  soup.get_text()

