from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import pytesseract

class Captcha(object):
    def __init__(self, bot):
        self.bot = bot
    def get_image(self, browser, link):
        browser.open(link)
        response = browser.response()
        soup = BeautifulSoup(response.get_data(), "lxml")
        src_captcha = soup.findAll('img', {'id': 'captcha_img'})[0]['src']
        img_response = browser.open_novisit(src_captcha)
        captcha = Image.open(BytesIO(img_response.read()))
        return captcha, browser
    def read_image(self, image):
        res_captcha = pytesseract.image_to_string(image, config='-psm 13')
        return str(res_captcha)
