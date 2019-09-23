# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 电影ID
    movie_id = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 导演
    movie_director = scrapy.Field()
    # 演员
    movie_actor = scrapy.Field()
    # 电影类型
    movie_type = scrapy.Field()
