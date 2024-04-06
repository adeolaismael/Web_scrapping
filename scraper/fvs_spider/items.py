import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst

class FvSSpiderItem(scrapy.Item):
    nom = scrapy.Field()
    marque = scrapy.Field()
    prix = scrapy.Field()
    lien = scrapy.Field()
    image_url =  scrapy.Field()