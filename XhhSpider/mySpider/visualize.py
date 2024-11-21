# visualize.py

import pandas as pd
import webbrowser
from datetime import datetime
from pyecharts.charts import Bar
from pyecharts import options as opts


df = pd.read_csv('games.csv')


print(df)


bar = Bar()
bar.add_xaxis(df['game_name'].tolist())
bar.add_yaxis("Online Players", df['game_online'].tolist())
bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title="steam玩家在线数排行",
        subtitle=f"数据来自于 xiaoheihe.cn 爬取时间{datetime.now()}",
       
    ),
    xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45}),
    legend_opts=opts.LegendOpts(pos_left="center")
)


bar.render('games_online_players.html')
# 打开html
webbrowser.open('games_online_players.html')

