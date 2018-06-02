# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    runtime = scrapy.Field()
    release = scrapy.Field()
    director = scrapy.Field()
    year = scrapy.Field()
