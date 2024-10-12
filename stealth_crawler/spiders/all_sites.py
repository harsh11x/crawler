import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class AllSitesSpider(CrawlSpider):
    name = 'all_sites'
    
    # Initial seed URLs to start the crawling
    start_urls = ['https://example.com', 'https://anotherexample.com']
    
    # Rules to follow all links recursively
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # Extract text content from the current page
        paragraphs = response.css('p::text').getall()

        # Store the content in a dictionary (you can save it to a file/db later)
        yield {'url': response.url, 'paragraphs': paragraphs}
