PYTHON分析统计自己微信朋友的信息
首先，你得安装itchat，命令为pip install itchat，其余的较为简单，我不再说明，直接看注释吧。

以下的代码我在Win7+Python3.7里面调试通过
__author__ = 'Yue Qingxuan'
# -*- coding: utf-8 -*-
import itchat

# hotReload=True可不用每次都去扫描二维码，只需要手机上确认下
itchat.auto_login(hotReload=True)
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]

# 初始化计数器，有男有女，当然，有些人是不填的
male = female = other = 0

# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算，其中sex=1时表示男性，2为女性，0是未注明性别的
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
        #这里可以输出哪些是未注明性别的
        print("NickName=",i['NickName'],"\t\t RemarName",i['RemarkName'])

# 算上微信朋友总数，计算比例
total = len(friends[1:])

# 好了，打印结果
print("微信朋友数量=",str(len(friends[1:])))
print("男性好友数量%d，占比：%.2f%%" % (male,float(male) / total * 100))
print("女性好友数量%d，占比：%.2f%%" % (female,float(female) / total * 100))
print("未明性别数量%d，占比：%.2f%%" % (other,float(other) / total * 100))
