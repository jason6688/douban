# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime

from douban.queryBuild import QueryBuild

class DoubanPipeline(object):
    def process_item(self, item, spider):

        qb = QueryBuild('127.0.0.1', 'root', 'root', 'test')
        add_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = "insert into douban(`title`,`describe`,`star`,`add_time`) values('"+item['title']+"','"+item['describe']+"','"+item['star']+"','"+add_time+"')"
        print(sql)
        #print("itme结果：")
        #print(item)
        ins = qb.query(sql)

        #print("insert 执行结果：", ins)

        return item
