# -*- coding: utf-8 -*-

#实训1#

import numpy as np
import pandas as pd


#1.基本信息
def basic_information(detail):
    print("1.属性列表为:",detail.columns)
    print("2.数据的维度为：",detail.ndim)
    print("3.数据矩阵的格式",detail.shape)
    print("4.数据的具体信息")
    detail.info()
    print("\n")
   
    
#2.剔除整列为空或者取值相同的列

def dropNullStd(data):
    beforelen=data.shape[1]
    
    colisNull=data.describe().loc["count"] #每一列值不为空的总数
    
    for i in range(len(colisNull)):      #遍历所有的列的count
        if colisNull[i]==0 :              #筛选出计数为0，表示为空，将其删除
            data.drop(colisNull.index[i],axis=1,inplace=True)  

    
    stdisZero=data.describe().loc["std"]  #std表示每一列的标准差
    
    for i in range(len(stdisZero)):      
        if stdisZero[i]==0:
            data.drop(stdisZero.index[i],axis=1,inplace=True) 
            
    afterlen=data.shape[1]  # shape[0]表示行  shape[1]表示列
  
    print('\n剔除的列的数目为',beforelen-afterlen)  
    print("剔除数据的形状为",data.shape)  #剔除后的列表

#实训2#

#1.将用户信息转换为时间字符串
def fun1(LogInfo):
    print("进行转换前,Listinginfo1的类型为：",LogInfo["Listinginfo1"].dtypes)
    LogInfo["Listinginfo1"]=pd.to_datetime(LogInfo["Listinginfo1"])
    print("进行转换后,Listinginfo1的类型为：",LogInfo["Listinginfo1"].dtypes)
    print("\n")

#2.用year、month、week方法提取用户时间信息
def fun2(LogInfo):
    year=[i.year for i in LogInfo["Listinginfo1"]]
    month=[i.month for i in LogInfo["Listinginfo1"]]
    day=[i.day for i in LogInfo["Listinginfo1"]]
    week=[i.week for i in LogInfo["Listinginfo1"]]
    weekday=[i.weekday() for i in LogInfo["Listinginfo1"]]
    weekname=[i.weekday_name for i in LogInfo["Listinginfo1"]]

    print("登录数据表，前5条数据的年信息为",year[:5])
    print("登录数据表，前5条数据的月信息为",month[:5])
    print("登录数据表，前5条数据的日信息为",day[:5])
    print("登录数据表，前5条数据的周信息为",week[:5])
    print("登录数据表，前5条数据的星期信息为",weekday[:5])
    print("登录数据表，前5条数据的星期名信息为",weekname[:5])
    print("\n")

LogInfo=pd.read_csv(filepath2,sep=",",encoding="GBK")
fun1(LogInfo)
fun2(LogInfo)
Userupdate=pd.read_csv(filepath3,sep=",",encoding="GBK")
fun1(Userupdate)
fun2(Userupdate)

#计算时间差
timeDelta=Userupdate["Listinginfo1"]-LogInfo["Listinginfo1"]

print("以天为单位",timeDelta[:5].values/np.timedelta64(1, 'D'))
print("以小时为单位",timeDelta[:5].values/np.timedelta64(1, 'h'))
print("以分钟为单位",timeDelta[:5].values/np.timedelta64(1, 'm'))

#实训3#

#使用groupby方法对用户信息更新表和登录信息表进行分组
UserupdateGroup=Userupdate[["Idx","UserupdateInfo3"]].groupby(by="Idx")
print('分组后的登录信息表为：',UserupdateGroup)

LogInfoGroup=LogInfo[["Idx","LogInfo2"]].groupby(by="Idx")
print('分组后的登录信息表为：',LogInfoGroup)

#使用agg方法求取分组后的最早和最晚更新及登录时间
UpdateEarly=UserupdateGroup.agg(np.min)
UpdateLate=UserupdateGroup.agg(np.max)
print("分组后最早更新时间：",UpdateEarly)
print("分组后最晚更新时间：",UpdateLate)

#使用size方法求取分组后的数据的信息更新次数和登录次数
UpdateTimes=UserupdateGroup.size()
LogInTimes=LogInfoGroup.size()
print("分组后信息更新次数：",UpdateTimes)
print("分组后登录次数：",LogInTimes)

#实训4#

ponpivot = pd.pivot_table(pon,index='Idx')
pupCross = pd.crosstab(index=pup['Idx'],columns='UserupdateInfo1')
print(pupCross)