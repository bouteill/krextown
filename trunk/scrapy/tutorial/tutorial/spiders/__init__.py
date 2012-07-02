# This package will contain the spiders of your Scrapy project
#
# To create the first spider for your project use this command:
#
#   scrapy genspider myspider myspider-domain.com
#
# For more info see:
# http://doc.scrapy.org/topics/spiders.html

from scrapy.spider import BaseSpider

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ['dmoz.org']
    start_urls = [
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/'
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
