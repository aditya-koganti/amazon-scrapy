# -*- coding: utf-8 -*-
import scrapy

class SonyBudsSpider(scrapy.Spider):
    name = 'sony_buds'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    allowed_domains = ['www.amazon.com/s?k=sony+earbuds']
    start_urls = ['http://www.amazon.com/s?k=sony+earbuds/']
   
    def parse(self, response):
        buds_title = response.xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[*]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span/text()").getall()
        yield{
            'buds_titles': buds_title
        }