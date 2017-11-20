# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from eastmoney.items import EastMoneyAriticleItem
from urllib import parse
from scrapy.http import Request


class ArticleSpiderSpider(scrapy.Spider):
    name = 'article_spider'
    allowed_domains = ['finance.eastmoney.com', 'stock.eastmoney.com',
                       'money.eastmoney.com', 'www.eastmoney.com']

    start_urls = ['http://www.eastmoney.com/']

    def parse(self, response):
        """
        爬取主页中的文章列表，再对文章进行更深爬取
        :return: 
        """
        # 获取文章url列表
        post_urls = response.css('div.mainboxr a::attr(href)').extract()
        # 提取目标url
        finance_url = [url for url in post_urls if url.startswith('http://finance')]
        print(finance_url)
        stock_url = [url for url in post_urls if url.startswith('http://stock')]
        money_url = [url for url in post_urls if url.startswith('http://money')]
        post_url = finance_url + stock_url + money_url
        print(post_url)
        print(len(post_url))

        for url in post_url:
            yield Request(url=parse.urljoin(response.url, url), callback=self.parse_detail)

    def parse_detail(self, response):
        # 通过itemloader加载item
        item_loader = ItemLoader(item=EastMoneyAriticleItem(), response=response)
        item_loader.add_css('title', 'div.newsContent h1::text')
        item_loader.add_value('url', response.url)
        item_loader.add_css('publish_time', 'div.time::text')
        item_loader.add_css('comment_num', 'div.about-left .cNumShow::text')
        item_loader.add_css('click_num', 'div.about-left .ml5::text')
        article_item = item_loader.load_item()
        yield article_item

        # pass
