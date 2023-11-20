import scrapy
from ..items import GuaziItem

class FangSpider(scrapy.Spider):
    name = "fang"
    allowed_domains = ["lianjia.com"]
    start_urls = [f"https://dg.lianjia.com/ershoufang/pg{page}co32/" for page in range(0,10)]


    def parse(self, response):
        House_list = response.xpath('//ul[@class="sellListContent"]/li')
        for house in House_list:
            house_item = GuaziItem()
            house_item['name'] = house.xpath('.//div[@class="info clear"]/div[@class="title"]/a/text()').get() #获取房源信息
            house_item['place']= house.xpath('.//div[@class="positionInfo"]/a[2]/text()').get() #获取房源信息
            house_item['price']= house.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()').get() #获取房源价格
            house_item['cost'] = house.xpath('.//div[@class="unitPrice"]/span/text()').get() #获取房源造价信息
            yield house_item

            # next_page = response.xpath('//span[@class="next"]/a/@href').get()
            # if next_page:
            #     yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)







