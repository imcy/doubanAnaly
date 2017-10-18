# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutodoubanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 短评ID
    comment=scrapy.Field()  # 短评评论
    score=scrapy.Field()   # 短评评分
    pass
