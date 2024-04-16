# 在学校电脑上做的实验，对于文件读取需要修改路径
#
#


import matplotlib.pyplot as plt
import seaborn as sns

# 数据
time = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
postage_prices = [0.32, 0.32, 0.32, 0.32, 0.33, 0.33, 0.34, 0.37, 0.37, 0.37, 0.37, 0.39, 0.41, 0.42, 0.44]

# 阶梯图（步进图）使用matplotlib
plt.figure(figsize=(10, 5))
plt.step(time, postage_prices, where='post', label='Step Plot')
plt.ylim([0.2, 0.5])  # 设置y轴的最小值和最大值
plt.title('1995-2009 U.S. Postage Prices')
plt.xlabel('Year')
plt.ylabel('Postage Price')
plt.grid(True)
plt.legend()
plt.show()

# 折线图使用seaborn
plt.figure(figsize=(10, 5))
sns.lineplot(x=time, y=postage_prices, label='Line Plot')
plt.ylim([0.2, 0.5])  # 设置y轴的最小值和最大值
plt.title('1995-2009 U.S. Postage Prices')
plt.xlabel('Year')
plt.ylabel('Postage Price')
plt.grid(True)
plt.legend()
plt.show()

###############################################################

import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件，并指定需要读取的列名
df = pd.read_csv('C:\\Users\\Teacher\\Downloads\\world-population.csv', usecols=['Year', 'Population'])

# 绘制折线图
plt.plot(df['Year'], df['Population'], marker='o')

# 设置图表标题和坐标轴标签
plt.title('World Population Line Chart')
plt.xlabel('Year')
plt.ylabel('Population')

# 显示图表
plt.show()

##############################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取CSV文件
df = pd.read_csv(r'C:\Users\Teacher\Downloads\unemployment-rate-1948-2010.csv')

# 按年份分组并计算每年的平均失业率
yearly_average = df.groupby('Year')['Value'].mean().reset_index()

# 确保列名是正确的
x_column = 'Year'
y_column = 'Value'

# 绘制原始数据的折线图
plt.plot(yearly_average[x_column], yearly_average[y_column], marker='o', label='original data')

# 使用numpy的polyfit进行曲线拟合，这里我们使用二次拟合作为示例
# 您可以根据需要调整多项式的阶数
p = np.polyfit(yearly_average[x_column], yearly_average[y_column], 2)
poly_fn = np.poly1d(p)

# 创建用于绘制拟合曲线的x值范围
x_fit = np.linspace(yearly_average[x_column].min(), yearly_average[x_column].max(), 100)
y_fit = poly_fn(x_fit)

# 绘制拟合曲线
plt.plot(x_fit, y_fit, color='red', label='fit curve')

# 设置图表标题和坐标轴标签
plt.title('line graph fitted to curve')
plt.xlabel('Year')
plt.ylabel('yearly average unemployment')

# 显示图例
plt.legend()

# 显示图表
plt.show()


##########################################################

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

# 读取CSV文件
df = pd.read_csv(r'C:\Users\Teacher\Downloads\flowingdata_subscribers.csv')

# 将日期列转换为日期格式
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%Y')

# 提取年份和月份，因为我们只关心2010年1月份的数据
df['YearMonth'] = df['Date'].dt.to_period('M')

# 筛选出2010年1月份的数据
df_jan_2010 = df[df['YearMonth'] == '2010-01']

# 绘制散点图
plt.figure(figsize=(10, 5))  # 设置图表大小
plt.scatter(df_jan_2010['Date'], df_jan_2010['Subscribers'],
            s=60, color='green', marker='o', alpha=0.6, label='Subscribers')

# 设置x轴为日期格式
plt.gcfmt_x = mdates.DateFormatter('%d-%m')  # 设置x轴日期格式

# 设置图表标题和坐标轴标签
plt.title('Scatter plot')
plt.xlabel('Date')
plt.ylabel('Subscribers_Sum')

# 显示图例
plt.legend()

# 显示图表
plt.grid(True)  # 添加网格
plt.show()

###############################################################

import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv(r'C:\Users\Teacher\Desktop\hot-dog-contest-winners.csv')

# 确保数据按年份排序
df.sort_values('Year', inplace=True)

# 绘制柱状图
plt.figure(figsize=(12, 6))  # 设置图形大小
plt.bar(df['Year'], df['Dogs eaten'], color='skyblue')

# 设置图表标题和坐标轴标签
plt.title('result of the last thirty years\' competion')
plt.xlabel('Year')
plt.ylabel('Eated hot dogs')

# 添加数据标签到每个柱子上
for index, value in enumerate(df['Dogs eaten']):
    plt.text(index, value, str(round(value, 2)), ha='center', va='bottom')

# 显示网格线
plt.grid(True, axis='y', alpha=0.75)

# 显示图表
plt.tight_layout()  # 确保布局不会重叠
plt.show()

#############################################################

import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv(r'C:\Users\Teacher\Downloads\hot-dog-places.csv', header=None)

# 设置列名为年份
df.columns = pd.date_range(start='2000', periods=len(df.columns), freq='A')

# 设置堆叠柱形图的标签
labels = df.columns.strftime('%Y').tolist()

# 创建堆叠柱形图
fig, ax = plt.subplots()

# 绘制每位选手的数据
# 第一个选手
ax.bar(labels, df.iloc[1], label='top 3')
# 第二个选手，堆叠在第一个选手的数据上
ax.bar(labels, df.iloc[2], bottom=df.iloc[1], label='top 2')
# 第三个选手，堆叠在前两个选手的数据上
ax.bar(labels, df.iloc[3], bottom=df.iloc[2]+df.iloc[1], label='top 1')

# 设置图表标题和坐标轴标签
ax.set_title('stack bar tor the top')
ax.set_xlabel('Year')
ax.set_ylabel('Score')

# 设置x轴刻度标签的位置和旋转角度
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=45)

# 显示图例
ax.legend()

# 显示图表
plt.tight_layout()  # 确保布局不会重叠
plt.show()

