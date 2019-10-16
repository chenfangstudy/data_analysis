# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
data = np.load('../data/国民经济核算季度数据.npz')
name = data['columns']
values = data['values']## 提取其中的values数组，数据的存在位置
p = plt.figure(figsize=(12,12)) ##设置画布

## 散点图
ax1 = p.add_subplot(2,1,1)
plt.scatter(values[:,0],values[:,3], marker='o',c='r')## 绘制散点
plt.scatter(values[:,0],values[:,4], marker='D',c='b')## 绘制散点
plt.scatter(values[:,0],values[:,5], marker='v',c='y')## 绘制散点
plt.scatter(values[:,0],values[:,6], marker='8',c='g')## 绘制散点
plt.scatter(values[:,0],values[:,7], marker='p',c='c')## 绘制散点

plt.title('1996-2015年人口数据特征分析散点图')
plt.legend(['年末总人口','男性人口','女性人口','城镇人口','乡村人口'])

## 折线图
ax2 = p.add_subplot(2,1,2)
plt.plot(values[:,0],values[:,8], 'r-',## 绘制折线图
        values[:,0],values[:,9], 'b-.',## 绘制折线图
        values[:,0],values[:,10],'y--',## 绘制折线图
        values[:,0],values[:,11], 'g:',## 绘制折线图
        values[:,0],values[:,12], 'c-',## 绘制折线图
plt.xlabel('年份')
plt.ylabel('人口数（万）')
plt.legend(['年末总人口','男性人口','女性人口','城镇人口','乡村人口'])
plt.title('1996-2015年人口数据特征分析折线图')
plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation=45)
plt.savefig('../tmp/1996-2015年人口数据特征分析散点折线图.png')
plt.show()

