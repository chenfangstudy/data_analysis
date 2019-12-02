# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
##实训一
import numpy as np
import matplotlib.pyplot as plt
data=np.load('C:/Users/3SXL20803/Desktop/populations.npz',allow_pickle=True)
print(data.files)
print(data['data'])
print(data['feature_names'])
 
plt.rcParams['font.sans-serif']='SimHei'
name=data['feature_names']
values=data['data']
 
p1=plt.figure(figsize=(12,12))
pip1=p1.add_subplot(2,1,1)

plt.scatter(values[0:20,0],values[0:20,1],marker='8',color='red')
plt.ylabel('总人口（万人）')
plt.legend('年末')
plt.title('1996~2015年末与各类人口散点图')
 
pip2=p1.add_subplot(2,1,2)
plt.scatter(values[0:20,0],values[0:20,2],marker='o',color='yellow')
plt.scatter(values[0:20,0],values[0:20,3],marker='D',color='green')
plt.scatter(values[0:20,0],values[0:20,4],marker='p',color='blue')
plt.scatter(values[0:20,0],values[0:20,5],marker='s',color='purple')
plt.xlabel('时间')
plt.ylabel('总人口（万人）')
plt.xticks(values[0:20,0])
plt.legend(['男性','女性','城镇','乡村'])
 
 

p2=plt.figure(figsize=(12,12))
p1=p2.add_subplot(2,1,1)
plt.plot(values[0:20,0],values[0:20,1],color='r',linestyle='--',marker='8')
plt.ylabel('总人口（万人）')
plt.xticks(range(0,20,1),values[range(0,20,1),0],rotation=45)
plt.legend('年末')
plt.title('1996~2015年末总与各类人口折线图')
 
p2=p2.add_subplot(2,1,2)
plt.plot(values[0:20,0],values[0:20,2],'y-')
plt.plot(values[0:20,0],values[0:20,3],'g-.')
plt.plot(values[0:20,0],values[0:20,4],'b-')
plt.plot(values[0:20,0],values[0:20,5],'p-')
plt.xlabel('时间')
plt.ylabel('总人口（万人）')
plt.xticks(values[0:20,0])
plt.legend(['男性','女性','城镇','乡村'])
 

plt.show()



##实训二
import numpy as np
import matplotlib.pyplot as plt
 
data=np.load('C:/Users/3SXL20803/Desktop/populations.npz',allow_pickle=True)
print(data['data'])
name=data['feature_names']
values=data['data']
plt.rcParams['font.sans-serif']='SimHei'
label1=['男性','女性']
label2=['城镇','乡村']
ex=[0.01,0.01]
 
#1.直方图
p1=plt.figure(figsize=(12,12))
#子图1
a1=p1.add_subplot(2,2,1)
plt.bar(range(2),values[19,2:4],width=0.5,color='orange')
plt.ylabel('人口（万人）')
plt.ylim(0,80000)
plt.xticks(range(2),label1)
plt.title('1996年男、女人口数直方图')
 
#子图2
b1=p1.add_subplot(2,2,2)
plt.bar(range(2),values[0,2:4],width=0.5,color='red')
plt.ylabel('人口（万人）')
plt.ylim(0,80000)
plt.xticks(range(2),label1)
plt.title('2015年男、女人口数直方图')
 
#子图3
c1=p1.add_subplot(2,2,3)
plt.bar(range(2),values[19,4:6],width=0.5,color='orange')
plt.xlabel('类别')
plt.ylabel('人口（万人）')
plt.ylim(0,90000)
plt.xticks(range(2),label2)
plt.title('1996年城、乡人口数直方图')
 
#子图4
d1=p1.add_subplot(2,2,4)
plt.bar(range(2),values[0,4:6],width=0.5,color='red')
plt.xlabel('类别')
plt.ylabel('人口（万人）')
plt.ylim(0,90000)
plt.xticks(range(2),label2)
plt.title('2015年城、乡人口数直方图')
plt.savefig('F:/data/tmp/1996、2015年各类人口直方图.png')
 
#2.饼图
p2=plt.figure(figsize=(8,8))
#子图1
a2=p2.add_subplot(2,2,1)
plt.pie(values[19,2:4],explode=ex,labels=label1,colors=['pink','crimson'],autopct='%1.1f%%')
plt.title('1996年男、女人口数饼图')
 
#子图2
b2=p2.add_subplot(2,2,2)
plt.pie(values[0,2:4],explode=ex,labels=label1,colors=['PeachPuff','skyblue'],autopct='%1.1f%%')
plt.title('2015年男、女人口数饼图')
 
#子图3
c2=p2.add_subplot(2,2,3)
plt.pie(values[19,4:6],explode=ex,labels=label2,colors=['pink','crimson'],autopct='%1.1f%%')
plt.title('1996年城、乡人口数饼图')
 
#子图4
d2=p2.add_subplot(2,2,4)
plt.pie(values[0,4:6],explode=ex,labels=label2,colors=['PeachPuff','skyblue'],autopct='%1.1f%%')
plt.title('2015年城、乡人口数饼图')
plt.savefig('F:/data/tmp/1996、2015年各类人口饼图.png')
 
#3.箱线图
p3=plt.figure(figsize=(10,10))
plt.boxplot(values[0:20,1:6],notch=True,labels=['年末','男性','女性','城镇','乡村'],meanline=True)
plt.xlabel('类别')
plt.ylabel('人口（万人）')
plt.title('1996~2015年各特征人口箱线图')
plt.savefig('F:/data/tmp/1996`2015年各特征人口箱线图.png')

plt.show()















