import numpy as np
import matplotlib.pyplot as plt
data=np.load("../data/populations.npz")
clumns=data['feature_names']
data=np.delete(data['data'],-1,0)
data2=np.delete(data,-1,0)
values=data2
label1=['男性人口','女性人口','农村人口','城镇人口']
explode1 = [0.01,0.01,0.01,0.01]
p = plt.figure(figsize=(12,12)) ##设置画布

ax1 = p.add_subplot(2,2,1)
plt.bar(range(4),values[1,4:5],width = 0.5)## 绘制散点图
plt.xlabel('年份')## 添加横轴标签
plt.ylabel('人口（万人）')## 添加y轴名称
plt.xticks(range(4),label1)
plt.title('2000年第一季度国民生产总值产业构成分布直方图') 
plt.savefig('../tmp/1996年-2015年人口特征直方图.png')
plt.show()

ax12 = p.add_subplot(2,2,2)
p = plt.figure(figsize=(6,6))
label1=['男性人口','女性人口','农村人口','城镇人口']
explode1 = [0.01,0.01,0.01,0.01]
plt.pie(values[2,2:6],explode=explode1,labels=label1,
        autopct='%1.1f%%')## 绘制散点图
plt.title('2000年第一季度国民生产总值产业构成分布饼图') 
plt.savefig('../tmp/1996年-2015年人口特征布饼图.png')
plt.show()

label1=['男性人口','女性人口','农村人口','城镇人口']
gdp1= (list(values[:,2]),list(values[:,3]),list(values[:,4]),list(values[:,5]))
plt.boxplot(gdp1,notch=True,labels = label1, meanline=True)
plt.title('2000-2017各产业国民生产总值箱线图')
plt.ylabel('人口（万人）')## 添加y轴名称
plt.savefig('../tmp/1996年-2015年人口特征箱线图.png')
plt.show()