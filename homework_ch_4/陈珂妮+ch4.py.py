Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd

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





def userTimedelta(bdata,rdata):

    timedelta = pd.to_datetime(bdata) - pd.to_datetime(rdata)

    print('减去后的数据:',timedelta[:5])

    print('数据类型:',timedelta[:5])



userTimedelta(pon['Listinginfo1'],pon['LogInfo3'])

userTimedelta(pup['ListingInfo1'],pup['UserupdateInfo2'])



#实训3

ponidgp = pon[['Idx','Listinginfo1','LogInfo1','LogInfo2','LogInfo3']].groupby(by='Idx')

pupidgp = pup[['Idx','ListingInfo1','UserupdateInfo1','UserupdateInfo2']].groupby(by='Idx')

print("最早更新时间，最晚更新时间为:",ponidgp[['LogInfo3']].agg(['max','min']).head())

print("最早登陆时间，最晚登陆时间为:",pupidgp[['UserupdateInfo2']].agg(['max','min']).head())

print("信息更新次数:",ponidgp.size())

print("登陆次数:",pupidgp.size())



#实训4

ponpivot = pd.pivot_table(pon,index='Idx')

pupCross = pd.crosstab(index=pup['Idx'],columns='UserupdateInfo1')

print(pupCross)



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





def userTimedelta(bdata,rdata):

    timedelta = pd.to_datetime(bdata) - pd.to_datetime(rdata)

    print('减去后的数据:',timedelta[:5])

    print('数据类型:',timedelta[:5])



userTimedelta(pon['Listinginfo1'],pon['LogInfo3'])

userTimedelta(pup['ListingInfo1'],pup['UserupdateInfo2'])



#实训3

ponidgp = pon[['Idx','Listinginfo1','LogInfo1','LogInfo2','LogInfo3']].groupby(by='Idx')

pupidgp = pup[['Idx','ListingInfo1','UserupdateInfo1','UserupdateInfo2']].groupby(by='Idx')

print("最早更新时间，最晚更新时间为:",ponidgp[['LogInfo3']].agg(['max','min']).head())

print("最早登陆时间，最晚登陆时间为:",pupidgp[['UserupdateInfo2']].agg(['max','min']).head())

print("信息更新次数:",ponidgp.size())

print("登陆次数:",pupidgp.size())



#实训4

ponpivot = pd.pivot_table(pon,index='Idx')

pupCross = pd.crosstab(index=pup['Idx'],columns='UserupdateInfo1')

print(pupCross)
