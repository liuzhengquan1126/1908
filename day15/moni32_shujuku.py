#-*- coding = utf-8 -*-
#@Time : 2021/8/31 9:57
#@Author : lpl
#@File : moni32_shujuku.py

'''
---------
1.鱼香肉丝
2.宫保鸡丁
3.酸菜鱼
4.红烧肉
--------
请输入要点的菜：

'''

# caidan = '''
# ---------
# 1.鱼香肉丝
# 2.宫保鸡丁
# 3.酸菜鱼
# 4.红烧肉
# --------
# 请输入要点的菜：
# '''
#
# while 1:
#     cai = int(input(caidan))
#     if cai == 1:
#         print('鱼香肉丝')
#     elif cai == 2:
#         print('宫保鸡丁')
#     elif cai == 3:
#         print('酸菜鱼')
#     elif cai == 4:
#         print('红烧肉')
#
# def he(a,b):
#     return a+b
#
# def jian(a,b):
#     return a -b
#
# def cheng(a,b):
#     return a * b
#
# def chu(a,b):
#     return a / b
# fu = input('输入符号：')
# shu1 = int(input('数1：'))
# shu2 = int(input('数2：'))
# if fu == '+':
#     he(shu1,shu2)
# elif fu == '-':
#     jian(shu1,shu2)

import pymysql

db = pymysql.connect(user='root',password='root',host='127.0.0.1',database='xuexi')
yb = db.cursor()

yb.execute('drop table if exists student;')
yb.execute('create table student(id int(11),name char(10),class char(15),sushe char(20));')

def zeng():
    id = int(input('id:'))
    name = input('name:')
    bangji = input('banji:')
    sushe = input('suxhe:')

    sql = '''insert into student values(%d,'%s','%s','%s')''' %(id,name,bangji,sushe)
    yb.execute(sql)
    db.commit()  #马上将数据更新进数据库

def shan():
    id  = int(input('id:'))
    sql = '''delete from student where id = %d''' %(id)
    yb.execute(sql)

def gai():
    id = int(input('id:'))
    bangji = input('banji:')
    sql = '''update student set class = '%s' where id = %d''' %(bangji,id)
    yb.execute(sql)

def cha():
    sql = '''select * from student;'''
    yb.execute(sql)
    a = yb.fetchall()  #获取结果
    print(a)

while 1:
    a = '''
    -----------------
    ---ddddddd------
    ---------------
    1.zneg
    2.shan
    3.gai
    4.cha
    0.退出
    --------------------
    输入要执行的操作编号：
    '''

    xuanze = int(input(a))
    if xuanze == 1:
        zeng()
    elif xuanze == 2:
        shan()
    elif xuanze ==3:
        gai()
    elif xuanze ==4:
        cha()
    elif xuanze ==0:
        break
    else:
        print('没有实现')

db.close()















