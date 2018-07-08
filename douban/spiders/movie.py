# -*- coding: utf-8 -*-
import scrapy

from douban.items import DoubanItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = DoubanItem()
        lists = response.xpath("//div[@class='article']/ol//li")

        for list in lists:
            title = list.xpath(".//div[@class='hd']/a/span[@class='title']/text()").extract_first()
            item['title'] = title
            #print("电影标题：")
            #print(title)
            describe = list.xpath(".//div[@class='bd']/p/text()").extract_first()
            item['describe'] = describe
            #print("电影描述：")
            #print(describe)
            star = list.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract_first()
            item['star'] = star
            print("电影评分：",star)
            yield item

        pass
