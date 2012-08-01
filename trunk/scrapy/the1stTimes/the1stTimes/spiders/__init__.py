# This package will contain the spiders of your Scrapy project
#
# To create the first spider for your project use this command:
#
#   scrapy genspider myspider myspider-domain.com
#
# For more info see:
# http://doc.scrapy.org/topics/spiders.html

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

class The1stTimes(CrawlSpider):
    name = "the1sttimes"
    allowed_domains = ["the1sttimes.com"]
    start_urls = [
        'http://the1sttimes.com/?cat=31',
        'http://the1sttimes.com/?cat=1',
        'http://the1sttimes.com/?cat=12',
        'http://the1sttimes.com/?cat=4',
        'http://the1sttimes.com/?cat=5',
        'http://the1sttimes.com/?cat=45',
        'http://the1sttimes.com/?cat=19',
        'http://the1sttimes.com/?cat=42',
        'http://the1sttimes.com/?cat=21',
        'http://the1sttimes.com/?cat=15'
    ]
    rules = [
        Rule(SgmlLinkExtractor(allow=['/the1sttimes.com/\?cat=\d+']),
          'parse'),
        Rule(SgmlLinkExtractor(allow=['/the1sttimes.com/?p=\d+']),
          'parse')
    ]

    def parse(self, response):
        x = HtmlXPathSelector(response)
        post = x.select('//div[@class="post"]/text()').extract()
        posts = x.select('//div[@class="post"]')
        latest_entries = x.select('//li[@id="tab-latest]')
        links = []
        for post in posts:
            link = post.select('a/@href').extract()
            links.append(link)
        for entry in latest_entries:
            link = item.select('li/a/@href').extract()
            links.append(link)

        print "DEBUG links: ",links

        #print "DEBUG post: ",post
        print "DEBUG response.url: ",response.url
        urls = response.url.split("/")
        filename = urls[-2]
        filename = filename.replace('.com', '.dotcom.')
        page_part = urls[-1]
        page_part = page_part.replace('?', '')
        page_part = page_part.replace('=', '-')
        filename = filename + page_part + ".html"
        open(filename, 'wb').write(response.body)

