Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
import matplotlib.pyplot as plt

data = np.load('./data/pop.npz',allow_pickle=True)
pdata = data['data']
name = data['feature_names']
plt.rcParams['font.sans-serif'] = 'SimHei'
p = plt.figure(figsize=(12,12))
print(sorted(pdata[0:20,1]))
print(name[1:6])

#散点图
ax1 = p.add_subplot(2,1,1)
plt.scatter(sorted(pdata[0:20,0]),sorted(pdata[0:20,1]),marker='o',c='r')#年末总人口
plt.scatter(sorted(pdata[0:20,0]),sorted(pdata[0:20,2]),marker='D',c='b')#男性人口
plt.scatter(sorted(pdata[0:20,0]),sorted(pdata[0:20,3]),marker='v',c='y')#女性人口
plt.scatter(sorted(pdata[0:20,0]),sorted(pdata[0:20,4]),marker='8',c='g')#城镇人口
plt.scatter(sorted(pdata[0:20,0]),sorted(pdata[0:20,5]),marker='p',c='c')#乡村人口
plt.legend(name[1:6])
plt.ylabel('人数(万)')
plt.xlabel('年份')
plt.title("1996~2015年人口特征分析")

#折线图
ax2 = p.add_subplot(2,1,2)
plt.plot(
    sorted(pdata[0:20,0]),sorted(pdata[0:20,1]),'r-',
    sorted(pdata[0:20,0]),sorted(pdata[0:20,2]),'b-',
    sorted(pdata[0:20,0]),sorted(pdata[0:20,3]),'y--',
    sorted(pdata[0:20,0]),sorted(pdata[0:20,4]),'g:',
    sorted(pdata[0:20,0]),sorted(pdata[0:20,5]),'c-',
)

plt.legend(name[1:6])
plt.ylabel('人数(万)')
plt.xlabel('年份')
plt.title("1996~2015年人口特征分析")

plt.savefig('./pic/1996~2015年人口特征分析.png')
plt.show()
