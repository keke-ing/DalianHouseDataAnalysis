# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import pymongo
# import dllianjia.settings

class MongoPipeline(object):
    collection = 'lianjia_house'  # 数据库collection名称

    def __init__(self, mongo_uri, mongo_db, mongo_user, mongo_psw):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_user = mongo_user
        self.mongo_psw = mongo_psw
        # 数据库登录需要帐号密码的话
        # self.db.authenticate(settings['MONGO_USER'], settings['MONGO_PSW'])
        # self.db.authenticate(mongo_user, mongo_psw)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_user=crawler.settings.get('MONGO_USER'),
            mongo_psw=crawler.settings.get('MONGO_PSW')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        # self.db.authenticate(self.mongo_user, self.mongo_psw)


    def close(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        table = self.db[self.collection]
        data = dict(item)
        table.insert_one(data)
        return item
