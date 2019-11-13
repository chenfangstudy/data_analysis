# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

ppd = pd.read_csv('data\第4章\Training_Master.csv',sep=',',encoding="gbk")
print(ppd.ndim)#维度
print(ppd.shape)#大小
print(ppd.memory_usage())#内存信息
print(ppd.describe())
def dropNullStd(data):
    beforelen = data.shape[1]
    colisNull = data.describe().loc['count'] == 0
    for i in range(len(colisNull)):
        if colisNull[i]:
            data.drop(colisNull.index[i],axis=1,inplace=True)
    
    stdisZero = data.describe().loc['std'] == 0
    for i in range(len(stdisZero)):
        if stdisZero[i]:
            data.drop(stdisZero.index[i],axis=1,inplace=True)
    afterlen = data.shape[1]
    print('剔除的列的数目为：',beforelen-afterlen)
    print('剔出后数据的形状为：',data.shape)
dropNullStd(ppd)

#实训2
#使用to_datetime函数转换用户信息更新表和登录信息表的时间字符串

pon = pd.read_csv('data\第4章\Training_LogInfo.csv',sep=',',encoding='gbk')
pup = pd.read_csv('data\第4章\Training_Userupdate.csv',sep=',',encoding='gbk')

pon['Listinginfo1'] = pd.to_datetime(pon['Listinginfo1'])
pon['LogInfo3']= pd.to_datetime(pon['LogInfo3'])
pup['ListingInfo1']= pd.to_datetime(pup['ListingInfo1'])
pup['UserupdateInfo2']= pd.to_datetime(pup['UserupdateInfo2'])

print(pon['Listinginfo1'].dtypes)
print(pon['LogInfo3'].dtypes)
print(pup['ListingInfo1'].dtypes)
print(pup['UserupdateInfo2'].dtypes)

#使用year、month、week等方法提取用户信息更新表和登录信息表中的信息
def ymw(data):
    year = [i.year for i in data]
    month = [i.month for i in data]
    week = [i.week for i in data]
    print(year[:5])
    print(month[:5])
    print(week[:5])

ymw(pon['Listinginfo1'])
ymw(pon['LogInfo3'])
ymw(pup['ListingInfo1'])
ymw(pup['UserupdateInfo2'])

#计算用户信息更新表和登陆信息表中两时间的差，分别以日、小时、分钟计算
def userTimedelta(bdata,rdata):
    timedelta = pd.to_datetime(bdata) - pd.to_datetime(rdata)
    print('减去后的数据:',timedelta[:5])
    print('数据类型:',timedelta[:5])

userTimedelta(pon['Listinginfo1'],pon['LogInfo3'])
userTimedelta(pup['ListingInfo1'],pup['UserupdateInfo2'])

#实训3
#使用groupby方法对用户信息更新表和登录信息表进行分组
detailGroup = detail[['order_id','counts','amounts']].groupby(by = 'order_id')
print('分组后的登录信息表为：',detailGroup)

LogInfoGroup=LogInfo[["Idx","LogInfo2"]].groupby(by="Idx")
print('分组后的登录信息表为：',LogInfoGroup)


#使用agg方法求取分组后的最早和最晚更新及登录时间
UpdateEarly=UserupdateGroup.agg(np.min)
UpdateLate=UserupdateGroup.agg(np.max)
print("分组后最早更新时间：",UpdateEarly)
print("分组后最晚更新时间：",UpdateLate)

#使用size方法求取分组后的数据的信息更新次数和登录次数
ponidgp = UserupdateGroup.size()
LogInTimes=LogInfoGroup.size()
print("分组后信息更新次数：",ponidgp)
print("分组后登录次数：",LogInTimes)

#实训4
#使用pivot_table函数对用户更新时间表进行长宽表转换
ponpivot = pd.pivot_table(pon,index='Idx')
print(ponpivot)

#使用crosstab方法对登录信息表进行长宽表转换
LogCross = pd.crosstab(index=pup['Idx'],columns='LogInfo')
print(LogCross)