# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:47:41 2019

@author: 3SXL_21111
"""

import numpy as np
import matplotlib.pyplot as plt
data=np.load('C:/Users/3SXL_21111/Desktop/新建文件夹/populations.npz')
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
def getKeys(data):
    ks=[]
    for i in data.keys():
        ks.append(i)
    return ks
keys = getKeys(data)
values = data[keys[0]][-3::-1, :]
name = data[keys[1]] 


p = plt.figure(figsize=(15,20))
label=['男性人口','女性人口','城镇人口','乡村人口']
explode=[0.01,0.01,0.01,0.01]
gdp=(list(values[:,2]),list(values[:,3]),list(values[:,4]),list(values[:,5]))
#子图1
ax1 =p.add_subplot(3,1,1)
plt.title('1996-2015年人口数据特征间的关系直方图')
plt.xlabel('类别')
plt.ylabel('人口数（万人）')
plt.bar(range(4),values[0,2:6],width=0.5)
plt.xticks(range(4),label)
#子图2
ax2 = p.add_subplot(3,1,2)
plt.title('1996-2015年人口数据特征间的关系饼图')
plt.pie(values[0,2:6],explode=explode,labels=label,autopct='%1.1f%%')
#子图3
ax3 = p.add_subplot(3,1,3)
plt.title('1996-2015年人口数据特征间的关系箱线图')
plt.boxplot(gdp,notch=True,labels=label,meanline=True)
plt.savefig('1996~2015年人口数据特征间关系分布图.png')
plt.show()