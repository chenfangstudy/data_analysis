
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-

#实训1
import pandas as pd
Master=pd.read_csv("..\data\Training_Master.csv",encoding="gbk")
Userupdate=pd.read_csv("..\data\Training_Userupdate.csv",encoding="gbk")
LogInfo=pd.read_csv("..\data\raining_LogInfo.csv",encoding="gbk")

print("主表的维度为：",Master.ndim)
print("用户信息更新表的维度为：",Userupdate.ndim) #用ndim查看维度
print("登录信息表的维度为：",LogInfo.ndim)

print("主表的形状为：",Master.shape)
print("用户信息更新表的形状为：",Userupdate.shape)  #用shape查看大小
print("登录信息表的形状为：",LogInfo.shape)

print("主表的形状为：",Master.memory_usage().head())
print("用户信息更新表的形状为：",Userupdate.memory_usage().head())   #用memory_usage查看占用内存信息
print("登录信息表的形状为：",LogInfo.memory_usage().head())

print("主表的索引为：",Master.index)
print("主表的值为：",Master.values)
print("主表的列名为：",Master.columns)
print("主表的数据类型为：",Master.dtypes)
print("主表的元素个数为：",Master.size)

print("主表的描述性统计为：",Master.describe())  #用describe方法进行描述性统计

def DropStrNull(data):      #剔除值相同或全为空的列

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
print("用户信息更新表的删除值相同或者全空的列操作为：")
DropStrNull(Userupdate)
print("登录信息表的删除值相同或者全空的列操作为：")
DropStrNull(LogInfo)

#实训2
import pandas as pd
Master=pd.read_csv("..\data\Training_Master.csv",encoding="gbk")
Userupdate=pd.read_csv("..\data\Training_Userupdate.csv",encoding="gbk")
LogInfo=pd.read_csv("..\data\Training_LogInfo.csv",encoding="gbk")
Userupdate["ListingInfo1"]=pd.to_datetime(Userupdate["ListingInfo1"])       #用to_datetime函数转换时间字符串
Userupdate["UserupdateInfo2"]=pd.to_datetime(Userupdate["UserupdateInfo2"])
LogInfo["Listinginfo1"]=pd.to_datetime(LogInfo["Listinginfo1"])
LogInfo["LogInfo3"]=pd.to_datetime(LogInfo["LogInfo3"])

year=[i.year for i in Userupdate["ListingInfo1"].head()]        #用year、month、week、day提取时间信息
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

def TransformDayIntoMinute(data):           #计算时间差
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
import pandas as pd
import numpy as np
Userupdate=pd.read_csv("..\data\Training_Userupdate.csv",encoding="gbk")
LogInfo=pd.read_csv("..\data\Training_LogInfo.csv",encoding="gbk")

UserupdateGroup=Userupdate[["Idx","UserupdateInfo2"]].groupby(by="Idx")     #用groupby方法进行分组
print('分组后的登录信息表为：',UserupdateGroup)         
LogInfoGroup=LogInfo[["Idx","LogInfo3"]].groupby(by="Idx")

UpdateEarly=UserupdateGroup.agg(np.min)    #用agg方法求取分组后最早和最晚的更新、登陆时间
UpdateLate=UserupdateGroup.agg(np.max)
print("分组后最早更新时间：",UpdateEarly)
print("分组后最晚更新时间：",UpdateLate)

UpdateTimes=UserupdateGroup.size()    #用size方法求取分组后的数据信息更新次数、登陆次数
LogInTimes=LogInfoGroup.size()
print("分组后更新时间：",UpdateTimes)
print("分组后登录时间：",LogInTimes)

#实训4
import numpy as np
import pandas as pd
Master=pd.read_csv("..\data\Training_Master.csv",encoding="gbk")
Userupdate=pd.read_csv("..\data\Training_Userupdate.csv",encoding="gbk")
LogInfo=pd.read_csv("..\data\Training_LogInfo.csv",encoding="gbk")
print("Master表长宽转换前的形状：",Master.shape)
print("Userupdate表长宽转换前的形状：",Userupdate.shape)
print("LogInfo表长宽转换前的形状：",LogInfo.shape)

CMaster=Master.T
print("Master表长宽转换后的形状：",CMaster.shape)    #用pivot_table函数进行长款表转换
PMaster=pd.pivot_table(Master,index="Idx")
print("使用pivot_table后Master表的形状为：",PMaster.shape)
print("使用pivot_table后Master表为：",PMaster.head())

CRMaster=pd.crosstab(index=Master["Idx"],columns=Master["ListingInfo"],values=Master["ThirdParty_Info_Period2_7"],aggfunc=np.sum)
print("使用crosstab后Master表为：",CRMaster.head())  #用crosstab方法进行长宽表转换

