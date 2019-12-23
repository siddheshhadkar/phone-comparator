import scrapy
from ..items import FlipkartscraperItem

class FlipkartCrawler(scrapy.Spider):
    name = 'flipkart'
    start_urls = [
        'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=offhttps://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_7&otracker1=AS_QueryStore_OrganicAutoSuggest_0_7&as-pos=0&as-type=RECENT&as-searchtext=mobiles'
    ]
    count = 0

    def parse(self, response):
        gendiv = response.css('._1UoZlX')
        for div in gendiv:
            items = {}

            name = div.css('._3wU53n::text').get()
            price = div.css('._2rQ-NK::text').get()
            href = div.css('._31qSD5::attr(href)').get()
            href = response.urljoin(href)

            items['name'] = name
            items['price'] = price
            items['href'] = href
            yield scrapy.Request(href, callback=self.inside, meta={'item': items})

    def inside(self, response):
        items = response.meta['item']
        
        itemlist = ["modelnumber" , "modelname" , "color" , "operatingsystem" , "displaysize" , "processortype" , "processorcore" , "internalstorage" , "resolution" , "gpu" , "ram" , "expandablestorage" , "primarycamera" , "secondarycamera" , "batterycapacity" , "warrantysummary"]
        for values in itemlist:
            items[values]=""
        
        bigdiv = response.css('._3_6Uyw')
        for div in bigdiv:
            keytext = div.css('._3-wDH3::text').get()
            keytext = keytext.replace(" ", "")
            keytext = keytext.lower()
            keyval = div.css('._3YhLQA::text').get()
            items[keytext] = keyval
        return items
