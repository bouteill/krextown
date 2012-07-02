# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

class The1SttimesPipeline(object):
    def process_item(self, item, spider):
        return item
