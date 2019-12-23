import scrapy


class FlipkartscraperItem(scrapy.Item):
    name=scrapy.Field()
    price=scrapy.Field()
    modelnumber=scrapy.Field()
    modelname=scrapy.Field()
    color=scrapy.Field()
    operatingsystem=scrapy.Field()
    displaysize=scrapy.Field()
    processortype=scrapy.Field()
    processorcore=scrapy.Field()
    internalstorage=scrapy.Field()
    resolution=scrapy.Field()
    gpu=scrapy.Field()
    ram=scrapy.Field()
    expandablestorage=scrapy.Field()
    primarycamera=scrapy.Field()
    secondarycamera=scrapy.Field()
    batterycapacity=scrapy.Field()
    warrantysummary=scrapy.Field()
