# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field()
    authors = scrapy.Field()
    reply_nums = scrapy.Field()

class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    text = scrapy.Field()
    authors = scrapy.Field()
    repost = scrapy.Field()
    comment_nums = scrapy.Field()
    praise = scrapy.Field()
