#-*- coding = utf-8 -*-
#@Time : 2021/9/2 10:47
#@Author : lpl
#@File : shujuku.py

def dayin():
    a = '''
    ----------------------
    -------guanli---------
    ----------------------
    1.tianjia
    2.shan
    3.xiugai
    4.chazhao
    5.quan
    6.tui
    =======================
    请输入序号：
    '''
    print(a)

# dayin()

import pymysql
db = pymysql.connect(user='root',password='root',host='127.0.0.1',database='xuexi')    #localhost
yb = db.cursor()

yb.execute('drop table if exists stuInfo;')
yb.execute('''create table stuInfo(
                                    name char(20),
                                    phone char(20),
                                    wexin char(20)
                                    );''')

def zeng():
    name = input('xin name:')
    phone = input('phone:')
    wexin = input('wexin:')
    sql = '''insert into stuInfo values ('%s','%s','%s');''' %(name,phone,wexin)
    yb.execute(sql)
    db.commit()

    sql = '''select * from stuInfo where name = '%s';''' %(name)
    yb.execute(sql)
    a = yb.fetchall()
    print(a)

def shan():
    name = input('shan name:')
    sql = '''delete from stuInfo where name = '%s';''' %(name)
    yb.execute(sql)

def xiu():
    jiuname = input('yuan name:')
    name = input('xin name:')
    phone = input('phone:')
    wexin = input('wexin:')

    sql = '''update stuInfo set name = '%s',
            phone = '%s', wexin = '%s' where name = '%s';''' %(name,phone,wexin,jiuname)
    yb.execute(sql)

def cha():
    name = input('xin name:')
    sql = '''select * from stuInfo where name = '%s';''' % (name)
    yb.execute(sql)
    a = yb.fetchall()
    print(a)

def quan():
    sql = '''select * from stuInfo;'''
    yb.execute(sql)
    a = yb.fetchall()
    print(a)


while 1:
    dayin()
    xu = int(input())
    if xu == 1:
        while 1:
            zeng()

            xia = input('继续还是返回（j/f）')
            if xia == 'j':
                continue
            else:
                break

    elif xu == 2:

        while 1:
            shan()

            xia = input('继续还是返回（j/f）')
            if xia == 'j':
                continue
            else:
                break
    elif xu == 3:
        while 1:
            xiu()

            xia = input('继续还是返回（j/f）')
            if xia == 'j':
                continue
            else:
                break
    elif xu == 4:
        while 1:
            cha()

            xia = input('继续还是返回（j/f）')
            if xia == 'j':
                continue
            else:
                break
    elif xu ==5:
        while 1:
            quan()

            xia = input('继续还是返回（j/f）')
            if xia == 'j':
                continue
            else:
                break
    elif xu == 6:
        break

