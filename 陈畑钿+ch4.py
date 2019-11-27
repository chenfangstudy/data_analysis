import pandas as pd;
import numpy as np
order1= pd.read_table('../data/Training_LogInfo.csv',
      sep = ',',encoding = 'gbk')
print('使用read_table读取的订单信息表的长度为：',len(order))
print('订单详情表的元素个数为：',order.size)
print('订单详情表的维度数为：', order.ndim) ## 查看DataFrame的维度数
print('订单详情表的形状为：', order.shape) ## 查看DataFrame的形状
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
    print('去除的列的数目为：',beforelen-afterlen)
    print('去除后数据的形状为：',data.shape)
dropNullStd(order)
order['Listinginfo1']= pd.to_datetime(order['Listinginfo1'])
print('进行转换后订单信息表time的类型为：', 
      order['Listinginfo1'].dtypes)
order['LogInfo3']= pd.to_datetime(order['LogInfo3'])
print('进行转换后订单信息表time的类型为：', 
      order['LogInfo3'].dtypes)
year1 =[i.year for i in order['Listinginfo1']]
print('登录信息表中的年份数据前5个为：',year1[:5])
month1 = [i.month for i in order['Listinginfo1']]
print('登录信息表中的月份数据前5个为：',month1[:5])
day1 = [i.day for i in order['Listinginfo1']]
print('登录信息表中的日期数据前5个为：',day1[:5])
weekday1 = [i.weekday_name for i in order['Listinginfo1']]
print('登录信息表中的星期名称数据前5个为：',weekday1[:5])
year1 =[i.year for i in order['LogInfo3']]
print('登录信息表中的年份数据前5个为：',year1[:5])
month1 = [i.month for i in order['LogInfo3']]
print('登录信息表中的月份数据前5个为：',month1[:5])
day1 = [i.day for i in order['LogInfo3']]
print('登录信息表中的日期数据前5个为：',day1[:5])
weekday1 = [i.weekday_name for i in order['LogInfo3']]
print('登录信息表中的星期名称数据前5个为：',weekday1[:5])
timeDelta = order['LogInfo3'] - pd.to_datetime('2014/3/5')
print('登录信息表减去2017年1月1日0点0时0分后的数据：\n',
      timeDelta[:5])
print('LogInfo3减去Listinginfo1后的数据类型为：',timeDelta.dtypes)
ordergroup=order[['Idx','Listinginfo1','LogInfo1',
 'LogInfo2','LogInfo3']].groupby(by='Idx')
print('分组后的情况:',ordergroup)
print('登录信息表的最早和最晚时间：\n', order[['LogInfo3']].agg([np.max,np.min]))
print('登录次数：\n', order[['Idx']].agg([np.size])) 

order2= pd.read_table('../data/Training_Userupdate.csv',
      sep = ',',encoding = 'gbk')
print('使用read_table读取的订单信息表的长度为：',len(order))
print('订单详情表的元素个数为：',order.size)
print('订单详情表的维度数为：', order.ndim) ## 查看DataFrame的维度数
print('订单详情表的形状为：', order.shape) ## 查看DataFrame的形状
    
