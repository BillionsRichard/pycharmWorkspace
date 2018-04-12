# -*- coding: utf-8 -*-
import os
import csv

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def process_item(self, item, spider):
        file_obj = open('meiju.csv', 'a+', newline='')
        csv_writer = csv.writer(file_obj)

        name = item.get('name')
        status = item.get('status', '')
        tv = item.get('tv', '')
        update_time = item.get('update_time', '')
        new_movie_rec = [name, status, tv, update_time]

        csv_writer.writerow(new_movie_rec)
        file_obj.close()
