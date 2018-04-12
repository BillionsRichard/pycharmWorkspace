# -*- coding: utf-8 -*-
import scrapy
from toolkit.items import ToolkitItem

class ToolSpider(scrapy.Spider):
    name = 'tool'
    allowed_domains = ['support.huawei.com']
    start_urls = ['http://support.huawei.com/enterprise/zh/cloud-storage/oceanstor-toolkit-pid-8576706/software/22800652/?idAbsPath=fixnode01%7C7919749%7C7941815%7C9523109%7C8576706/',

                  'http://support.huawei.com/enterprise/zh/cloud-storage/oceanstor-toolkit-pid-8576706/software/22789227',
                  'http://support.huawei.com/enterprise/zh/cloud-storage/oceanstor-toolkit-pid-8576706/software/22752413/?idAbsPath=fixnode01%7C7919749%7C7941815%7C9523109%7C8576706']

    def parse(self, response):
        tools = response.xpath('//tbody[@id="softListDiv"]/tr')

        for tool in tools:
            tool_item = ToolkitItem()
            name_en = tool.xpath('./td/a/@title').extract()[0]
            name_cn = tool.xpath('./td/div[@class="spte-tool-list-desc breakword"]/text()').extract()[0].strip()

            size = tool.xpath('./td[@width="11%"]/text()').extract()[0]

            release_date = tool.xpath('./td[@width="12%"]/text()').extract()[0]

            download_cnt = tool.xpath('./td[@width="10%" and @style="text-align:center;"]/text()').extract()[0]

            tool_item['tool_name_en'] = name_en
            tool_item['tool_name_cn'] = name_cn
            tool_item['tool_size'] = size
            tool_item['release_date'] = release_date
            tool_item['download_cnt'] = download_cnt
            tool_item['download_url'] = None

            yield tool_item

