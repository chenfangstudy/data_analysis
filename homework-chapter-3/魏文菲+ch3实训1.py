Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
import matplotlib.pyplot as plt
 #使用numpy库读取人口数据
data=np.load('C:/2345Downloads/populations.npz',allow_pickle=True)
print(data.files)#查看文件中的数组
print(data['data'])
print(data['feature_names'])
 
plt.rcParams['font.sans-serif']='SimHei'#设置中文显示
name=data['feature_names']
values=data['data']
 
p1=plt.figure(figsize=(12,12))#确定画布大小
pip1=p1.add_subplot(2,1,1)#创建一个两行一列的子图并开始绘制
#在子图上绘制散点图
plt.scatter(values[0:20,0],values[0:20,1],marker='8',color='red')
plt.ylabel('总人口（万人）')
plt.legend('年末')
plt.title('1996~2015年末与各类人口散点图')
 
pip2=p1.add_subplot(2,1,2)#绘制子图2
plt.scatter(values[0:20,0],values[0:20,2],marker='o',color='yellow')
plt.scatter(values[0:20,0],values[0:20,3],marker='D',color='green')
plt.scatter(values[0:20,0],values[0:20,4],marker='p',color='blue')
plt.scatter(values[0:20,0],values[0:20,5],marker='s',color='purple')
plt.xlabel('时间')
plt.ylabel('总人口（万人）')
plt.xticks(values[0:20,0])
plt.legend(['男性','女性','城镇','乡村'])
#在子图上绘制折线图
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
 
#显示图片
plt.show()
