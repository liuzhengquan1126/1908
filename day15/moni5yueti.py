#-*- coding = utf-8 -*-
#@Time : 2021/8/31 15:30
#@Author : lpl
#@File : moni5yueti.py

list1 = [3,1,32,34,6,7,2,34,89]
# for i in range(len(list1)-1):       #  0 <= i <len(list1)-1
#     for j in range(len(list1)-1-i):
#         if list1[j] > list1[j+1]:
#             list1[j],list1[j+1] = list1[j+1],list1[j]
#
# print(list1)
print(list1)

list1=[['张三',85],['李四',80],['王五',70],['赵六',75]]
i = 0
while i < (len(list1)-1):
    j = 0
    while j < (len(list1)-1-i):
        if list1[j][1] > list1[j+1][1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
        j = j+1

    i = i+1

print(list1)

import random
def dayin(d1,shu1,d2,shu2,d3,shu3):
    liushui = random.randint(1000,9999)
    piao = f''' 
         星宇超市收银软件免费版
    流水号：{liushui}     2010/11/18 11:17
    ==============================
    编号         单价    数量   金额
    ------------------------------
    皮鞋
    001          {d1}      {shu1}     {shu1*d1}
    吉氏超值装婴儿尿裤
    002          {d2}      {shu2}     {d2*shu2}      
    广州单裤
    0023         {d3}      {shu3}     {d3*shu3}
    ------------------------------
    合计:                 {shu1+shu2+shu3}     {shu1*d1+d2*shu2+d3*shu3}
    优惠金额: 0.00 实收金额:  130.00
    收款金额: 150.00 找零金额：20.00
    ------------------------------
    会员卡号:002
    本次积分:25.66
    可以积分:15.34
    ==============================
          欢迎光临，谢谢惠顾！
          网址：www.xingyusoft.com
          QQ ： 1416683076
    '''
    print(piao)
dayin(3.1,2,3.3,2,3.3,1)

import time
zong = 0

def cun():
    shijian = str(time.asctime())
    cqian = int(input('qian:'))
    global zong
    zong = zong+cqian
    a = f'''{shijian} \t 存入：{cqian} \t 总金额：{zong}\n'''
    print(a)
    f = open('balance.txt','a')
    f.write(a)
    f.close()

# cun()
def qu():
    shijian = str(time.asctime())
    qqian = int(input('qian:'))
    global zong
    zong = zong-qqian
    a = f'''{shijian} \t 取出：{qqian} \t 总金额：{zong}\n'''
    print(a)
    f = open('balance.txt','a')
    f.write(a)
    f.close()

def du():
    f = open('balance.txt','r')
    shu = f.read()
    f.close()
    print(shu)

while 1:
    a = '''
    ------------
    xitong
    -------------
    1.cun
    2,qu
    3.cha
    0.tui
    ------------
    请输入要只想的数：
    '''
    xuanz = int(input(a))
    if xuanz == 1:
        cun()
    elif xuanz == 2:
        qu()
    elif xuanz == 3:
        du()
    elif xuanz == 0:
        break
    else:
        print('请输入符合要求的数：')