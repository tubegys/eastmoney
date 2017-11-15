# -*- coding: utf-8 -*-
import scrapy


class ArticleSpiderSpider(scrapy.Spider):
    name = 'article_spider'
    allowed_domains = ['www.eastmoney.com']
    start_urls = ['http://www.eastmoney.com/']

    def parse(self, response):
        pass
