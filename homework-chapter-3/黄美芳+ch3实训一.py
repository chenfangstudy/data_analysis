import numpy as np
import matplotlib.pyplot as plt
 
data=np.load('C:/Users/3SXL_21144/Desktop/mikit/populations.npz') 
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
name=data['feature_names']
values=data['data']
 
p1=plt.figure(figsize=(12,12))#设置画布
pip1=p1.add_subplot(2,1,1)
plt.scatter(values[0:20,0],values[0:20,1],marker='8',color='red')
plt.ylabel('总人口（万人）')
plt.legend('年末')
plt.title('1996~2015年末与各类人口散点图')
pip2=p1.add_subplot(2,1,2)
plt.scatter(values[0:20,0],values[0:20,2],marker='o',color='black')
plt.scatter(values[0:20,0],values[0:20,3],marker='D',color='pink')
plt.scatter(values[0:20,0],values[0:20,4],marker='p',color='blue')
plt.scatter(values[0:20,0],values[0:20,5],marker='s',color='red')
plt.xlabel('时间')#添加横轴标签
plt.ylabel('总人口（万人）')#添加纵轴标签
plt.xticks(values[0:20,0])
plt.legend(['男性','女性','城镇','乡村'])
 
p2=plt.figure(figsize=(12,12))#设置画布
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
plt.xlabel('时间')#添加横轴标签
plt.ylabel('总人口（万人）')#添加纵轴标签
plt.xticks(values[0:20,0])
plt.legend(['男性','女性','城镇','乡村'])
plt.savefig('.1996~2015年人口数据特征间关系散点图和折线图.png')
 
plt.show()
