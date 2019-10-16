# -*- coding: utf-8 -*-
###############################################################################
########################           实训第1题         ##########################
###############################################################################

import numpy as np
import matplotlib.pyplot as plt
data=np.load("../data/populations.npz")
clumns=data['feature_names']
data=np.delete(data['data'],-1,0)
data2=np.delete(data,-1,0)
print(clumns)
print(data2)
values=data2
p = plt.figure(figsize=(12,12)) ##设置画布

## 子图1
ax1 = p.add_subplot(2,1,1)
plt.scatter(values[:,0],values[:,1], marker='o',c='r')## 绘制散点
plt.scatter(values[:,0],values[:,2], marker='o',c='r')## 绘制散点
plt.scatter(values[:,0],values[:,3], marker='D',c='b')## 绘制散点
plt.scatter(values[:,0],values[:,4], marker='v',c='y')## 绘制散点
plt.scatter(values[:,0],values[:,5], marker='p',c='c')## 绘制散点
plt.ylabel('人口（万人）')## 添加纵轴标签
plt.title('1996年-2015年人口特征散点图')## 添加图表标题
plt.legend(['年末人口','男性人口','女性人口','农村人口','城镇人口'])## 添加图例

ax2 = p.add_subplot(2,1,2)
plt.plot(values[:,0],values[:,1], 'r-',## 绘制折线图
         values[:,0],values[:,2], 'm-.',## 绘制折线图
         values[:,0],values[:,3], 'k--',## 绘制折线图
         values[:,0],values[:,4], 'r:',## 绘制折线图
         values[:,0],values[:,5], 'b-')## 绘制折线图
plt.legend(['男性人口','女性人口','农村人口','城镇人口'])## 添加图例([
plt.xticks(range(0,20,1),values[range(0,20,1),0],rotation=45)
plt.savefig('../tmp/1996年-2015年人口特征折线图图.png')
plt.show()


