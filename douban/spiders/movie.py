# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from bs4 import BeautifulSoup

from douban.items import DoubanItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    headers = {
        "Host": "movie.douban.com",
        "Referer": "https://movie.douban.com/top250?start=225&filter=",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": '?1',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }

    def start_requests(self):
        for page in range(0, 11):
            page = page * 25
            url = "https://movie.douban.com/top250?start={0}&filter=".format(page)
            yield scrapy.Request(url, headers=self.headers, callback=self.movie_url_list_parse)

    def movie_url_list_parse(self, response):
        print('正在抓取:{0}'.format(response.url))
        url_results = []
        url_lists = response.xpath('//ol[@class="grid_view"]/li')
        for url_info in url_lists:
            url_detail = url_info.xpath('div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/@href').extract()
            url_detail = "".join(url_detail).strip()
            url_results.append(url_detail)

            yield scrapy.Request(url_detail, headers=self.headers, callback=self.detail_parse)

    def detail_parse(self, response):
        movie_id = re.findall(r'(\d+)', response.url)
        movie_id = ''.join(movie_id)
        # 电影名称
        title = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        movie_name = "".join(title).strip()
        # 导演
        director = response.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        director = "".join(director)
        # 演员
        actor, movie_type = self.get_actor(response.url)
        actor = "".join(actor).strip()
        # 电影类型

        item = DoubanItem()
        # 电影ID
        item['movie_id'] = movie_id
        # 电影名称
        item['movie_name'] = movie_name
        # 导演
        item['movie_director'] = director
        # 演员
        item['movie_actor'] = actor
        # 电影类型
        item['movie_type'] = movie_type

        yield item

    def get_actor(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.content, 'lxml')
        x = soup.find_all('div', id='info')[0]
        try:
            actor = x.find_all('span', class_="actor")[0].find_all('span', class_="attrs")
            movie_type = x.find_all('span', property='v:genre')
            movie_type_result = []
            for info in movie_type:
                info = info.text
                movie_type_result.append(info)
            movie_type_result = '/'.join(movie_type_result)
            for info in actor:
                actor_result = info.text
                return actor_result, movie_type_result
        except Exception as e:
            print(e)


if __name__ == '__main__':
    movie = MovieSpider()
    movie.get_actor("https://movie.douban.com/subject/10463953/")

