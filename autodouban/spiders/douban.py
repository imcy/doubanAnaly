# -*- coding: utf-8 -*-
import scrapy
from autodouban.items import AutodoubanItem
from scrapy.http import Request

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/26801052/comments?start=0&limit=20&sort=new_score&status=P']
    def parse(self, response):
        item = AutodoubanItem()
        item["name"] = response.xpath("//a[@class='']/text()").extract()
        item["comment"] = response.xpath("//p[@class='']/text()").extract()
        item["score"] = response.xpath("//span[@class='allstar50 rating' or @class='allstar40 rating' or @class='allstar30 rating' or @class='allstar20 rating' or @class='allstar10 rating']/@title").extract()
        yield item
        for i in range(1,200,20):
            url = "https://movie.douban.com/subject/26801052/comments?start=" + str(i) + "&limit=20&sort=new_score&status=P"
            print(url)
            # 自动爬虫
            yield Request(url, callback=self.parse)
        pass
