import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

data = np.load('./data/populations.npz', allow_pickle=True)
pdata = data['data'][::-1]#倒序
name = data['feature_names']
labelx = name[2:6]
# 直方图
p1 = plt.figure(figsize=(20, 40))
for i in range(20):
    p1.add_subplot(5, 4, i+1)
    plt.bar(name[2:6], pdata[i+2, 2:6], width=0.5)#pdata[0,2:6]每行是首元素的2-5行元素的值
    plt.xlabel('类型')
    plt.ylabel('人口(万)')
    plt.title(pdata[i+2][0])

plt.savefig('./pic/1996~2015年人口特征分析直线图')
#饼图
p2 = plt.figure(figsize=(20, 40))
explode = [0.01, 0.01, 0.01, 0.01]
for j in range(20):
    p2.add_subplot(5, 4, j+1)
    plt.pie(pdata[j+2, 2:6], explode=explode,
            labels=name[2:6], autopct='%1.lf%%')
    plt.title(pdata[j+2][0])
plt.savefig('./pic/1996~2015年人口特征分析饼图')

# 箱线图
gdp = (list(pdata[2:, 2]), list(pdata[2:, 3]),
       list(pdata[2:, 4]), list(pdata[2:, 5]))
p3 = plt.figure(figsize=(20, 40))
plt.boxplot(gdp, notch=True, labels=name[2:6], meanline=True)
plt.title('1996~2015年人口特征分析')
plt.xlabel('类型')
plt.ylabel('人口(万)')
plt.savefig('./pic/1996~2015年人口特征分析箱线图')


plt.show()
