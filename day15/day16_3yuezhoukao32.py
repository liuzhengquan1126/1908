#-*- coding = utf-8 -*-
#@Time : 2021/8/28 11:11
#@Author : lpl
#@File : day16_3yuezhoukao32.py

import calendar
def yue():
    nian = int(input('nian:'))
    yue = int(input('yue:'))
    print('余一下{}nian{}yue de ri li'.format(nian,yue))
    print(calendar.month(nian,yue))

# yue()

import math

def f6(shu):
    if shu >= 0:
        gen = math.sqrt(shu)
        jue = math.fabs(shu)
    else:
        jue = math.fabs(shu)
        gen = '负数没有平方根'
    return gen,jue

jie = f6(5)
print(jie)

jie2 = f6(-5)
print(jie2)

def f7(x,y):
    res = math.pow(x,y)
    print(res)

f7(2,3)
f7(3,2)

he = lambda shu1, shu2: shu1 + shu2
print(he(3, 4))


def xu(listi):
    for i in range(len(listi)-1):
        for j in range(len(listi) - 1-i):
            if listi[j] > listi[j+1]:
                listi[j],listi[j+1] = listi[j+1],listi[j]
    print(listi)

xu([1,3,4,6,63,2,2,456,7])