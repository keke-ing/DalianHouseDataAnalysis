#!/usr/bin/env python
from scrapy import cmdline

cmdl = 'scrapy crawl LianjiaSpider -o chengjiao.csv'
cmdline.execute(cmdl.split())
