# -*- coding: utf-8 -*-
import scrapy

class SonyBudsSpider(scrapy.Spider):
    name = 'sony_buds'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    allowed_domains = ['www.amazon.com/s?k=sony+earbuds']
    start_urls = ['http://www.amazon.com/s?k=sony+earbuds/']
   
    def parse(self, response):
        
        # 2
        item_block = response.xpath("//text()[contains(., 'Results')]/following::div[@data-index]//text()[contains(., 'WF-1000XM4')]/ancestor-or-self::div[5]").getall()
        
        
        yield{
            'item_block': item_block
        }
        
        #================ olds ================#
        # buds_title = response.xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[*]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span/text()").getall()
        
        # whole item # 
        # 1 
        # item_block = response.xpath("//text()[contains(., 'Results')]/following::div[@data-index]//text()[contains(., 'WF-1000XM4')]/parent::node()/parent::a[contains(@href, 'WF-1000XM4')]/parent::node()/parent::node()/parent::node()").getall()
        