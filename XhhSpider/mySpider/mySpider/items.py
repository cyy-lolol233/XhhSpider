# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class xhhspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #游戏名称
    game_name = scrapy.Field()
    #游戏在线人数
    game_online = scrapy.Field()
    pass
