# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:20:47 2019

@author: 3SXL_21109
"""
import numpy as np
import matplotlib.pyplot as plt
data = np.load('C:/Users/3SXL_21153/Desktop/161034109+罗芷程/populations.npz')
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
p1 = plt.figure(figsize = (14, 7)) 

ax1 = p1.add_subplot(1, 2, 1)
plt.title('1996-2015年人口数据特征间的关系散点图') 
plt.xlabel('年份')
plt.ylabel('人口数（万人）') 
plt.xticks(range(0, 20), values[:, 0], rotation = 45) 
plt.scatter(values[:, 0], values[:, 1], marker = 'o', c = 'r')
plt.scatter(values[:, 0], values[:, 2], marker = 'D', c = 'b')
plt.scatter(values[:, 0], values[:, 3], marker = 'h', c = 'g')
plt.scatter(values[:, 0], values[:, 4], marker = 's', c = 'y')
plt.scatter(values[:, 0], values[:, 5], marker = '*', c = 'c')
plt.legend(['年末总人口','男性人口','女性人口','城镇人口','乡村人口'])

ax2 = p1.add_subplot(1, 2, 2)
plt.title('1996-2015年人口数据特征间的关系折线图')
plt.xlabel('年份')
plt.ylabel('人口数（万人）')
plt.xticks(range(0,20), values[:,0], rotation=45)
plt.plot(values[:,0], values[:,1], 'rs-',
        values[:,0], values[:,2], 'bd-.',
        values[:,0], values[:,3], 'gh--',
        values[:,0], values[:,4], 'y*:', 
        values[:,0], values[:,5], 'cv-.')
plt.legend(['年末总人口','男性人口','女性人口','城镇人口','乡村人口'])
plt.savefig('.1996~2015年人口数据特征间关系散点图和折线图.png')
plt.show()
