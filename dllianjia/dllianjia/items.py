# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field
# class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

class HomelinkItem(Item):
    # define the fields for your item here like:
    region=Field()                       #区域
    address = Field()                    #地理位置
    deal_time = Field()                  #成交时间
    deal_totalPrice = Field()            #成交价格
    deal_unitPrice = Field()             #成交单价
    household_style = Field()            #房屋户型
    gross_area = Field()                 #建筑面积
    # usable_area = Field()                #使用面积
    house_orientation = Field()          #房屋朝向
    house_decoration = Field()           #装修情况
    floor_number = Field()               #所在楼层
    build_year = Field()                 #建筑年代
    year_of_property = Field()           #产权年限
    with_elevator = Field()              #配备电梯
    house_usage = Field()                #房屋用途
    is_two_five = Field()                #满二满五
    longitude_latitude = Field()         #经纬度
    xiaoqu = Field()                     #小区

class XiaoquItem(Item):
    region = Field()                     #行政区域
    href = Field()                       #房源链接
    name = Field()                       #房源名称
    area = Field()                       #小区
    house_orientation = Field()          #朝向
    decoration = Field()                 #装修
    elevator = Field()                   #电梯
    floor = Field()                      #楼层高度
    build_year = Field()                 #建造时间
    deal_unitPrice = Field()             #每平米单价
    total_price = Field()                #总价

