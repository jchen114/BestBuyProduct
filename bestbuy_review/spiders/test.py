# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from bestbuy_review.items import BestbuyReviewItem
from bs4 import BeautifulSoup


class MySpider(CrawlSpider):
    name = "review"
    allowed_domains = ["bestbuy.ca"]
    start_urls = ["http://www.bestbuy.ca/en-ca/reviews/apple-rogers-apple-iphone-7-plus-128gb-smartphone-jet-black-2-year-agreement-mn4v2vc-a/10484369.aspx?"]

    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse_items(self, response):

        items = []
        print("HAHAHHA" + response.url)
        if "reviews" in response.url:
            soup = BeautifulSoup(response.body, 'html.parser')
            for review in soup.find_all("div", class_="customer-review-item"):
                review_item = BestbuyReviewItem()
                review_item['link'] = response.url
                review_item['text'] = review.findAll("p", {"itemprop" : "reviewBody"})[0].getText()

        # Return all the found items
        return items
