import os
import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Sipder run函数
def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl('xhhSpider')
    process.start()

# 可视化
def run_visualize():
    os.system('python visualize.py')

# 入口函数
run_spider()

# 检查 games.csv 文件是否存在且第二行没有数据
if os.path.exists('games.csv'):
    df = pd.read_csv('games.csv')
    if df.shape[0] > 1:
        run_visualize()
