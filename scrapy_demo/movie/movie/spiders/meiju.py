# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')

        for each_movie in movies:
            item = MovieItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]

            sta_lst = each_movie.xpath('./span[@class="state1 new100state1"]/text()').extract()
            sta = sta_lst[0].strip() if sta_lst else None
            if not sta:
                sta = each_movie.xpath('./span[@class="state1 new100state1"]/font/text()').extract()[0]
            else:
                sta = sta_lst[0].strip()
            item['status'] = sta

            tv = each_movie.xpath('./span[@class="mjtv"]/text()').extract()
            item['tv'] = tv[0] if tv else None

            lst_update_tm = each_movie.xpath('./div[@class="lasted-time new100time fn-right"]/text()').extract()
            lst_up_time = lst_update_tm[0] if lst_update_tm else None
            if not lst_up_time:
                lst_up_time = each_movie.xpath('./div[@class="lasted-time new100time fn-right"]/font/text()').extract()[0]
            item['update_time'] = lst_up_time

            yield item
