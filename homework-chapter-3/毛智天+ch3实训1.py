import numpy as np
import matplotlib.pyplot as plt

data = np.load('populations.npz')
pdata = data['data']
name = data['feature_names']
plt.rcParams['font.sans-serif'] = 'SimHei'
p = plt.figure(figsize=(12,12))
print(sorted(pdata[0:20,1]))
print(name[1:6])

#散点图
ax1 = p.add_subplot(2,1,1)
plt.scatter(sorted(pdata[0:20,0]),sorted(pdata[0:20,1]),marker='o',c='b')#年末总人口
plt.scatter(sorted(pdata[0:20,0]),sorted(pdata[0:20,2]),marker='D',c='g')#男性人口
plt.scatter(sorted(pdata[0:20,0]),sorted(pdata[0:20,3]),marker='v',c='r')#女性人口
plt.scatter(sorted(pdata[0:20,0]),sorted(pdata[0:20,4]),marker='8',c='c')#城镇人口
plt.scatter(sorted(pdata[0:20,0]),sorted(pdata[0:20,5]),marker='p',c='m')#乡村人口
plt.legend(name[1:6])
plt.ylabel('人数(万)')
plt.xlabel('年份')
plt.title("1996~2015年人口特征分析")

#折线图
ax2 = p.add_subplot(2,1,2)
plt.plot(
    sorted(pdata[0:20,0]),sorted(pdata[0:20,1]),'m-',
    sorted(pdata[0:20,0]),sorted(pdata[0:20,2]),'y-',
    sorted(pdata[0:20,0]),sorted(pdata[0:20,3]),'k--',
    sorted(pdata[0:20,0]),sorted(pdata[0:20,4]),'r:',
    sorted(pdata[0:20,0]),sorted(pdata[0:20,5]),'b-',
)

plt.legend(name[1:6])
plt.ylabel('人数(万)')
plt.xlabel('年份')
plt.title("1996~2015年人口特征分析")

plt.savefig('../tmp/1996~2015年人口特征分析.png')
plt.show()