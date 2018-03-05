from bs4 import BeautifulSoup
import mechanize, os, sqlite3

class ScrapingSKYSSH(object):
    def __init__(self):
        # Connection to database
        BASE = os.path.dirname(os.path.realpath(__file__))
        self.con = sqlite3.connect(os.path.join(BASE, 'db/urls.db'), check_same_thread=False)
        # Create table queue if not exits
        self.c = self.con.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS urls (header, link)')
        self.con.commit()
        super(ScrapingSSHDropbear, self).__init__()

    def run():
        base_urls = [
            'https://skyssh.com/ssh-list/country/singapore',
            'https://skyssh.com/ssh-list/country/japan',
            'https://skyssh.com/ssh-list/country/india',
            'https://skyssh.com/ssh-list/country/united-states',
            'https://skyssh.com/ssh-list/country/canada',
            'https://skyssh.com/ssh-list/country/netherland',
            'https://skyssh.com/ssh-list/country/united-kingdom',
            'https://skyssh.com/ssh-list/country/germany',
            'https://skyssh.com/ssh-list/country/france',
            'https://skyssh.com/ssh-list/country/australia'
        ]
        for url in base_urls:
            self.scrapper(url)

    def scrapper(url):
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        headers = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1'),
        ]

        browser.addheaders = headers

        browser.open(url)

        soup = BeautifulSoup(browser.response().get_data(), 'lxml')

        head_class = soup.findAll('div', {'class': 'pricing-v1-head'})
        footer_class = soup.findAll('div', {'class': 'pricing-v1-footer'})

        for i in range(0, len(head_class)):
            header = head_class[i].get_text().replace('\n', '').lower().replace(' ', '_')
            link = footer_class[i].findAll('a', href=True)[0]['href']
            self.c.execute('SELECT header FROM urls WHERE header = ?', (header,))
            if self.c.fetchone()[0] == header:
                self.c.execute('UPDATE urls SET link ? WHERE header = ?', (link, header))
                self.con.commit()
            else:
                self.c.execute('INSERT INTO urls (header, link) VALUES (?, ?)', (header, link))
                self.con.commit()
