# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # 景点名字
    name = scrapy.Field()
    # 景点英文名字
    en_name = scrapy.Field()
    # 登记
    level = scrapy.Field()
    # 简介
    brief = scrapy.Field()
    # 景点类型
    # type = scrapy.Field()

    province = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 联系电话
    phone = scrapy.Field()
    # 网站
    web = scrapy.Field()
    # 维度
    lat = scrapy.Field()
    # 经度
    lon = scrapy.Field()

    # 图片url1
    url1 = scrapy.Field()
    # 图片url2
    url2 = scrapy.Field()
    # 图片url3
    url3 = scrapy.Field()
    # 图片url4
    url4 = scrapy.Field()
