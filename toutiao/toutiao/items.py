# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ToutiaoItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    abstract = Field()
    tag = Field()
    behot_time = Field()

    group_id = Field()

    article = Field()
    header = Field()
