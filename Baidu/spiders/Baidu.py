# encoding: utf-8
# @author: John
# @contact: BoHongtao@yeah.net
# @software: PyCharm
# @time: 2018/7/6 15:25
import scrapy,json,requests
from bs4 import BeautifulSoup
from scrapy.http import Request
from Baidu.items import BaiduItem
from pypinyin import lazy_pinyin

class Myspider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ['baidu.com']
    base_url = "http://lvyou.baidu.com/destination/ajax/jingdian?format=ajax&cid=0&playid=0&seasonid=5&surl=beijing&pn=1&rn=18"

    # 尝试申请数据
    def start_requests(self):
        yield Request(self.base_url,self.parse)

    #获最大的页码数，便于分页爬取
    def parse(self, response):
        info = json.loads(response.body)
        # 最大的页码数
        max = int(info['data']['scene_total']/18)
        for i in range(1,max+1):
            print("正在请求"+str(i)+"页数据")
            url = "http://lvyou.baidu.com/destination/ajax/jingdian?format=ajax&cid=0&playid=0&seasonid=5&surl=beijing&pn="+str(i)+"&rn=18"
            yield Request(url,self.get_page,meta={'page':i})

    # 解析json中的数据
    def get_page(self,response):
        print("解析的页码是"+str(response.meta['page']))
        per_page_info = json.loads(response.body)['data']['scene_list']
        print(per_page_info)
        for info in per_page_info:
            print("解析一个景点数据")
            # 有些参数不存在，这里使用try，其实我也不想啊
            # 中文名字
            try:
                name =  info['sname'].strip()
            except Exception:
                name = ""
            # 转换中文名字为拼音，获取景点详情链接
            pinyin_name = ''.join(lazy_pinyin(name))
            detail_url = "https://lvyou.baidu.com/"+pinyin_name.strip()

            # 英文名字
            try:
                en_name = info['ext']['en_sname'].strip()
            except Exception:
                en_name = ""

            # 星级
            try:
                level = info['ext']['level'].strip()
            except Exception:
                level = ""

            # 简介
            try:
                brief = info['ext']['sketch_desc'].strip()
            except Exception:
                brief = ""
            # 地区
            try:
                province = info['province'].strip()
            except Exception:
                province = ""

            # 地址
            try:
                address = info['ext']['address'].strip()
            except Exception:
                address = ""

            # 电话
            try:
                phone = info['ext']['phone'].strip()
            except Exception:
                phone = ""

            # web
            try:
                web = info['ext']['website'].strip()
            except Exception:
                web = ""

            # 经度
            try:
                lon = info['ext']['map_info'].split(',')[0].strip()
            except Exception:
                lon = ""

            # 纬度
            try:
                lat = info['ext']['map_info'].split(',')[1].strip()
            except Exception:
                lat = ""
            yield Request(detail_url, self.get_pic_url,meta={'name':name,'en_name':en_name,'level':level,'address':address,'phone':phone,'web':web,'lon':lon,'lat':lat,'brief':brief,'province':province})

    # # 获取景点图片url
    def get_pic_url(self,response):
        item = BaiduItem()
        item['name'] = response.meta['name']
        item['en_name'] = response.meta['en_name']
        item['level'] = response.meta['level']
        item['brief'] = response.meta['brief']
        item['address'] = response.meta['address']
        item['phone'] = response.meta['phone']
        item['web'] = response.meta['web']
        item['lon'] = response.meta['lon']
        item['lat'] = response.meta['lat']
        item['province'] = response.meta['province']

        # 获取更多美图链接
        pics_url = BeautifulSoup(response.text,'lxml').find('ul',class_="pic-slider").find_all('img')
        print(pics_url)
        # 初始化
        url1 = url2 = url3 = url4 = ""

        try:
            url1 = pics_url[0]['src']
        except Exception:
            pass

        try:
            url2 = pics_url[1]['src']
        except Exception:
            pass

        try:
            url3 = pics_url[2]['src']
        except Exception:
            pass

        try:
            url4 = pics_url[3]['src']
        except Exception:
            pass

        item['url1'] = url1
        item['url2'] = url2
        item['url3'] = url3
        item['url4'] = url4
        return item
