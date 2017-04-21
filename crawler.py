from lxml import html
import requests
import browser_cookie3



class AppCrawler:

    def __init__(self, starting_url, params, cookies):
        self.starting_url = starting_url
        self.params = params
        self.cookies = cookies

    def crawl(self):
        self.get_app_from_link(self.starting_url, self.params, self.cookies)
        return

    def get_app_from_link(self, link, params, cookies):
        
        start_page = requests.get(link, params=params, cookies=cookies)

        tree = html.fromstring(start_page.text)

        result = tree.xpath('xpath query')
        if result:
            return True
        else:
            return False


class App:
    
    def __init__(self, is_there_a_gift, gift_img):
        self.is_there_a_gift = is_there_a_gift
        self.gift_img = gift_img

    def __str__(self):
        return("Is there a gift: " + self.is_there_a_gift.encode('UTF-8') + 
        "\r\nImageUrl: " + self.gift_img.encode('UTF-8') + "\r\n")




params = (
    ('key', 'value'),
)

cj = browser_cookie3.chrome()
site = requests.get('url', cookies=cj)
cookie = site.cookies


crawler = AppCrawler('url', params, cookies=cookie)
x = crawler.crawl()
print(x)
