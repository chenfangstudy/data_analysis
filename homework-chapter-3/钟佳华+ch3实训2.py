# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
data = np.load('../data/1996-2015年人口数据.npz')
name = data['columns'] 
values = data['values']
plt.rcParams['font.sans-serif'] = 'SimHei' ## 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
label1 = ['男性人口','女性人口','城市人口','乡村人口']
p = plt.figure(figsize=(12,12))
## 直方图
ax1 = p.add_subplot(2,1,1)
plt.bar(range(4),values[0,4:6],width = 0.5)
plt.ylabel('人口数（万）')
plt.xlabel('人口类型')
plt.xticks(range(4),label1)
plt.title('1996-2015年人口数据特征分析直方图') 
plt.savefig('../tmp/1996-2015年人口数据特征分析直方图.png')
#饼图
explode1 = [0.01,0.01,0.01]
explode2 = [0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01]
p = plt.figure(figsize=(12,12))
ax2 = p.add_subplot(2,1,2)
plt.pie(values[0,4:6],explode=explode1,labels=label1,
        autopct='%1.1f%%')
plt.ylabel('人口数（万）')
plt.xlabel('人口类型')
plt.title('1996-2015年人口数据特征分析饼图') 
plt.savefig('../tmp/1996-2015年人口数据特征分析饼图.png')
## 箱线图
gdp1 = (list(values[:,3]),list(values[:,4]),list(values[:,5]))
gdp2 = ([list(values[:,i]) for i in range(6,15)])
p = plt.figure(figsize=(12,12))
ax3 = p.add_subplot(2,1,3)
plt.boxplot(gdp,notch=True,labels = label1, meanline=True)
plt.ylabel('人口数（万）')
plt.xlabel('人口类型')
plt.savefig('../tmp/1996-2015年人口数据特征分析箱线图.png')
plt.show()
