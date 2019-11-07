#实训 1

import pandas as pd
master = pd.read_csv('../03-实训数据/Training_Master.csv',encoding='gbk')
print('P2P 网络贷款主表数据的维度为:',master.ndim)
print('P2P 网络贷款主表数据的形状大小为:',master.shape)
print('P2P 网络贷款主表数据的占用内存:',master.memory_usage())
print('P2P 网络贷款主表数据的描述性统计为:\n',master.describe())
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
    print('去除的列的数目为:',beforelen-afterlen) 
    print('去除后数据的形状为:',data.shape)
  dropNullStd(master)
  


#实训 2
  
import pandas as pd
LogInfo = pd.read_csv('../03-实训数据/Training_LogInfo.csv',encoding='gbk') 
Userupdate = pd.read_csv('../03-实训数据/Training_Userupdate.csv',encoding='gbk') 
LogInfo['Listinginfo1']=pd.to_datetime(LogInfo['Listinginfo1']) 
LogInfo['LogInfo2']=pd.to_datetime(LogInfo['LogInfo2']) 
print('转换登录信息表的时间字符串前 5 行:\n',LogInfo.head())


Userupdate['ListingInfo1']=pd.to_datetime(Userupdate['ListingInfo1']) 
Userupdate['UserupdateInfo2']=pd.to_datetime(Userupdate['UserupdateInfo2']) 
print('转换用户信息更新表的时间字符串前 5 行:\n',Userupdate.head())


def extract(file,time):
    global year
    year = [i.year for i in file[time]] 
    month = [i.month for i in file[time]] 
    week = [i.week for i in file[time]] 
    return year,month,week
ETLog1 = extract(LogInfo,'Listinginfo1') 
print('每行的前五个数据:\n',ETLog1[0][0:5],ETLog1[1][0:5],ETLog1[2][0:5])

ETLog2 = extract(LogInfo,'LogInfo2') 
print('每行的前五个数据:\n',ETLog2[0][0:5],ETLog2[1][0:5],ETLog2[2][0:5])

ETUser1 = extract(Userupdate,'ListingInfo1') 
print('每行的前五个数据:\n',ETUser1[0][0:5],ETUser1[1][0:5],ETUser1[2][0:5])

ETUser2 = extract(Userupdate,'UserupdateInfo2') 
print('每行的前五个数据:\n',ETUser2[0][0:5],ETUser2[1][0:5],ETUser2[2][0:5])

TDLog = LogInfo['Listinginfo1'] - LogInfo['LogInfo2'] 
print('计算登录信息表中两时间之差:\n',TDLog.head())

TDUser = Userupdate['ListingInfo1'] - Userupdate['UserupdateInfo2'] 
print('计算更新表中两时间之差:\n',TDUser.head())


#实训 3

import pandas as pd

df = pd.read_csv('../03-实训数据/Training_LogInfo.csv')
dff = pd.read_csv('../03-实训数据/Training_LogInfo.csv')

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


#实训 4

import pandas as pd 
master = pd.read_csv('../03-实训数据/Training_Master.csv',encoding='gbk') 
LogInfo = pd.read_csv('../03-实训数据/Training_LogInfo.csv',encoding='gbk') 
Userupdate = pd.read_csv('../03-实训数据/Training_Userupdate.csv',encoding='gbk') 
# 用 pivot_table 函数将长表转换成宽表 

LogInfo_pivot = pd.pivot_table(LogInfo,index='Idx',columns = ['LogInfo1'],aggfunc='count') 
print('用 LogInfo1 作为分组键创建的登录信息表：\n',LogInfo_pivot.head())

Userupdate_pivot=pd.pivot_table(Userupdate,index='Idx',columns=['UserupdateInfo1'],aggfunc='count')
print('用 UserupdateInfo1 作为分组键创建的用户信息更新表：\n',Userupdate_pivot.head())
# 用 crosstab 方法将长表转换成宽表 

LogInfo_cross = pd.crosstab(index=LogInfo['Idx'],columns=LogInfo['LogInfo1'])
print('用 LogInfo1 作为分组键创建的登录信息表: \n',LogInfo_pivot.head())

Userupdate_cross=pd.crosstab(index=Userupdate['Idx'],columns=Userupdate['UserupdateInfo1']) 
print('用 UserupdateInfo1 作为分组键创建的用户信息更新表：\n',Userupdate_pivot.head())

