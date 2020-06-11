# -*- coding: utf-8 -*-
import scrapy
import json


from lxml import etree
from scrapy import Request
from dllianjia.items import HomelinkItem
# from dllianjia.dllianjia.items import omelinkItem

class LianjiaspiderSpider(scrapy.Spider):
    name = 'LianjiaSpider'
    allowed_domains = ['dl.lianjia.com']
    regions = {
        'ganjingzi': '甘井子',
        'shahekou': '沙河口',
        'zhongshan': '中山',
        'xigang': '西岗',
        'gaoxinyuanqu': '高新园区',
        'kaifaqudl': '开发区',
        'jinzhou': '金州',
        'lvshunkou': '旅顺口',
        'pulandian': '普兰店',
    }

    def start_requests(self):
        for region in list(self.regions.keys()):
            url = "https://dl.lianjia.com/chengjiao/" + region + "/"
            yield Request(url=url, callback=self.parse, meta={'region': region})  # 用来获取页码

    def parse(self, response):
        region = response.meta['region']
        selector = etree.HTML(response.text)
        sel = selector.xpath("//html/body/div[3]/div[1]/dl[2]/dd/div/div[2]/a/@href")
        for address in sel:
            url_page = "https://dl.lianjia.com{}".format(address)
            yield Request(url=url_page, callback=self.parse_region, meta={'region': region, 'address': address})  # 获取区域页码


    def parse_region(self, response):
        region = response.meta['region']
        address = response.meta['address']
        selector = etree.HTML(response.text)
        sel = selector.xpath("//div[@class='page-box house-lst-page-box']/@page-data")[0]  # 返回的是字符串字典
        sel = json.loads(sel)  # 转化为字典
        total_pages = sel.get("totalPage")
        for i in range(int(total_pages)):
            url_page = "https://dl.lianjia.com{}pg{}/".format(address, str(i + 1))
            yield Request(url=url_page, callback=self.parse_sale, meta={'region': region, 'address': address})

    def parse_sale(self, response):
        region = response.meta['region']
        address = response.meta['address']
        selector = etree.HTML(response.text)
        house_urls = selector.xpath("//div[@class='content']//div[@class='title']//a/@href")  # 返回列表
        for house_url in house_urls:
            yield Request(url=house_url, callback=self.parse_content, meta={'region': region, 'address': address})

    def parse_content(self, response):
        item = HomelinkItem()
        # 行政区
        region = response.meta['region']
        # 地理位置
        address = response.meta['address']
        item['region'] = region
        item['address'] = address.split('/')[-2]
        # 成交时间
        item["deal_time"] = ''.join(response.xpath("//section//p[@class='record_detail']/text()").re(r"\d{4}[-]\d{2}"))

        # 成交总价
        item["deal_totalPrice"] = response.xpath("//section//span/i/text()").extract_first()
        # 成交单价
        item["deal_unitPrice"] = response.xpath("//section//div[@class='price']/b/text()").extract_first()
        # 其他成交信息
        deal_info = response.xpath("//section//ul/li/text()")  # response.xpath返回选择器对象，selector.xpath有区别
        item["household_style"] = deal_info.extract()[0].strip()  # 房屋户型
        item["gross_area"] = deal_info.extract()[2].strip()  # 建筑面积
        # item["usable_area"] = deal_info.extract()[4].strip()  # 使用面积
        item["house_orientation"] = deal_info.extract()[6].strip()  # 房屋朝向
        item['house_decoration'] = deal_info.extract()[8].strip()  # 装修情况
        item["floor_number"] = deal_info.extract()[1].strip()  # 所在楼层
        item["build_year"] = deal_info.extract()[7].strip()  # 建筑年限
        item["year_of_property"] = deal_info.extract()[12].strip()  # 产权年限
        item["with_elevator"] = deal_info.extract()[13].strip()  # 配备电梯
        item["house_usage"] = deal_info.extract()[17].strip()  # 房屋用途
        item["is_two_five"] = deal_info.extract()[18].strip()  # 满二满五

        # 经纬度,小区名
        regex_latitude = '''resblockPosition(.+)'''
        regex_xiaoqu_name = '''resblockName(.+)'''
        latitude = ''.join(response.xpath('/html/body/script[11]/text()').re(regex_latitude)).strip(':').strip(
            ',').strip('\'')
        item['longitude_latitude'] = latitude
        xiaoqu_name = ''.join(response.xpath('/html/body/script[11]/text()').re(regex_xiaoqu_name)).strip(':').strip(
            ',').strip('\'')
        item['xiaoqu'] = xiaoqu_name
        yield item
