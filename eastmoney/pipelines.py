# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import pymysql

class EastmoneyPipeline(object):
    def process_item(self, item, spider):
        with open('/home/gys/data/eastmoney_article', 'w') as f:
            f.write(item['title'])
            f.write(item['url'])
        return item


class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123',
                                    db='db_gys', )
