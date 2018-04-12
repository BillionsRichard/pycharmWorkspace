# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import datetime
import os


class ToolkitPipeline(object):
    def __init__(self):
        csv_file_name = 'V2R3C00RC3_' + str(datetime.date.today()) + '.csv'
        if os.path.exists(csv_file_name):
            os.remove(csv_file_name)

        self.f = open(csv_file_name, 'a+', newline='')
        self.csv_writer = csv.writer(self.f)

        headers = ['tool_name_en', 'tool_name_cn', 'tool_size', 'release_date', 'download_count']
        self.csv_writer.writerow(headers)

    def process_item(self, item, spider):
        
        tool_name_en = item['tool_name_en']
        tool_name_cn = item['tool_name_cn']
        tool_size = item['tool_size']
        release_date = item['release_date']
        download_cnt = item['download_cnt']
        # download_url = item['download_url']

        tool_rec = [tool_name_en, tool_name_cn, tool_size, release_date, download_cnt]
        # result_file_name = 'V2R3C00RC3.csv'
        #
        # csv_writer = csv.writer(open(result_file_name, 'a+', newline=''))
        self.csv_writer.writerow(tool_rec)

    def spider_close(self, spider):
        self.f.close()
