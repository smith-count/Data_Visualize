import matplotlib.pyplot as plt

Intersted_area = ['finance','medical care','Marketing industry','retail trade',\
'manufacturing','judicial','Engineering and Science','Insurance industry' ,'other']
Number_of_tickets = [172,136,135,101,80,68,50,29,41]

colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'grey', 'lightgreen', 'lightskyblue']  # 各个部分的颜色

# 绘制饼图
fig1, ax1 = plt.subplots()
ax1.pie(Number_of_tickets, labels=Intersted_area, colors=colors, autopct='%1.1f%%', startangle=90)

plt.show()


import matplotlib.pyplot as plt

# 环数据
labels_outer = ['finance','medical care','Marketing industry','retail trade',\
'manufacturing','judicial','Engineering and Science','Insurance industry' ,'other']
sizes_outer = [172,136,135,101,80,68,50,29,41]  # 外层饼图各部分的大小
colors_outer = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'grey', 'lightgreen', 'lightskyblue']  # 外层饼图的颜色


# 绘制外层饼图
fig, ax = plt.subplots()
ax.pie(sizes_outer, labels=labels_outer, colors=colors_outer, startangle=90, radius=1,
       wedgeprops=dict(width=0.75, edgecolor='w'))

# 显示图表
plt.show()
#
# Problems = ['racial problem','education','terrorist activities','energy policy','foreign affairs',\
# 'environment','Religious policies','tax revenue','Healthcare policies','economic','employment policy',\
# 'trade policy','Immigrants']
# Supporters = [52,49,48,47,44,43,41,41,40,38,36,31,29]
# Opposers = [38,40,45,42,48,51,53,54,57,59,57,64,62]
# Mute = [10,11,7,11,8,6,6,5,3,3,7,5,9]
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# # 数据
# N = 13  # 分类的数量
#
# ind = np.arange(N)  # 分类的x坐标
# width = 0.4  # 柱子的宽度
#
# # 绘制第一组数据（底层）
# p1 = plt.bar(ind, Supporters, width, color='blue')
#
# # 绘制第二组数据（堆叠在第一组数据上），设置bottom参数为第一组数据
# p2 = plt.bar(ind, Opposers, width, bottom=Supporters, color='green')
#
# # 第三组数据
# bottom_list = [a+b for a,b in zip(Supporters,Opposers)]
# p3 = plt.bar(ind, Mute, width, bottom=bottom_list, color='red')
#
# # 添加一些文本标签和标题
# plt.ylabel('Population')
# plt.title('Stack graph for voting data graph')
# plt.xticks(ind, Problems, rotation=45)
#
#
#
# plt.yticks(np.arange(0, 40, 10))
# plt.legend((p1[0], p2[0],p3[0]), ('Support', 'Oppose','Mute'))
#
# # 显示图形
# plt.show()
#
#
# #
# # A = [2, 1, 12, 4, 2, 1, 1, 3, 12, 3, 4, None, 9]
# # B = [4, 2, 5, 10, 3, 4, 2, 7, 4, -10, None, 8, 3, 1]
# # C = [3, 8, 3, 3, 5, 3, 3, 5, 4, 12]
# # D = [23, 18]
# # E = [1, 2, 1, 2, 3, 3, 1, 2, 3,4, 3, 1, 2, 1, 1, 1, 1, 1]
# # F = [31]
# # G = [5, 9.3, 8.1, 12, 4, 3, 2]
# # H = [12, 3, 3]
#
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# # 数据集
# A = [2, 1, 12, 4, 2, 1, 1, 3, 12, 3, 4, None, 9]
# B = [4, 2, 5, 10, 3, 4, 2, 7, 4, -10, None, 8, 3, 1]
# C = [3, 8, 3, 3, 5, 3, 3, 5, 4, 12]
# D = [23, 18]
# E = [1, 2, 1, 2, 3, 3, 1, 2, 3, 4, 3, 1, 2, 1, 1, 1, 1, 1]
# F = [31]
# G = [5, 9.3, 8.1, 12, 4, 3, 2]
# H = [12, 3, 3]
#
# # 忽略None和负数，并转换为列表（如果需要）
# datasets = [
#     [x for x in A if x is not None and x >= 0],
#     [x for x in B if x is not None and x >= 0],
#     C,
#     D,
#     E,
#     F,
#     G,
#     H
# ]
#
# # 为每个数据集创建条形图
# fig, axs = plt.subplots(nrows=len(datasets), ncols=1, figsize=(10, 15))
#
# for i, dataset in enumerate(datasets):
#     # 计算数据集的长度，并确定条形图的x位置
#     n = len(dataset)
#     x = np.arange(n)
#
#     # 绘制条形图
#     axs[i].bar(x, dataset, color='b')
#
#     # 设置标题和标签
#     axs[i].set_title(f'Module {chr(65 + i)}')
#     axs[i].set_xlabel('Index')
#     axs[i].set_ylabel('Value')
#
#     # 如果数据集只有一个元素，则移除x轴标签
#     if n == 1:
#         axs[i].set_xticks([])
#
#     # 调整子图间距
# plt.tight_layout()
#
# # 显示图形
# plt.show()


