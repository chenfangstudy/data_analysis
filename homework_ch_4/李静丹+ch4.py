# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:19:24 2019

@author: 3SXL_21154
"""

import pandas as pd
import numpy as np
#读取信息表
Master=pd.read_csv("C:\\Users\\3SXL_21154\\Desktop\\shuju\\Training_Master.csv",encoding="gbk")
Userupdate=pd.read_csv("C:\\Users\\3SXL_21154\\Desktop\\shuju\\Training_Userupdate.csv",encoding="gbk")
LogInfo=pd.read_csv("C:\\Users\\3SXL_21154\\Desktop\\shuju\\Training_LogInfo.csv",encoding="gbk")



#实训一
#DataFrame的常用属性及方法
#维度
print("主表的维度是：",Master.ndim)
#形状
print("主表的形状为：",Master.shape)
#占用内存
print("主表的形状为：",Master.memory_usage().head())
#describe方法
print("主表的描述性统计为：",Master.describe())
#删除值相同或者全空的列
def DropStrNull(data):
#去除全空的列
    before=data.shape[1]
    NullCol=data.describe().loc["count"]==0
    for i in range(0,len(NullCol)):
        if NullCol[i]:
            data.drop(labels=NullCol.index[i],axis=1,inplace=True)
    StdCol=data.describe().loc["std"]==0
    for j in range(0,len(StdCol)):
        if StdCol[j]:
            data.drop(labels=StdCol.index[j],axis=1,inplace=True)
    after=data.shape[1]
    print("删除后的列数为：",before-after)
    print("删除后的形状为：",data.shape)
print("主表的删除值相同或者全空的列操作为：")
DropStrNull(Master)

#实训二
Userupdate["ListingInfo1"]=pd.to_datetime(Userupdate["ListingInfo1"])
Userupdate["UserupdateInfo2"]=pd.to_datetime(Userupdate["UserupdateInfo2"])
LogInfo["Listinginfo1"]=pd.to_datetime(LogInfo["Listinginfo1"])
LogInfo["LogInfo3"]=pd.to_datetime(LogInfo["LogInfo3"])
#ListingInfo1:year,month,week
year=[i.year for i in Userupdate["ListingInfo1"].head()]
print("ListingInfo1中的前5个年份信息：",year[:5])
month=[i.month for i in Userupdate["ListingInfo1"].head()]
print("ListingInfo1中的前5个月份信息：",month[:5])
week=[i.week for i in Userupdate["ListingInfo1"].head()]
print("ListingInfo1中的前5个星期信息：",week[:5])
day=[i.day for i in Userupdate["ListingInfo1"].head()]
print("ListingInfo1中的前5个日期信息：",day[:5])
#时间的差，分日，小时，分钟计算
timeDeltaUserupdate=Userupdate["ListingInfo1"]-Userupdate["UserupdateInfo2"]
print("计算时间差以日期为单位：\n",timeDeltaUserupdate)
timeDelta1LogInfo=LogInfo["Listinginfo1"]-LogInfo["LogInfo3"]
#将(timedelta)days转化成minute
def TransformDayIntoMinute(data):
    for i in range(0,len(data)):
        data[i]=data[i].total_seconds()/60
    return data
print("计算时间差以分钟为单位：\n",TransformDayIntoMinute(timeDeltaUserupdate))
def TransformDayIntoSecond(data):
    for i in range(0,len(data)):
        data[i]=data[i].total_seconds()
    return data 
timeDeltaUserupdate=Userupdate["ListingInfo1"]-Userupdate["UserupdateInfo2"]
print("计算时间差以秒为单位：\n",TransformDayIntoSecond(timeDeltaUserupdate))


#实训三
#对更新表和登录信息表进行分组
UserupdateGroup=Userupdate[["Idx","UserupdateInfo2"]].groupby(by="Idx")
print('分组后的登录信息表为：',UserupdateGroup)
LogInfoGroup=LogInfo[["Idx","LogInfo3"]].groupby(by="Idx")
#求取分组后的最早、最晚的更新及登录时间
UpdateEarly=UserupdateGroup.agg(np.min)
UpdateLate=UserupdateGroup.agg(np.max)
print("分组后最早更新时间：",UpdateEarly)
print("分组后最晚更新时间：",UpdateLate)
#求取分组后的数据的信息更新次数与登录次数
UpdateTimes=UserupdateGroup.size()
LogInTimes=LogInfoGroup.size()
print("分组后更新时间：",UpdateTimes)
print("分组后登录时间：",LogInTimes)



#实训四
print("Master表长宽转换前的形状：",Master.shape)
print("Userupdate表长宽转换前的形状：",Userupdate.shape)
print("LogInfo表长宽转换前的形状：",LogInfo.shape)
#使用pivot_table
CMaster=Master.T
print("Master表长宽转换后的形状：",CMaster.shape)
PMaster=pd.pivot_table(Master,index="Idx")
print("使用pivot_table后Master表的形状为：",PMaster.shape)
print("使用pivot_table后Master表为：",PMaster.head())
#使用crosstab
CRMaster=pd.crosstab(index=Master["Idx"],columns=Master["ListingInfo"],values=Master["ThirdParty_Info_Period2_7"],aggfunc=np.sum)
print("使用crosstab后Master表为：",CRMaster.head())