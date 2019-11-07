# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:47:01 2019

@author: sheil
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.load('G:/Seven G/04 大四/02 python/03 第3章/03-实训数据/populations.npz',allow_pickle=True)
print(data.files)
pdata = data['data'][::-1]                #倒序
print(pdata)
name = data['feature_names']
plt.rcParams['font.sans-serif'] = 'SimHei'
p = plt.figure(figsize=(12,12))
print(name[1:6])

#散点图
ax1 = p.add_subplot(2,1,1)
plt.scatter(pdata[2:20,0],pdata[2:20,1],marker='o',c='r')#年末总人口
plt.scatter(pdata[2:20,0],pdata[2:20,2],marker='D',c='b')#男性人口
plt.scatter(pdata[2:20,0],pdata[2:20,3],marker='v',c='y')#女性人口
plt.scatter(pdata[2:20,0],pdata[2:20,4],marker='8',c='g')#城镇人口
plt.scatter(pdata[2:20,0],pdata[2:20,5],marker='p',c='c')#乡村人口
plt.legend(name[1:6])
plt.ylabel('人数(万)')
plt.xlabel('年份')
plt.title("1996~2015年人口特征分析")

#折线图
ax2 = p.add_subplot(2,1,2)
plt.plot(
    pdata[2:20,0],pdata[2:20,1],'r-',
    pdata[2:20,0],pdata[2:20,2],'b-',
    pdata[2:20,0],pdata[2:20,3],'y--',
    pdata[2:20,0],pdata[2:20,4],'g:',
    pdata[2:20,0],pdata[2:20,5],'c-',
)

plt.legend(name[1:6])
plt.ylabel('人数(万)')
plt.xlabel('年份')
plt.title("1996~2015年人口特征分析")

plt.savefig('G:/Seven G/04 大四/02 python/03 第3章/04 实训代码/1996~2015年人口特征分析.png')
plt.show()