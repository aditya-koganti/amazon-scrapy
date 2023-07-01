# -*- coding: utf-8 -*-
import scrapy
import logging
class SonyBudsSpider(scrapy.Spider):
    name = 'sony_buds'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/s?k=sony+wf-1000xm4']
   
    # Global Variables
    item_name = ''
    
    def parse(self, response):
        item_name = []
        item_price = []
        item_links = []
        # 2
        item_blocks = response.xpath("//text()[contains(., 'Results')]/following::div[@data-index]//text()[contains(., 'WF-1000XM4')]/ancestor-or-self::div[5]")
        
        for item in item_blocks:
            self.item_name = item.xpath(".//text()[contains(., 'Sony')]").get()
            item_name.append(self.item_name)
            item_price.append(item.xpath('.//descendant::span[@class="a-offscreen"][1]//text()').get())
            item_link = item.xpath(".//text()[contains(., 'Sony')]/ancestor-or-self::a[1]/@href").get()
            item_links.append(item_link)

            absolute_url = f"https://www.amazon.com{item_link}"
            yield scrapy.Request(url=absolute_url, callback=self.parse_item)
       
    def parse_item(self, response):
       review_data = [self.item_name]
       commented_names = []
       commented_ratings = []
       reviews = response.xpath('//*[@data-hook="review"]')
    #    print("\n------------------------")
    #    print('reviews: \n')
    #    print(reviews)
    # #    print("\n------------------------")
       
       for review in reviews:
           commented_names_text = review.xpath('(.//descendant::*[@class="a-profile-name"]//text())[1]').get()
        #    print(commented_names)
        #    for commented_profile_name in commented_names_text:
        #        commented_names.append(commented_profile_name)
        #    commented_names.append(commented_names_text)
           
           commented_rating = review.xpath('(.//descendant::*[contains(@class, "a-icon a-icon-star")]//text())[1]').get()
           
        #    commented_ratings.append(commented_rating)
           
           review_data.append({
               'commented name': commented_names_text,
               'commented rating': commented_rating
           })                                                                                 
       print("\n------------------")
       print("\n Reviews Data: ", review_data)
       
    #    print("\n commented names: ", commented_names)
    #    print("\n commented ratings: ", commented_ratings)
    #    yield{ 
    #          "-------------------------------": "---------------------",
    #         'commented_name': commented_name,
    #          "-------------------------------": "-----------------------------"
            
    #    }
        # yield{
        #     # 'item_block': item_block
        #     'item_names': item_name,
        #     'item_prices': item_price,
        #     'item_links': item_link
        # }
        
        #================ olds ================#
        # buds_title = response.xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[*]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span/text()").getall()
        
        # whole item # 
        # 1 
        # item_blocks = response.xpath("//text()[contains(., 'Results')]/following::div[@data-index]//text()[contains(., 'WF-1000XM4')]/parent::node()/parent::a[contains(@href, 'WF-1000XM4')]/parent::node()/parent::node()/parent::node()").getall()
        