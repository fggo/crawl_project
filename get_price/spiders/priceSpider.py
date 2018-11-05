import scrapy


class priceSpider(scrapy.Spider):
    name = 'price' # spider name

    def start_requests(self):
        """send request to url for crawling and parse
        """
        url = "https://search.shopping.naver.com/search/all.nhn?query=" + self.product_name
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """parse the html elements and return the discount price
        """
        for row in response.css('ul.goods_list>li'):
            yield{
                "price": row.css('span.num::text').extract_first(),
            }
