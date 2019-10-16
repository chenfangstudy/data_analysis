# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:24:24 2019

@author: 3SXL_21144
"""

将 numpy 导入为 np
导入 matplotlib.pyplot 作为 plt
数据= np.load（' C：\ Users \ 3 SXL_21154 \ .spyder-py3 / data / populations.npz '）
plt.rcParams [ ' font.sans-serif ' ] = ' SimHei '
plt.rcParams [ ' axes.unicode_minus ' ] = False
def  getKeys（data）：
    ks = []
    对于我在 data.keys（）中：
        ks.append（i）
    返回 ks
键= getKeys（数据）
值=数据[按键[ 0 ] [ - 3 :: - 1，：]
名称=数据[键[ 1 ]] 
P1 = plt.figure（figsize  =（14，7）） 

AX1 = p1.add_subplot（1，2，1）
plt.title（' 1996-2015年人口数据特征间的关系散点图'） 
plt.xlabel（'年份'）
plt.ylabel（'人口数（万人）'） 
plt.xticks（范围（0，20），数值[：，0 ]，旋转 =  45） 
plt.scatter（values [:, 0 ]，values [:, 1 ]，标记 =  ' o '，c  =  ' r '）
plt.scatter（values [:, 0 ]，values [:, 2 ]，标记 =  ' D '，c  =  ' b '）
plt.scatter（values [:, 0 ]，values [:, 3 ]，标记 =  ' h '，c  =  ' g '）
plt.scatter（values [:, 0 ]，values [:, 4 ]，marker  =  ' s '，c  =  ' y '）
plt.scatter（values [:, 0 ]，values [:, 5 ]，标记 =  ' * '，c  =  ' c '）
plt.legend（[ '年末总人口'，'男性人口'，'女性人口'，'城镇人口'，'乡村人口' ]）

AX2 = p1.add_subplot（1，2，2）
plt.title（' 1996-2015年人口数据特征间的关系折线图'）
plt.xlabel（'年份'）
plt.ylabel（'人口数（万人）'）
plt.xticks（范围（0，20），数值[：，0 ]，旋转= 45）
plt.plot（values [:, 0 ]，values [:, 1 ]，' rs- '，
        values [:, 0 ]，values [:, 2 ]，' bd-。'，
        values [:, 0 ]，values [:, 3 ]，' gh-- '，
        values [:, 0 ]，values [:, 4 ]，' y *：'， 
        values [:, 0 ]，values [:, 5 ]，' cv-。'）
plt.legend（[ '年末总人口'，'男性人口'，'女性人口'，'城镇人口'，'乡村人口' ]）
plt.savefig（'. 1996〜2015年人口数据特征间关系散点图和折线图.png '）
plt.show（）