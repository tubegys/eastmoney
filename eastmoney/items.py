# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from eastmoney.utils.common import get_default



class EastmoneyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class EastmoneyItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class EastMoneyAriticleItem(scrapy.Item):
    """
    东方财富网 文章内容爬虫
    """
    title = scrapy.Field()  # 文章标题
    url = scrapy.Field()  # 文章url
    publish_time = scrapy.Field()  # 文章发布时间
    comment_num = scrapy.Field(
        input_processor=MapCompose(get_default)
    )  # 文章评论数
    click_num = scrapy.Field(
        input_processor=MapCompose(get_default)
    )  # 文章点击率
    crawl_time = scrapy.Field()  # 爬取时间
