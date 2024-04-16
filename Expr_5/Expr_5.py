##################### test 1 ########################
# import jieba
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
#
# # 读取文本文件
# with open('我和我的祖国.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
#
# # 使用jieba进行中文分词
# wordlist = jieba.cut(text, cut_all=False)
# wordlist = " ".join(wordlist)
#
# # 创建词云对象
# wordcloud = WordCloud( width = 1600, height = 900,font_path='simhei.ttf', background_color="white").generate(wordlist)
#
# # 显示词云图
# plt.figure(figsize=(50, 10))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()

################################### test 2 #####################

# from pyecharts.charts import Sunburst
# from pyecharts import options as opts
#
# with open('guzhai_tag.txt', 'r') as file:
#     lines = file.readlines()
#
# list_tags = []
# for i in range(0,1):
#     list_tags.append(lines[0].split(' '))
#
#
#
# data = []
#
# for i in range(0,80-1,5):
#     print(i)
#     data.append(opts.SunburstItem(name=list_tags[0][i], value= 5,
#         children=[  opts.SunburstItem(name=list_tags[0][i+1], value=1),
#                     opts.SunburstItem(name=list_tags[0][i+2], value=2),
#                     opts.SunburstItem(name=list_tags[0][i+3], value=3),
#                     opts.SunburstItem(name=list_tags[0][i+4], value=4),
#                 ]
#
# ))
#
# for i in range(80,200-1,15):
#     print(i)
#     data.append(opts.SunburstItem(name=list_tags[0][i], value= 5,
#         children=[  opts.SunburstItem(name=list_tags[0][i+1], value=1,\
#                                       children=[opts.SunburstItem(name=list_tags[0][i+2], value=2,
#                                         children=[[opts.SunburstItem(name=list_tags[0][i+8], value=2),\
#                                                 opts.SunburstItem(name=list_tags[0][i+9], value=3)]]),\
#                                                 opts.SunburstItem(name=list_tags[0][i+3], value=3,
#                                         children=[[opts.SunburstItem(name=list_tags[0][i+6], value=2),\
#                                                 opts.SunburstItem(name=list_tags[0][i+7], value=3,
#                                         children=[opts.SunburstItem(name=list_tags[0][i + 12], value=2),
#                                                   opts.SunburstItem(name=list_tags[0][i + 13], value=2)])]])]),
#                     opts.SunburstItem(name=list_tags[0][i + 4], value=1, \
#                                       children=[opts.SunburstItem(name=list_tags[0][i + 5], value=2)]),
#                     opts.SunburstItem(name=list_tags[0][i + 10], value=1, \
#                                                         children=[opts.SunburstItem(name=list_tags[0][i + 11], value=2),
#                                                                   opts.SunburstItem(name=list_tags[0][i + 14], value=2)]
#                                                         ),
#                 ]
#
# ))
#
#
#
# sunburst = (
#     Sunburst(init_opts=opts.InitOpts(width="1000px", height="600px"))
#     .add(series_name="", data_pair=data, radius=[0, "90%"])
#     .set_global_opts(title_opts=opts.TitleOpts(title="Sunburst-基本示例"))
#     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
#     .render("basic_sunburst.html")
# )


##################### test 3 ########################
import numpy as np
# import pandas as pd
# from pyecharts.globals import ThemeType
# import pyecharts.options as opts
# from pyecharts.charts import ThemeRiver
#
# df_ThemeRiver = pd.read_excel(".\complaints.xls")
# # print(df_ThemeRiver)
# # df_ThemeRiver_target = df_ThemeRiver[ (df_ThemeRiver.category == "产品质量") | (df_ThemeRiver.category == "服务态度") | (df_ThemeRiver.category == "售后服务") ]
# # df_ThemeRiver_target = df_ThemeRiver_target[ ["date", "count", "category"] ]
# # print(df_ThemeRiver_target)
#
# colors = ['red', 'green', 'blue']
#
# df_ThemeRiver.values.tolist()
# c_ThemeRiver = (
#     ThemeRiver(init_opts=opts.InitOpts(width="1000px", height="600px",theme = ThemeType.CHALK))
#     .add(
#         series_name=list(df_ThemeRiver["category"].unique()),
#         data=df_ThemeRiver.values.tolist(),
#         singleaxis_opts=opts.SingleAxisOpts(
#             pos_top="50", pos_bottom="50", type_="time",
#         ),
#
#     )
#     .set_global_opts(
#         tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line"),
#         title_opts=opts.TitleOpts(title="Python：river chart of the three changes",pos_bottom = "85%")
#     )
#     .set_colors(colors)
#     .set_series_opts(label_opts=opts.LabelOpts(is_show = 0))
#     .render("theme_river.html")
# )

# c_ThemeRiver.render_notebook()

################################### test 4 ########################################################
import json
import os

from pyecharts.commons.utils import JsCode
from pyecharts import options as opts
from pyecharts.charts import Graph, Page
from pyecharts.faker import Collector
# 可以在Jupyter Lab中渲染展示图片
from pyecharts.globals import CurrentConfig, NotebookType

CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB


def graph_weibo() -> Graph:
    with open("weibo.json", "r", encoding="utf-8") as f:
        j = json.load(f)
        nodes, links, categories, cont, mid, userl = j

    c = (
        Graph()
        .add(
            "",
            nodes,
            links,
            categories,
            repulsion=50,
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
            label_opts=opts.LabelOpts(is_show=False),  # True),#
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),  # True),#
            title_opts=opts.TitleOpts(title="Graph-微博转发关系图"),
        )
    )
    return c

c = graph_weibo()

c.load_javascript()

c.render('my_chart.html')
# c.render_notebook()