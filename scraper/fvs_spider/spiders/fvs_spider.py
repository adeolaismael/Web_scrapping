from scrapy import Request, Spider
from scrapy.loader import ItemLoader
from fvs_spider.items import FvSSpiderItem
from datetime import datetime

class FvSSpider(Spider):
    
    name = "fvs"
    allowed_domains = ['www.rayondor-bagages.fr', 'www.mesbagages.com']
    start_urls = [
        'https://www.rayondor-bagages.fr/865-bagages',
        'https://www.mesbagages.com/bagages/valises.htm' ]
    
    
    def parse(self, response):
        if "www.rayondor-bagages.fr" in response.url:
            return self.parse_rayondor(response)
        elif "www.mesbagages.com" in response.url:
            return self.parse_mesbagages(response)


    def parse_rayondor(self, response):
        articles = response.xpath('//div[@class="product-list"]')
        self.logger.info(f"Nombre d'articles trouvés : {len(articles)}")

        for article_valises in articles:
            valise = FvSSpiderItem()
            valise['nom'] = article_valises.xpath('.//h4[@itemprop="name"]/a/text()').get()
            valise['marque'] = article_valises.xpath('.//h3[@itemprop="manufacturer"]/a/text()').get()
            valise['prix'] = article_valises.xpath('.//span[@itemprop="price"]/text()').get()
            valise['lien'] = response.urljoin(article_valises.xpath('.//h4[@itemprop="name"]/a/@href').get())
            valise['image_url'] = article_valises.xpath('.//h4[@itemprop="name"]/a/@href').get()
            
            yield valise
     

    def parse_mesbagages(self, response):
        articles = response.xpath('//ul[@class="articles"]/li[contains(@class, "article")]')
        self.logger.info(f"Nombre d'articles trouvés : {len(articles)}")

        for article_valises in articles:
            valise = FvSSpiderItem()
            valise['nom'] = article_valises.xpath('.//div[@class="txt"]/a[not(contains(@class, "marque"))]/@title').get()
            valise['marque'] = article_valises.xpath('.//div[@class="txt"]/a[contains(@class, "marque")]/text()').get()
            valise['prix'] = article_valises.xpath('.//div[@class="prix"]/span[contains(@class, "new")]/text()').get()
            valise['lien'] = response.urljoin(article_valises.xpath('.//div[@class="photo"]/a/@href').get())
            valise['image_url'] = article_valises.xpath('.//div[@class="photo"]/a/@href').get()
            
            yield valise