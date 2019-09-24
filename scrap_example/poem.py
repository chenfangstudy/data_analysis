# 这是一个抓取古诗词的实例，大家来学习一下

from urllib import request
# from urllib.error import HTTPError
from urllib.error import URLError
import re

import pymysql

import time

base_url = "https://so.gushiwen.org"
shiwen_url = 'https://www.gushiwen.org/shiwen/'


def get_html(url):
    """打开网页并将其转成utf-8编码
    """
    html = request.urlopen(url).read().decode('utf-8')
    return html


def get_model_url(shiwen_url):
    """
    """
    html = get_html(shiwen_url)
    res = '<a href="https://so\.gushiwen\.org/(.*?)\.aspx">(.*?)</a>'
    urls = re.compile(res).findall(html)
    return urls


def conn_mysql():
    """做一个数据库连接点
    """
    url = '127.0.0.1'
    # 存储本地
    username = 'user_name'
    # 用户名
    password = 'Your_password'
    # 秘密
    dbname = 'Where you will access your data!'
    # 数据库的名称
    db = pymysql.connect(url, username, password, dbname)
    # 建立连接
    return db


def create_table_poem():
    """设置列表
    """
    sql = 'create table if not exists poem2(\
           model_name varchar(50),\
           poem_name varchar(50),\
           author_name varchar(50),\
           dynasty varchar(50),\
           content text)'
    db = conn_mysql()
    db.cursor().execute(sql)
    db.commit()


def get_url_list(html):
    """ 这里用来提取网页列表
    """
    res = '<span><a href="(.*?)" target="_blank">.*?</a>.*?</span>'
    url1 = re.compile(res).findall(html)
    url_list = []
    for u in url1:
        url_list.append(base_url+u)
    return url_list


def get_poem_content(url):
    html = get_html(url)
    res = '<h1 style="font-size:.*?;">(.*?)</h1>\n<p class="source"><a href=".*?">' \
        '(.*?)</a>.*?<a href=".*?">(.*?)</a> </p>\n<div class="contson" id="contson.*?">\n([\s\S]*?)\n</div>'
    poem_content = re.compile(res).findall(html)
    return poem_content


if __name__ == '__main__':

    start = time.process_time()
    db = conn_mysql()
    create_table_poem()

    model_name = []
    i = 0
    j = 0

    for g in get_model_url(shiwen_url):
        url = 'https://so.gushiwen.org/'+list(g)[0]+'.aspx'
        model_name.append(list(g)[1])
        try:
            html = get_html(url)
        except URLError as e:
            print("There is a wrong.")
        url_list = get_url_list(html)
        for s in url_list:
            i += 1
            try:
                LL = get_poem_content(s)
            except URLError as e:
                print("There is a wrong.")
            if len(LL) == 0:
                pl = ['NULL', 'NULL', 'NULL', 'NULL']
            else:
                pl = LL[0]
            sql = 'insert into poem2(model_name, poem_name,\
                   author_name, dynasty, content)\
                   values (%s,%s,%s,%s,%s)'
            data = [model_name[j], pl[0], pl[2], pl[1],
                    re.sub('<br />|<p>|</p>', '', pl[3])]
            try:
                db.cursor().execute(sql, data)
            except Exception as e:
                print("DATABASE HAVE a wrong")
            db.commit()
            print('Success!!!   ' + '当前模块 :' +
                  model_name[j]+'-----' +
                  '已导入------' + str(i)+'条数据'+'-----')
        j += 1

    db.close()

    print('Success!!!')
    print('End!!!')
    end = time.process_time()

    print('Running time: %s Seconds' %(end - start))
