# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class DoubanPipeline(object):
    def __init__(self):
        self.results_all = []

    def process_item(self, item, spider):
        result = [item['movie_name'], item['movie_director'], item['movie_actor'], item['movie_type']]
        self.results_all.append(result)
        return item

    def close_spider(self, spider):
        try:
            df = pd.DataFrame(data=self.results_all, columns=['电影名称', '导演', '演员', '类型'])
            df.to_csv('douban.csv', index=False, encoding="utf-8_sig")
        except Exception as e:
            print(e)