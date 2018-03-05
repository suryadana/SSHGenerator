import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'tools')))

from tools.captcha import Captcha

from bs4 import BeautifulSoup
import mechanize, time, sqlite3

class sshdropbear(object):
    def __init__(self, bot, server, group_id, user_id, admin_id):
        self.bot = bot
        self.group_id = group_id
        self.user_id = user_id
        self.admin_id = admin_id
        # Connection to database
        BASE = os.path.dirname(os.path.realpath(__file__))
        con = sqlite3.connect(os.path.join(BASE, 'db/urls.db'), check_same_thread=False)
        c = con.cursor()
        c.execute('SELECT header FROM urls')
        result = c.fetchall()
        server_list = "".join(header + "\n" for header in result)

        self.help = """
        Server SSH sshdropbear.
        Server list :
        ======= Server List =========
        {0}
        ==============================
        Example command request : /ssh sshdropbear {1}
        """.format(server_list, result[0][0])
        self.url_server = ""
        c.execute('SELECT link from urls WHERE header = ?', (server,))
        result = c.fetchone()
        if result:
            self.url_server = result[0]
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

        captcha = Captcha(browser)

        image, browser = captcha.get_image(self.url_server)

        browser.select_form(nr=0)
        browser.form['username'] = first_name+str(int(time.time()))[4:]
        browser.form['password'] = str(int(time.time()))[4:]
        browser.form['captcha'] = captcha.read_image(image)
        browser.submit()
        soup = BeautifulSoup(browser.response().get_data(), 'lxml')
        return  soup.get_text()
