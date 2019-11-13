Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #实训1
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
User=pd.read_csv("C:\Users\3SXL_21128\Desktop\ch4\ch4-实训数据\Training_Userupdate.csv",encoding="gbk")
Log=pd.read_csv("C:\Users\3SXL_21128\Desktop\ch4\ch4-实训数据\Training_LogInfo.csv",encoding="gbk")

#使用to_datetime函数转换用户信息更新表和登录信息表的时间字符串
User['Listinginfo1'] = pd.to_datetime(User['Listinginfo1'])
User['LogInfo3']= pd.to_datetime(User['LogInfo3'])

Log['ListingInfo1']= pd.to_datetime(Log['ListingInfo1'])
Log['UserupdateInfo2']= pd.to_datetime(Log['UserupdateInfo2'])

print(User['Listinginfo1'].dtypes)
print(User['LogInfo3'].dtypes)
print(Log['ListingInfo1'].dtypes)
print(Log['UserupdateInfo2'].dtypes)

#使用year、month、week等方法提取用户信息更新表和登录信息表的时间信息
def ymw(data):
    year = [i.year for i in data]
    month = [i.month for i in data]
    week = [i.week for i in data]
    print(year[:5]) #提取前5条数据的年份
    print(month[:5]) #提取前5条数据的月份
    print(week[:5]) #提取前5条数据的星期

ymw(User['Listinginfo1'])
ymw(User['LogInfo3'])
ymw(Log['ListingInfo1'])
ymw(Log['UserupdateInfo2'])

#计算用户信息更新表和登录信息表中两时间的差，分别以日、小时、分钟计算

timeDeltaUserupdate=Userupdate["ListingInfo1"]-Userupdate["UserupdateInfo3"]
print("用户信息更新表计算时间差以日为单位：\n",timeDeltaUserupdate)

timeDelta1LogInfo=LogInfo["Listinginfo1"]-LogInfo["LogInfo2"]
print("登录信息表计算时间差以日为单位：\n",timeDeltaUserupdate)

#换算为分钟
def TransformDayIntoMinute(data):
    for i in range(0,len(data)):
        data[i]=data[i].total_seconds()/60
    return data
print("用户信息更新表计算时间差以分钟为单位：\n",TransformDayIntoMinute(timeDeltaUserupdate))

def TransformDayIntoSecond(data):
    for i in range(0,len(data)):
        data[i]=data[i].total_seconds()
    return data 
timeDeltaUserupdate=Userupdate["ListingInfo1"]-Userupdate["UserupdateInfo3"]
print("用户信息更新表计算时间差以秒为单位：\n",TransformDayIntoSecond(timeDeltaUserupdate))

#实训3
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

#实训4
#使用pivot_table函数对用户更新时间表进行长宽表转换
Userpivot = pd.pivot_table(User,index='Idx')
print(Userpivot)

#使用crosstab方法对登录信息表进行长宽表转换
LogCross = pd.crosstab(index=pup['Idx'],columns='LogInfo')
print(LogCross)
