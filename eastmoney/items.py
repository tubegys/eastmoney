# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EastmoneyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class EastMoneyAriticleItem(scrapy.Item):
    """
    东方财富网 文章内容爬虫
    """
    title = scrapy.Field()  # 文章标题
    url = scrapy.Field()  # 文章url
    publish_time = scrapy.Field()  # 文章发布时间
    comment_num = scrapy.Field()  # 文章评论数
    click_num = scrapy.Field()  # 文章点击率
