# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class ToolkitPipeline(object):
    def process_item(self, item, spider):
        
        tool_name_en = item['tool_name_en']
        tool_name_cn = item['tool_name_cn']
        tool_size = item['tool_size']
        release_date = item['release_date']
        download_cnt = item['download_cnt']
        # download_url = item['download_url']

        tool_rec = [tool_name_en, tool_name_cn, tool_size, release_date, download_cnt]
        result_file_name = tool_name_en.split()[2].sptit('.')[0].strip() + '.csv'

        csv_writer = csv.writer(open(result_file_name, 'a+', newline=''))
        csv_writer.writerow(tool_rec)
        

