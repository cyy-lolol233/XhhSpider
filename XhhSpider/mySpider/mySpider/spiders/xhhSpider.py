import scrapy
import json
import re
from urllib.parse import urlencode
from mySpider.items import xhhspiderItem


class MySpider(scrapy.Spider):


    
    name = "xhhSpider"
    start_urls = ['https://api.xiaoheihe.cn/game/get_game_list_v3/']




    def start_requests(self):
        cookies = {
  
    }

        headers = {
   
}

        params = {
       
}

        for url in self.start_urls:
            url_with_params = f"{url}?{urlencode(params)}"
            yield scrapy.Request(url=url_with_params, headers=headers, cookies=cookies, callback=self.parse)

    
    def parse(self, response):
        data = response.text
        json_data = json.loads(data)
        if json_data.get('status')!="failed":
            
         games = json_data.get('result', {}).get('games', [])
         print(games)
         for game in games:
            item = xhhspiderItem()
            item['game_name'] = game.get('name')
             # re
            online_player = game.get('online_player')
            online_player_number = re.findall(r'[^\u4e00-\u9fa5]+', online_player)
            if online_player_number:
                item['game_online'] =float(online_player_number[0]) * 10000
            else:
                item['game_online'] = 0

            print(item)   
            yield item
        else:
         self.logger.info("登录过期了，请重新登录吧")
         
         
         

       
    
        
   
