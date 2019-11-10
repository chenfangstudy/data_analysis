# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:46:24 2019

@author: sheil
"""


#实训一
import pandas as pd
master = pd.read_csv('G:/Seven G/04 大四/02 python/04 第4章/03-实训数据/Training_Master.csv',encoding = 'gbk')
print('主表的维度数为：',master.ndim)                #查维度
print('主表的形状为：',master.shape)                 #查形状
print('主表的占用内存为：',master.memory_usage())    #查内存
print('主表的描述性统计为：',master.describe())      #描述性统计
#删除相同值或全空的列
def dropNullStd(data):
    beforelen = data.shape[1]
    colisNull = data.describe().loc['count'] == 0   #定义并判断是否为空的列
    for i in range(len(colisNull)):
        if colisNull[i]:
            data.drop(colisNull.index[i],axis = 1,inplace = True) #删除空的列
    stdisZero = data.describe().loc['std'] == 0     #定义标准差，并判断是否为0
    for i in range(len(stdisZero)):
        if stdisZero[i]:
            data.drop(stdisZero.index[i],axis = 1,inplace = True) #删除标准差为0的列
    afterlen = data.shape[1]
    print('剔除的列的数目为：',beforelen-afterlen)
    print('剔除后数据的形状为：',data.shape)
dropNullStd(master)                                 #对master进行操作


#实训二
import pandas as pd
user = pd.read_csv('G:/Seven G/04 大四/02 python/04 第4章/03-实训数据/Training_Userupdate.csv',encoding = 'gbk')
loginfo = pd.read_csv('G:/Seven G/04 大四/02 python/04 第4章/03-实训数据/Training_LogInfo.csv',encoding = 'gbk')
#转换时间类型
print('进行转换前用户信息更新表的ListingInfo1时间的类型为：',user['ListingInfo1'].dtypes)
user['ListingInfo1'] = pd.to_datetime(user['ListingInfo1'])
print('进行转换后用户信息更新表的ListingInfo1时间类型为：',user['ListingInfo1'].dtypes)
print('进行转换前用户信息更新表的UserupdateInfo2时间类型为：',user['UserupdateInfo2'].dtypes)
user['UserupdateInfo2'] = pd.to_datetime(user['UserupdateInfo2'])
print('进行转换后用户信息更新表的UserupdateInfo2时间类型为：',user['UserupdateInfo2'].dtypes)
print('进行转换前登录信息表的Listinginfo1时间类型为：',loginfo['Listinginfo1'].dtypes)
loginfo['Listinginfo1'] = pd.to_datetime(loginfo['Listinginfo1'])
print('进行转换后登录信息表的Listinginfo1事件类型为：',loginfo['Listinginfo1'].dtypes)
print('进行转换前登录信息表的LogInfo3时间类型为：',loginfo['LogInfo3'].dtypes)
loginfo['LogInfo3'] = pd.to_datetime(loginfo['LogInfo3'])
print('进行转换后登陆信息表的LogInfo3事件类型为：',loginfo['LogInfo3'].dtypes)
#提取时间信息
year1_user = [i.year for i in user['ListingInfo1']]
print('ListingInfo1中的年份数据前5个为：',year1_user[:5])
year2_user = [i.year for i in user['UserupdateInfo2']]
print('UserupdateInofo2中的年份数据前5个位：',year2_user[:5])
month1_user = [i.month for i in user['ListingInfo1']]
print('ListingInfo1中的月份数据前5个为：',month1_user[:5])
month2_user = [i.month for i in user['UserupdateInfo2']]
print('UserupdateInfo2中的月份数据前5个为：',month1_user[:5])
week1_user = [i.week for i in user['ListingInfo1']]
print('ListingInfo1中的星期数据前5个为：',week1_user[:5])
week2_user = [i.week for i in user['UserupdateInfo2']]
print('UserupdateInfo2中的星期数据前5个为：',week2_user[:5])
#时间差
timeDeltauser=user['ListingInfo1']-user['UserupdateInfo2']
print("计算时间差以日期为单位：\n",timeDeltauser)
timeDelta1loginfo=loginfo['Listinginfo1']-loginfo['LogInfo3']

def TransformDayIntoMinute(data):
    for i in range(0,len(data)):
        data[i]=data[i].total_seconds()/60
    return data
print("计算时间差以分钟为单位：\n",TransformDayIntoMinute(timeDeltauser))
def TransformDayIntoSecond(data):
    for i in range(0,len(data)):
        data[i]=data[i].total_seconds()
    return data 
timeDeltauser=user['ListingInfo1']-user['UserupdateInfo2']
print("计算时间差以秒为单位：\n",TransformDayIntoSecond(timeDeltauser))


#实训三
import pandas as pd
import numpy as np
user = pd.read_csv('G:/Seven G/04 大四/02 python/04 第4章/03-实训数据/Training_Userupdate.csv',encoding = 'gbk')
loginfo = pd.read_csv('G:/Seven G/04 大四/02 python/04 第4章/03-实训数据/Training_LogInfo.csv',encoding = 'gbk')

userGroup = user[['Idx','UserupdateInfo2']].groupby(by = 'Idx')
print('分组后的登录信息表为：',userGroup)
loginfoGroup = loginfo[['Idx','LogInfo3']].groupby(by = 'Idx')

updateEarly = userGroup.agg(np.min)
updateLate = userGroup.agg(np.max)
print('分组后最早更新时间：',updateEarly)
print('分组后最晚更新时间：',updateLate)

updateTimes = userGroup.size()
loginfoTimes = loginfoGroup.size()
print('分组后更新时间：',updateTimes)
print('分组后登录时间：',loginfoTimes)

#实训4
import numpy as np
import pandas as pd
master = pd.read_csv('G:/Seven G/04 大四/02 python/04 第4章/03-实训数据/Training_Master.csv',encoding = 'gbk')
user = pd.read_csv('G:/Seven G/04 大四/02 python/04 第4章/03-实训数据/Training_Userupdate.csv',encoding = 'gbk')
loginfo = pd.read_csv('G:/Seven G/04 大四/02 python/04 第4章/03-实训数据/Training_LogInfo.csv',encoding = 'gbk')
print('master表长宽转换前的形状：',master.shape)
print('user表长宽转换前的形状：',user.shape)
print('loginfo表长宽转换前的形状：',loginfo.shape)

Cmaster = master.T
print('master表长宽转换后的形状：',Cmaster.shape)
Pmaster = pd.pivot_table(master,index='Idx')
print('使用pivot_table后master表的形状为：',Pmaster.shape)
print('使用pivot_table后master表为：',Pmaster.head())

CRmaster = pd.crosstab(index=master['Idx'],columns = master['ListingInfo'],values = master['ThirdParty_Info_Period2_7'],aggfunc = np.sum)
print('使用crosstab后master表为：',CRmaster.head())







