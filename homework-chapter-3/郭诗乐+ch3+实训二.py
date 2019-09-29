# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:11:51 2019

@author: sheil
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.load('G:/Seven G/04 大四/02 python/03 第3章/03-实训数据/populations.npz', allow_pickle=True)
pdata = data['data'][::-1]                           #倒序
print(pdata)
name = data['feature_names']
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
labelx = name[2:6]

ax1 = plt.figure(figsize=(20,40))                    #直方图
for i in range(20):
    ax1.add_subplot(5,4,i+1)
    plt.bar(name[2:6], pdata[i+2,2:6],width=0.5)    #pdata[0,2:6]每行是首元素的2-5行元素的值
    plt.xlabel('类型')
    plt.ylabel('人口(万)')
    plt.title(pdata[i+2][0])
plt.savefig('G:/Seven G/04 大四/02 python/03 第3章/04 实训代码/1996~2015年人口特征分析直线图')

ax2 = plt.figure(figsize=(20,40))                    #饼图
explode = [0.01,0.01,0.01,0.01]
for j in range(20):
    ax2.add_subplot(5, 4, j+1)
    plt.pie(pdata[j+2, 2:6], explode=explode,
            labels=name[2:6], autopct='%1.lf%%')
    plt.title(pdata[j+2][0])
plt.savefig('G:/Seven G/04 大四/02 python/03 第3章/04 实训代码/1996~2015年人口特征分析饼图')

gdp = (list(pdata[2:,2]), list(pdata[2:,3]),
       list(pdata[2:,4]), list(pdata[2:,5]))       # 箱线图
ax3 = plt.figure(figsize=(20,40))
plt.boxplot(gdp, notch=True, labels=name[2:6], meanline=True)
plt.title('1996~2015年人口特征分析')
plt.xlabel('类型')
plt.ylabel('人口(万)')
plt.savefig('G:/Seven G/04 大四/02 python/03 第3章/04 实训代码/1996~2015年人口特征分析箱线图')

plt.show()
