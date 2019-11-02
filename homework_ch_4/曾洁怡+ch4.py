实训1
from sqlalchemy import create_engine
import pandas as pd
engine=create_engine('data\第4章\Training_Master.csv',sep=',',encoding="gbk")
print(detail.ndim)#维度
print(detail.shape)#大小
print(detail.memory_usage)#维度
print(detail.describe())
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
dropNullStd(detail)


实训2
import pandas as pd
LogInfo=pd.read_csv('data\第4章\Training_LogInfo.csv',sep=',',encoding="gbk")
Userupdate=pd.read_table('data\第4章\Training_Master.csv',sep=',',encoding="gbk")
Userupdate["ListingInfo1"]=pd.to_datetime(Userupdate["ListingInfo1"])
Userupdate["UserupdateInfo2"]=pd.to_datetime(Userupdate["UserupdateInfo2"])
LogInfo["Listinginfo1"]=pd.to_datetime(LogInfo["Listinginfo1"])
LogInfo["LogInfo3"]=pd.to_datetime(LogInfo["LogInfo3"])

year=[i.year for i in Userupdate["ListingInfo1"]]
print("ListingInfo1中的前5个年份信息：",year[:5])
month=[i.month for i in Userupdate["ListingInfo1"]]
print("ListingInfo1中的前5个月份信息：",month[:5])
week=[i.week for i in Userupdate["ListingInfo1"]]
print("ListingInfo1中的前5个星期信息：",week[:5])

timeDeltaUserupdate=Userupdate["ListingInfo1"]-Userupdate["UserupdateInfo2"]
timeDelta1LogInfo=LogInfo["Listinginfo1"]-LogInfo["LogInfo3"]
print("计算时间差以日期为单位：\n",timeDeltaUserupdate)
print("计算时间差以日期为单位：\n",timeDelta1LogInfo)
def TransformDayIntoHours(data):
    for i in range(0,len(data)):
        data[i]=data[i].total_seconds()*60
    return data 
timeDeltaUserupdate=Userupdate["ListingInfo1"]-Userupdate["UserupdateInfo2"]
timeDelta1LogInfo=LogInfo["ListingInfo1"]-LogInfo["UserupdateInfo3"]
print("计算时间差以小时为单位：\n",TransformDayIntoSecond(timeDeltaUserupdate))
print("计算时间差以小时为单位：\n",TransformDayIntoSecond(timeDelta1LogInfo))
def TransformDayIntoMinute(data):
    for i in range(0,len(data)):
        data[i]=data[i].total_seconds()/60
    return data
print("计算时间差以分钟为单位：\n",TransformDayIntoMinute(timeDeltaUserupdate))
print("计算时间差以分钟为单位：\n",TransformDayIntoMinute(timeDelta1LogInfo)）


实训3
import pandas as pd;
import numpy as np
from sqlalchemy import create_engine
engine=create_engine('data\第4章\Training_LogInfo.csv',sep=',',encoding='gbk')
engine=create_engine('data\第4章\Training_Userupdate.csv',sep=',',encoding='gbk')
detail=pd.read_sq_table('meal_order_detaill',con=engine)
print(detail.[['Idx','Listinginfo1','LogInfo1','LogInfo2','LogInfo3']].groupby(by='Idx')
print(detail.[['Idx','ListingInfo1','UserupdateInfo1','UserupdateInfo2']].groupby(by='Idx'))
print("最早更新时间，最晚更新时间为:",ponidgp[['LogInfo3']].agg(['max','min']).head())
print("最早登陆时间，最晚登陆时间为:",pupidgp[['UserupdateInfo2']].agg(['max','min']).head())
print("信息更新次数:",ponidgp.size())
print("登陆次数:",pupidgp.size())


实训4
import pandas as pd;
import numpy as np
from sqlalchemy import create_engine
Master=pd.read_csv('data\第4章\Training_Master.csv’,sep=',',encoding="gbk")
Userupdate=pd.read_csv('data\第4章\Training_Userupdate.csv’,sep=',',encoding="gbk")
LogInfo=pd.read_csv('data\第4章\Training_LogInfo.csv',sep=',',encoding="gbk")
detail=pd.read_sql_table('meal_oeder_detaill',con=engine)
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
