# -*- coding: utf-8 -*-
实训1
import pandas as pd
import numpy as np
oderinfo=pd.read_table(C:\Users\Desktop\chapter_4\03-实训数据\Training_Userupdate.csv
                       ,sep=',',encoding='utf-8')
print('P2P网络贷款主表的维度为:',orderinfo.ndim)#维度
print('P2P网络贷款主表的大小为:',orderinfo.shape)#大小
print('P2P网络贷款主表的内存信息为:',orderinfo.memory_usage())#内存信息
print(orderinfo.describe())
def dropNullStd(data):
    beforelen = data.shape[1]
    colisNull = data.describe().loc['count'] == 0
    for i in range(len(colisNull)):
        if colisNull[i]:
            data.drop(colisNull.index[i],axis = 1,inplace =True)

    stdisZero = data.describe().loc['std'] == 0
    for i in range(len(stdisZero)):
        if stdisZero[i]:
            data.drop(stdisZero.index[i],axis = 1,inplace =True)
    afterlen = data.shape[1]
    print('去除的列的数目为：',beforelen-afterlen)
    print('去除后数据的形状为：',data.shape)
dropNullStd(orderinfo)

实训2
order1=pd.read_table(C:\Users\Desktop\chapter_4\03-实训数据\Training_Userupdate.csv
                       ,sep=',',encoding='utf-8')
order2=pd.read_table(C:\Users\Desktop\chapter_4\03-实训数据\Training_LogInfo.csv
                       ,sep=',',encoding='utf-8')
order1['ListingInfo1'] = pd.to_datetime(order2['ListingInfo1'])
order1['UserupdateInfo2'] = pd.to_datetime(order2['LogInfo3'])
print(order['ListingInfo1'].dtypes)
print(order['LogInfo3'].dtypes)
year1 = [i.year for i in order1['Listinginfo1']]## 提取年份信息
month1 = [i.month for i in order1['Listinginfo1']]## 提取月份信息
day1 = [i.day for i in  order1['Listinginfo1']]## 提取日期信息
year2 = [i.year for i in order2['Listinginfo1']]## 提取年份信息
month2 = [i.month for i in order2['Listinginfo1']]## 提取月份信息
day2= [i.day for i in  order2['Listinginfo1']]## 提取日期信息
time1 = order1['ListingInfo1']-order2['ListingInfo1']
time2 = order1['UserupdateInfo2']-order2['LogInfo3']
print('相差的时间为:\n',timedelta[:5])

实训3
import pandas as pd
import numpy as np
order1Group = order1[['Idx','ListingInfo1',
      'UserupdateInfo1','UserupdateInfo2']].groupby(by = 'Idx')
order2Group = order2[['Idx','ListingInfo1',
      'LogInfo1','LogInfo2','LogInfo3']].groupby(by = 'Idx')
print("最早更新时间为:\n",order1Group[['LogInfo3']].agg(['min']).head())
print("最晚更新时间为:\n",order1Group[['LogInfo3']].agg(['max']).head())
print("最早登陆时间为:\n",order2Group[['Listinginfo1']].agg(['min']).head())
print("最晚登陆时间为:\n",order2Group[['Listinginfo1']].agg(['max']).head())
print("信息更新次数:\n",order1Group.size().head())
print("登陆次数:\n",order2Group.size().head())

实训4
order1lpivot5=pd.pivot_table(order1[[
 'Idx','ListingInfo1','UserupdateInfo1','UserupdateInfo2','LogInfo1',
 'LogInfo2','LogInfo3',]],
      index = 'Idx',columns = 'ListingInfo1',
      fill_value = 0,)
print('\n',order1Pivot5)
order1Cross = pd.crosstab(
      index=order1['order_id'],
      columns=order1['ListingInfo1'],)
print(order1Cross])


