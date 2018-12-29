# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TencentJsonPipeline(object):

        def __init__(self):
                self.file = open('tencent.json', mode='w')

        def process_item(self, item, spider):
                item_dic = dict(item)
                content = json.dumps(item_dic, ensure_ascii=False) + "\n"
                self.file.write(content)
                return item

        def close_spider(self, spider):
                self.file.close()
