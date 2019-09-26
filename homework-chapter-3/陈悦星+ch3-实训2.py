# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:53:50 2019

@author: 3SXL_21122
"""


import numpy as np
import matplotlib.pyplot as plt
 
data=np.load('populations.npz',allow_pickle=True)
print(data['data'])
name=data['feature_names']
values=data['data']
plt.rcParams['font.sans-serif']='SimHei'
label1=['男性','女性']
label2=['城镇','乡村']
ex=[0.01,0.01]

 
p1=plt.figure(figsize=(12,12))

a1=p1.add_subplot(2,2,1)
plt.bar(range(2),values[19,2:4],width=0.5,color='orange')
plt.ylabel('人口（万人）')
plt.ylim(0,80000)
plt.xticks(range(2),label1)
plt.title('1996年男、女人口数直方图')
 

b1=p1.add_subplot(2,2,2)
plt.bar(range(2),values[0,2:4],width=0.5,color='red')
plt.ylabel('人口（万人）')
plt.ylim(0,80000)
plt.xticks(range(2),label1)
plt.title('2015年男、女人口数直方图')
 

c1=p1.add_subplot(2,2,3)
plt.bar(range(2),values[19,4:6],width=0.5,color='orange')
plt.xlabel('类别')
plt.ylabel('人口（万人）')
plt.ylim(0,90000)
plt.xticks(range(2),label2)
plt.title('1996年城、乡人口数直方图')


d1=p1.add_subplot(2,2,4)
plt.bar(range(2),values[0,4:6],width=0.5,color='red')
plt.xlabel('类别')
plt.ylabel('人口（万人）')
plt.ylim(0,90000)
plt.xticks(range(2),label2)
plt.title('2015年城、乡人口数直方图')
plt.savefig('1996、2015年各类人口直方图.png')#保存图片
 

p2=plt.figure(figsize=(8,8))

a2=p2.add_subplot(2,2,1)
plt.pie(values[19,2:4],explode=ex,labels=label1,colors=['pink','crimson'],autopct='%1.1f%%')
plt.title('1996年男、女人口数饼图')
 

b2=p2.add_subplot(2,2,2)
plt.pie(values[0,2:4],explode=ex,labels=label1,colors=['PeachPuff','skyblue'],autopct='%1.1f%%')
plt.title('2015年男、女人口数饼图')
 

c2=p2.add_subplot(2,2,3)
plt.pie(values[19,4:6],explode=ex,labels=label2,colors=['pink','crimson'],autopct='%1.1f%%')
plt.title('1996年城、乡人口数饼图')
 

d2=p2.add_subplot(2,2,4)
plt.pie(values[0,4:6],explode=ex,labels=label2,colors=['PeachPuff','skyblue'],autopct='%1.1f%%')
plt.title('2015年城、乡人口数饼图')
plt.savefig('1996、2015年各类人口饼图.png')
 

p3=plt.figure(figsize=(10,10))
plt.boxplot(values[0:20,1:6],notch=True,labels=['年末','男性','女性','城镇','乡村'],meanline=True)
plt.xlabel('类别')
plt.ylabel('人口（万人）')
plt.title('1996~2015年各特征人口箱线图')
plt.savefig('1996`2015年各特征人口箱线图.png')
 
plt.show()