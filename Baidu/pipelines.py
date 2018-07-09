# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from Baidu.items import BaiduItem
from Baidu.sql import Sql

class BaiduPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, BaiduItem):
            name = item['name']
            en_name = item['en_name']
            level = item['level']
            brief = item['brief']
            address = item['address']
            province = item['province']
            phone = item['phone']
            web = item['web']
            lon = item['lon']
            lat = item['lat']
            url1 = item['url1']
            url2 = item['url2']
            url3 = item['url3']
            url4 = item['url4']
            Sql.insert(name, en_name,level,brief,province,address,phone,web,lon,lat,url1,url2,url3,url4)
