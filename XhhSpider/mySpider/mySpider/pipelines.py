# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter


class XhhPipeline:
    def open_spider(self, spider):
        self.file = open('games.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['game_name', 'game_online'])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.writer.writerow([item['game_name'], item['game_online']])
        return item