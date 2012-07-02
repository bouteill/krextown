# Scrapy settings for the1stTimes project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'the1stTimes'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['the1stTimes.spiders']
NEWSPIDER_MODULE = 'the1stTimes.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

