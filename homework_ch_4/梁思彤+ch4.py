# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#实训1

from sqlalchemy imort create_enqine
import pandas as pd
import numpy as np

engine = create_engine('data\第4章\Training_Master.csv',sep=',',encoding="gbk")
print(pd.ndim)#维度
print(pd.shape)#大小
print(pd.memory_usage())#内存信息
print(pd.describe())
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
dropNullStd(pd)


#实训2

import pandas as pd
Master=pd.read_csv("C:\\Users\\HP\\Desktop\\实训四\\Training_Master.csv",encoding="gbk")
Userupdate=pd.read_csv("C:\\Users\\HP\\Desktop\\实训四\\Training_Userupdate.csv",encoding="gbk")

year=[i.year for i in Userupdate["ListingInfo1"].head()]
print("ListingInfo1中的前5个年份信息：",year[:5])
month=[i.month for i in Userupdate["ListingInfo1"].head()]
print("ListingInfo1中的前5个月份信息：",month[:5])
week=[i.week for i in Userupdate["ListingInfo1"].head()]
print("ListingInfo1中的前5个星期信息：",week[:5])
day=[i.day for i in Userupdate["ListingInfo1"].head()]
print("ListingInfo1中的前5个日期信息：",day[:5])

timeDeltaUserupdate=Userupdate["ListingInfo1"]-Userupdate["UserupdateInfo2"]
print("计算时间差以日期为单位：\n",timeDeltaUserupdate)
timeDelta1LogInfo=LogInfo["Listinginfo1"]-LogInfo["LogInfo3"]

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


#实训3

import pandas as pd；
import numpy as np
from sqlalchemy import create_engine

engine = create_engine('data\第4章\Training_LogInfo.csv',sep=',',encoding="gbk")
detail = pd.read_sql_table('order_detaill',con = engine')
detailGroup = detail[['order_id','counts','amounts']].groupby(by = 'order_id'）
print('分组后的登录信息表为：',detailGroup)

UpdateLate=detailGroup.agg(np.max)
print("分组后最早更新时间：",UpdateEarly)
print("分组后最晚更新时间：",UpdateLate)

UpdateTimes=detailGroup.size()
LogInTimes=LogInfoGroup.size()
print("分组后更新时间：",UpdateTimes)
print("分组后登录时间：",LogInTimes)


#实训4

import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('data\第4章\Training_LogInfo.csv',sep=',',encoding="gbk")
detail = pd.read_sql_table('order_detaill',con = engine')
detalipivot = pd.pivot_table(detaill[['order_id','counts','amounts']],index = 'order_id')

print("Master表长宽转换前的形状：",Master.shape)
print("Userupdate表长宽转换前的形状：",Userupdate.shape)
print("LogInfo表长宽转换前的形状：",LogInfo.shape)

CMaster=Master.T
print("Master表长宽转换后的形状：",CMaster.shape)
PMaster=pd.pivot_table(Master,index="Idx")
print("使用pivot_table后Master表的形状为：",PMaster.shape)
print("使用pivot_table后Master表为：",PMaster.head())

CRMaster=pd.crosstab(index=Master["Idx"],columns=Master["ListingInfo"],values=Master["ThirdParty_Info_Period2_7"],aggfunc=np.sum)
print("使用crosstab后Master表为：",CRMaster.head())
