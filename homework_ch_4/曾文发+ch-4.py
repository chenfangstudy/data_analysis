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

#-----------------------------------方法1---------------------------------------------------------------
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


#对drop参数的理解 
#1.colisNull.index[i]表示删除表的行号或列好
#2.axis=0表示操作对象是行，axis=1表示操作对象是列
#3.inplace=True表示直接在原表上操作，False表示重新创建一个新表进行操作
filepath2="C:\Users\3SXL_21125\Desktop\第4章\03-实训数据/Training_LogInfo.csv"
filepath3="C:\Users\3SXL_21125\Desktop\第4章\03-实训数据/Training_Userupdate.csv"

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
import pandas as pd

df = pd.read_csv('Training_Userupdate.csv')
dff = pd.read_csv('Training_LogInfo.csv')

df1 = df.groupby('Idx')
dff1 = dff.groupby('Idx')

df2 = df1[['UserupdateInfo2']].agg(['max', 'min']).head()
print("前五组的最早和最晚更新时间为：",df2)

dff2 = dff1[['LogInfo3']].agg(['max', 'min']).head()
print("前五组的最早和最晚登陆时间为：",dff2)

df3 = df1.size().head()
print("前五组的登陆次数为：",df3)

dff3 = dff1.size().head()
print("前五组的更新登陆次数为：",dff3)
import pandas as pd 
master = pd.read_csv('../data/Training_Master.csv',encoding='gbk') 
LogInfo = pd.read_csv('../data/Training_LogInfo.csv',encoding='gbk') 
Userupdate = pd.read_csv('../data/Training_Userupdate.csv',encoding='gbk') 
# 用 pivot_table 函数将长表转换成宽表 
LogInfo_pivot = pd.pivot_table(LogInfo,index='Idx',columns = ['LogInfo1'],aggfunc='count') 
print('用 LogInfo1 作为分组键创建的登录信息表：\n',LogInfo_pivot.head())
Userupdate_pivot=pd.pivot_table(Userupdate,index='Idx',columns=['UserupdateInfo1'],aggf unc='count') 
print('用 UserupdateInfo1 作为分组键创建的用户信息更新表：\n',Userupdate_pivot.head())
# 用 crosstab 方法将长表转换成宽表 
LogInfo_cross = pd.crosstab(index=LogInfo['Idx'],columns=LogInfo['LogInfo1'] 
print('用 LogInfo1 作为分组键创建的登录信息表：\n',LogInfo_pivot.head())
Userupdate_cross=pd.crosstab(index=Userupdate['Idx'],columns=Userupdate['UserupdateInf o1']) print('用 UserupdateInfo1 作为分组键创建的用户信息更新表：\n',Userupdate_pivot.head())
