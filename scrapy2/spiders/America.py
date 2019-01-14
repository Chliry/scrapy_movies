# -*- coding: utf-8 -*-
import scrapy
from scrapy2.items import Scrapy2Item


class AmericaSpider(scrapy.Spider):
    name = 'America'        # 爬虫名，有优先级并发等设置
    allowed_domains = ['meijutt.com']       # 防止爬虫项目自动爬取到其它网站(请求前检查是否属于这个域名下)
    start_urls = ['http://meijutt.com/new100.html']        # 第一个请求的url，所有请求的入口。得到的reaponse返回给 self.parse(self, response=response)

    def parse(self, response):
        # 正规写法
        # dom = lxml.etree.HTML(request.text)
        # dom.xpath()
        # Selector(response.text).xpath('').extract()

        # 获取剧集名
        movies = response.xpath('//html/body/div[3]/div[4]/div[1]/ul/li')
        # /h5/text()
        for move in movies:

            # . 表示在子标签上进行解析
            # xpath().extract返回[things(), things()]
            # xpath().extract_first()返回'things'
            name = move.xpath('./h5/text()').extract_first()

            item = Scrapy2Item()
            item.name = name    # item["name"] = name
            yield item      # 相当于return


