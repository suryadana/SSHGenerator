import mechanize

class lowframe(object):
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message
    def generate(self):
        browser = mechanize.Browser()