# import os
# import json
# import codecs
# from pyecharts import Tree
# with codecs.open(os.path.json.join("./","module_level.json"),"r",encoding="utf-8")as f:
#      j = json.load(f)
# data = [j]
# tree = Tree(width=1200, height=800)
# tree.add("",data)
# tree.render('./Tree.html')

# import matplotlib.pyplot as plt
# import squarify
# import pandas as pd
#
# # 假设你有一个DataFrame，其中包含层次化数据
# # 这里我们使用一个简单的例子
#
# # A = [2, 1, 12, 4, 2, 1, 1, 3, 12, 3, 4, None, 9]
# # B = [4, 2, 5, 10, 3, 4, 2, 7, 4, -10, None, 8, 3, 1]
# # C = [3, 8, 3, 3, 5, 3, 3, 5, 4, 12]
# # D = [23, 18]
# # E = [1, 2, 1, 2, 3, 3, 1, 2, 3, 4, 3, 1, 2, 1, 1, 1, 1, 1]
# # F = [31]
# # G = [5, 9.3, 8.1, 12, 4, 3, 2]
# # H = [12, 3, 3]
# data = {
#     'Name': ['A.1','A.2','A.3','A.4','A.5','A.6','A.7','A.8','A.9','A.10','A.11','A.12',\
#               'B.1','B.2','B.3','B.4','B.5','B.6','B.7','B.8','B.9','B.10','B.11','B.12','B.13', \
#               'C.1', 'C.2', 'C.3', 'C.4','C.5', 'C.6', 'C.7', 'C.8', 'C.9', 'C.10',\
#               'D.1','D.2',\
#               'E.1','E.2','E.3','E.4','E.5','E.6','E.7','E.8','E.9','E.10','E.11','E.12','E.13','E.14','E.15','E.16','E.17','E.18',\
#               'F.1','G.1','G.2','G.3','G.4','G.5','G.6','G.7',\
#               'H.1','H.2','H.3'],
#     'Value': [2, 1, 12, 4, 2, 1, 1, 3, 12, 3, 4, 9,\
#               4, 2, 5, 10, 3, 4, 2, 7, 4, -10, 8, 3, 1,\
#               3, 8, 3, 3, 5, 3, 3, 5, 4, 12,\
#               23, 18,\
#               1, 2, 1, 2, 3, 3, 1, 2, 3, 4, 3, 1, 2, 1, 1, 1, 1, 1,\
#               31,5, 9.3, 8.1, 12, 4, 3, 2,\
#               12, 3, 3]
# }
# df = pd.DataFrame(data)
#
# # 设置层次化索引，以便squarify能够理解数据的层次结构
# df = df.set_index('Name')
# df = df.sort_values('Value', ascending=False)
#
# # 绘制矩形树图
# fig, ax = plt.subplots(figsize=(10, 7))
# squarify.plot(sizes=df['Value'], label=df.index, alpha=.8)
#
# # 设置标题和轴标签
# plt.title('Rectangular Tree Diagram')
# plt.axis('off')  # 关闭坐标轴
#
# # 显示图形
# plt.show()

# from pyecharts.charts import Line
# import pandas as pd
# year_population_age =pd.read_csv('./us_population_by_age.csv')
# #面积折线图
# line3 = Line()
# # ['under 5','between 20-44','between 45-64','over 64']
# line3.add_xaxis(list(year_population_age['year']))
#
# # year	year_under5	year5_19	year20_44	year45_64	year65above
#
#
# line3.add_yaxis(year_population_age['year'][0],list(year_population_age['year_under5']),areastyle_opts=0.8)
# line3.add_yaxis(year_population_age['year'][1],list(year_population_age['year5_19']),areastyle_opts=0.8)
# line3.add_yaxis(year_population_age['year'][2],list(year_population_age['year20_44']),areastyle_opts=0.8)
# line3.add_yaxis(year_population_age['year'][3],list(year_population_age['year45_64']),areastyle_opts=0.8)
# line3.add_yaxis(year_population_age['year'][4],list(year_population_age['year65above']),areastyle_opts=0.8)
#
# line3.render(path='./area.html')

