########################################################################################################################
# import plotnine as p9 # 包含了ggplot模块
# import pandas as pd
#
# crime = pd.read_csv("crimeRatesByState2005.csv")
# # 创建 ggplot 对象并添加图层 # 出现data显示传递问题，无法解决
# # p = (p9.ggplot(data=crime, mapping=p9.aes(x='murder', y='burglary')) + p9.geom_point(color='red'))
# # p.show()
#
# # 手动删去离散点
# crime2 = crime[crime.state != 'United States']
# crime2 = crime2[crime2.state != 'District of Columbia']
#
# p = ((p9.ggplot(data=crime2, mapping=p9.aes(x='murder', y='burglary')) +\
#       p9.geom_point(color = "green",shape = "^", size = 2.5) + p9.stat_smooth(method='loess',color='green')))
# p.show()
########################################################################################################################

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# crime = pd.read_csv("crimeRatesByState2005.csv")
#
# crime2 = crime[crime.state != "United States"]
# crime2 = crime2[crime2.state != "District of Columbia"]
# crime2 = crime2.drop(['state'],axis=1)
# crime2 =crime2.drop(['population'],axis=1)
#
# g = sns.pairplot(crime2,diag_kind="kde",plot_kws={'color': 'red'}) #hist kde种类少
# plt.show()

########################################################################################################################

# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
#
# crime = pd.read_csv("crimeRatesByState2005.csv")
# # print(list(crime.murder))
# crime2 = crime[crime.state != "United States"]
# crime2 = crime2[crime2.state != "District of Columbia"]
# z = list(crime2.population/10000)
# colors = np.random.rand(len(list(crime2.murder)))
# cm = plt.cm.get_cmap('RdYlBu')
# csv_row_name = ['forcible_rape','robbery','aggravated_assault','burglary','larceny_theft','motor_vehicle_theft']
# for i in range(1,7):
#     plt.scatter(list(crime2.murder), list(crime2.iloc[:,i]), s=z,c=z,cmap=cm, linewidth = 0.6, alpha = 0.6)
#     plt.xlabel("murder")
#     plt.ylabel(csv_row_name[i-1])
#     plt.show()

########################################################################################################################


# import numpy as np
# import math
# from itertools import groupby
# import pandas as pd
#
# birth = pd.read_csv("birthrate.csv",encoding='GBK')
# birth.dropna(subset=['2018'], inplace= True)
# dirt= {}
# data = list(round(birth ['2018'],1))
# rangenum = []
# for k,g in groupby(sorted(data),key = lambda x: int(x)):
#     lst = map(str,list(map(lambda y:divmod(int(y*10), 10)[1],list(g))))
#     dirt[k] = ' '.join(lst)
#     rangenum.append(k)
# num = list(range(rangenum[0],rangenum[-1],2))
# for i in num:
#     a = ''
#     for k in sorted(dirt.keys()):
#         if 0<= k-i <=1:
#             a = a + ' ' + dirt[k]
#         elif k-i > 1:
#             break
#     print(str(i).rjust(5),'|',a)

########################################################################################################################

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.mlab as mlab
#
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
# plt.rcParams['axes.unicode_minus']=False
# titanic=pd.read_csv('birthrate.csv',encoding='GBK')
# titanic.dropna(subset=['2018'], inplace=True)
# plt.style.use('ggplot')
# plt.hist(titanic['2018'], bins = 10, color ='steelblue', edgecolor ='k', label = 'histagram-birth-rate')
# plt.tick_params(top= 'off', right= 'off')
# plt.legend()
# plt.show()

########################################################################################################################

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.mlab as mlab
#
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
# plt.rcParams['axes.unicode_minus']=False
# titanic=pd.read_csv('./birthrate.csv',encoding='GBK')
# titanic.dropna(subset=['2018'], inplace=True)
# plt.style.use('ggplot')
# plt.hist(titanic['2018'], bins =np.arange(titanic['2018'].min(), titanic['2018'].max(),3), density= True, color ='steelblue',edgecolor ='k')
# plt.title('2018年出生直方图和密度图')
# plt.xlabel('出生率')
# plt.ylabel('频率')
# kde =mlab.GaussianKDE(titanic['2018'])
# x2 =np.linspace(titanic['2018'].min(),titanic['2018'].max(),1000)
# line2 = plt.plot(x2,kde(x2),'g-',linewidth=2)
# plt.tick_params(top='off',right='off')
# plt.show()