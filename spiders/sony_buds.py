# -*- coding: utf-8 -*-
import scrapy

class SonyBudsSpider(scrapy.Spider):
    name = 'sony_buds'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/s?k=sony+wf-1000xm4']
   
    def parse(self, response):
        item_name = []
        item_price = []
        
        # 2
        item_blocks = response.xpath("//text()[contains(., 'Results')]/following::div[@data-index]//text()[contains(., 'WF-1000XM4')]/ancestor-or-self::div[5]")
        
        for item in item_blocks:
            item_name.append(item.xpath(".//text()[contains(., 'Sony')]").get())
            item_price.append(item.xpath('.//descendant::span[@class="a-offscreen"][1]//text()').get())

        yield{
            # 'item_block': item_block
            'item_names': item_name,
            'item_prices': item_price
        }
        
        #================ olds ================#
        # buds_title = response.xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[*]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span/text()").getall()
        
        # whole item # 
        # 1 
        # item_blocks = response.xpath("//text()[contains(., 'Results')]/following::div[@data-index]//text()[contains(., 'WF-1000XM4')]/parent::node()/parent::a[contains(@href, 'WF-1000XM4')]/parent::node()/parent::node()/parent::node()").getall()
        