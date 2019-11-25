import pandas as pd

engine ='python'
master = pd.read_csv('../data/Training_Master.csv',sep=',',encoding="gbk")
print(master.ndim)#维度
print(master.shape)#大小
print(master.memory_usage())#内存信息
print(master.describe())
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
dropNullStd(master)

#实训2

LogInfo = pd.read_csv('../data/Training_LogInfo.csv',sep=',',encoding='gbk')
Userupdate = pd.read_csv('../data/Training_Userupdate.csv',engine ='python',sep='/t',encoding='gb18030')

LogInfo['Listinginfo1'] = pd.to_datetime(LogInfo['Listinginfo1'])
LogInfo['LogInfo3']= pd.to_datetime(LogInfo['LogInfo3'])
Userupdate['ListingInfo1'] = pd.to_datetime(Userupdate['ListingInfo1'])
Userupdate['UserupdateInfo2']= pd.to_datetime(Userupdate['UserupdateInfo2'])

print(LogInfo['Listinginfo1'].dtypes)
print(LogInfo['LogInfo3'].dtypes)
print(Userupdate['ListingInfo1'].dtypes)
print(Userupdate['UserupdateInfo2'].dtypes)



#实训3
def ymw(data):
    year = [i.year for i in data]
    month = [i.month for i in data]
    week = [i.week for i in data]
    print('年份前5个数据为：',year[:5])
    print('月份前5个数据为：',month[:5])
    print('星期前5个数据为：',week[:5])

ymw(LogInfo['Listinginfo1'])
ymw(LogInfo['LogInfo3'])
ymw(Userupdate['ListingInfo1'])
ymw(Userupdate['UserupdateInfo2'])


def userTimedelta(bdata,rdata):
    timedelta = pd.to_datetime(bdata) - pd.to_datetime(rdata)
    print('减去后的数据:',timedelta[:5])
    print('数据类型:',timedelta[:5])

userTimedelta(LogInfo['Listinginfo1'],LogInfo['LogInfo3'])
userTimedelta(Userupdate['ListingInfo1'],Userupdate['UserupdateInfo2'])

#实训3
ponidgp = LogInfo[['Idx','Listinginfo1','LogInfo1','LogInfo2','LogInfo3']].groupby(by='Idx')
pupidgp = Userupdate[['Idx','ListingInfo1','UserupdateInfo1','UserupdateInfo2']].groupby(by='Idx'
                    )
print("最早更新时间，最晚更新时间为:",ponidgp[['LogInfo3']].agg(['max','min']).head())
print("最早登陆时间，最晚登陆时间为:",pupidgp[['UserupdateInfo2']].agg(['max','min']).head())
print("信息更新次数:",ponidgp.size())
print("登陆次数:",pupidgp.size())

#实训2
LogInfo = pd.read_csv('../data/Training_LogInfo.csv',sep=',',encoding='gbk')
Userupdate = pd.read_csv('../data/Training_Userupdate.csv',engine ='python',sep='/t',encoding='gb18030'  )

LogInfo['Listinginfo1'] = pd.to_datetime(LogInfo['Listinginfo1'])
LogInfo['LogInfo3']= pd.to_datetime(LogInfo['LogInfo3'])
Userupdate['ListingInfo1']= pd.to_datetime(Userupdate['ListingInfo1'])
Userupdate['UserupdateInfo2']= pd.to_datetime(Userupdate['UserupdateInfo2'])

print(LogInfo['Listinginfo1'].dtypes)
print(LogInfo['LogInfo3'].dtypes)
print(Userupdate['ListingInfo1'].dtypes)
print(Userupdate['UserupdateInfo2'].dtypes)


#实训3
def ymw(data):
    year = [i.year for i in data]
    month = [i.month for i in data]
    week = [i.week for i in data]
    print('年份前5个数据为：',year[:5])
    print('月份前5个数据为：',month[:5])
    print('星期前5个数据为：',week[:5])

ymw(LogInfo['Listinginfo1'])
ymw(LogInfo['LogInfo3'])
ymw(Userupdate['ListingInfo1'])
ymw(Userupdate['UserupdateInfo2'])


def userTimedelta(bdata,rdata):
    timedelta = pd.to_datetime(bdata) - pd.to_datetime(rdata)
    print('减去后的数据:',timedelta[:5])
    print('数据类型:',timedelta[:5])

userTimedelta(LogInfo['Listinginfo1'],LogInfo['LogInfo3'])
userTimedelta(Userupdate['ListingInfo1'],Userupdate['UserupdateInfo2'])

#实训3
ponidgp = LogInfo[['Idx','Listinginfo1','LogInfo1','LogInfo2','LogInfo3']].groupby(by='Idx')
pupidgp = Userupdate[['Idx','ListingInfo1','UserupdateInfo1','UserupdateInfo2']].groupby(by='Idx')
print("最早更新时间，最晚更新时间为:",ponidgp[['LogInfo3']].agg(['max','min']).head())
print("最早登陆时间，最晚登陆时间为:",pupidgp[['UserupdateInfo2']].agg(['max','min']).head())
print("信息更新次数:",ponidgp.size())
print("登陆次数:",pupidgp.size())

#实训4
ponpivot = pd.pivot_table(LogInfo,index='Idx')
pupCross = pd.crosstab(index=Userupdate['Idx'],columns='UserupdateInfo1')
print(pupCross)