import pandas as pd
import numpy as np

###########shixun1###############
ppd = pd.read_csv('data\第4章\Training_Master.csv',sep=',',encoding="gbk")
print('占用内存为：', detail.memory_usage)
print('维度数为：', detail.ndim) ## 查看DataFrame的维度数
print('形状为：', detail.shape) ## 查看DataFrame的形状
print('订单详情表counts和amounts两列的描述性统计为：\n',detail[['counts','amounts']].describe())
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
dropNullStd(detail)
###################

############shixun2###################
order = pd.read_table('data\第4章\Training_LogInfo.csv',
      sep = ',',encoding = 'gbk')
order = pd.read_table('data\第4章\Training_Userupdate.csvv',
      sep = ',',encoding = 'gbk')
order['use_start_time'] = pd.to_datetime(order['use_start_time'])
order['lock_time'] = pd.to_datetime(order['lock_time'])
print('进行转换后订单信息表use_start_time和lock_time的类型为：\n', 
      order[['use_start_time','lock_time']].dtypes)

year = [i.year for i in order['lock_time']]## 提取年份信息
month = [i.month for i in order['lock_time']]## 提取月份信息
day = [i.day for i in  order['lock_time']]## 提取日期信息
week = [i.week for i in  order['lock_time']]## 提取周信息
weekday = [i.weekday() for i in  order['lock_time']]##提取星期信息
## 提取星期名称信息
weekname = [i.weekday_name for i in  order['lock_time']]
print('订单详情表中的前5条数据的年份信息为：',year[:5])
print('订单详情表中的前5条数据的月份信息为：',month[:5])
print('订单详情表中的前5条数据的日期信息为：',day[:5])
print('订单详情表中的前5条数据的周信息为：',week[:5])
print('订单详情表中的前5条数据的星期信息为：',weekday[:5])
print('订单详情表中的前5条数据的星期名称信息为：',weekname[:5])

ymw(pon['Listinginfo1'])
ymw(pon['LogInfo3'])
ymw(pup['ListingInfo1'])
ymw(pup['UserupdateInfo2'])


def userTimedelta(bdata,rdata):
    timedelta = pd.to_datetime(bdata) - pd.to_datetime(rdata)
    print('减掉的:',timedelta[:5])
    print('数据类型:',timedelta[:5])

userTimedelta(pon['Listinginfo1'],pon['LogInfo3'])
userTimedelta(pup['ListingInfo1'],pup['UserupdateInfo2'])

#################shixun3######################

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:\
3306/testdb?charset=utf8')
detail = pd.read_sql_table('meal_order_detail1',con = engine)
detailGroup = detail[['order_id','counts',
      'amounts']].groupby(by = 'order_id')
print('分组后的为：',detailGroup)

print('订单详情表的均值为：\n',
      detail[['counts','amounts']].agg([np.min,np.max]))

print('更新次数大小为：','\n', 
      detailGroup.size().head())

#########################################

###################shixun4#############################
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:1234@\
127.0.0.1:3306/testdb?charset=utf8')
detail = pd.read_sql_table('meal_order_detail1',
      con = engine)
detailPivot = pd.pivot_table(detail[[
      'order_id','counts','amounts']],
      index = 'order_id')
print('以order_id作为分组键创建的透视表为：\n',
       detailPivot.head())

detailPivot1 = pd.pivot_table(detail[[
      'order_id','counts','amounts']],
      index = 'order_id',aggfunc = np.sum)
print('以order_id作为分组键创建的透视表为：\n',
       detailPivot1.head())

detailCross = pd.crosstab(
      index=detail['order_id'],
      columns=detail['dishes_name'],
      values = detail['counts'],aggfunc = np.sum)
print('以order_id和dishes_name为分组键\
counts为值的透视表前5行5列为：\n',detailCross.iloc[:5,:5])