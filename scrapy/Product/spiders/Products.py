import scrapy
from Product.items import ProductItem   

class ProductsSpider(scrapy.Spider):
    name = "Products"
    allowed_domains = ["sandbox.oxylabs.io"]
    start_urls = ["https://sandbox.oxylabs.io/products"]

    def parse(self, response):
        products = response.css('div.product-card')

        for product in products:
            relative_url = product.css('a::attr(href)').get()
            if relative_url and relative_url != "#":
                product_url = response.urljoin(relative_url)
                yield scrapy.Request(product_url, callback=self.parse_product)

        next_page = response.css('a[rel="next"]::attr(href)').get()
        if next_page and next_page != "#":
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_product(self, response):
        item = ProductItem()
        item['url'] = response.url
        item['title'] = response.css('h2.title::text').get()
        item['stock_availability'] = response.css('p.availability::text').get()
        item['stars'] = response.css('div.star-rating::attr(class)').get()
        item['description'] = response.css('p.description::text').get()
        item['price'] = response.css('div.price::text').get()
        yield item
