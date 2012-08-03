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
    name = "the1stTimes"
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
          'parse', follow=True),
        Rule(SgmlLinkExtractor(allow=['/the1sttimes.com/?p=\d+']),
          'parse', follow=True)
    ]

    def __init__(self):
        self.queue_links = []


    def parse(self, response):
        x = HtmlXPathSelector(response)
        a_post = x.select('//div[@class="post"]/text()').extract()
        posts = x.select('//div[@class="post"]')
        #latest_entries = x.select('//li[@id="tab-latest]')
        for post in posts:
            link = post.select('a/@href').extract()
            if link not in self.queue_links:
                self.queue_links.append(link)
        '''
        for entry in latest_entries:
            link = item.select('li/a/@href').extract()
            links.append(link)
        '''

        print "DEBUG links: ",self.count_members()
        print "DEBUG links: ",self.queue_links

        #print "DEBUG post: ",post
        '''
        print "DEBUG response.url: ",response.url
        urls = response.url.split("/")
        filename = urls[-2]
        filename = filename.replace('.com', '.dotcom.')
        page_part = urls[-1]
        page_part = page_part.replace('?', '')
        page_part = page_part.replace('=', '-')
        filename = filename + page_part + ".html"
        open(filename, 'wb').write(response.body)
        '''


    def count_members(self):
        n = 0
        for item in self.queue_links:
            n += 1
        return n

