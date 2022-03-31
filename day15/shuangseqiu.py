#-*- coding = utf-8 -*-
#@Time : 2021/9/1 9:37
#@Author : lpl
#@File : shuangseqiu.py

userdic = {'lplpl':'123456'}

def zhuce():
    while 1:
        name = input('name:')
        if name not in userdic.keys():
            '''没有注册，可以注册'''
            if len(name) == 5 and name.isalpha():
                '''符合要求可以注册'''
                mima = input('mima:')
                if len(mima) == 6 and mima.isdigit():
                    print('注册成功')
                    userdic[name] = mima
                    break
                else:
                    print('密码不是6位纯数字')
            else:
                print('账号不是5位纯字母')
        else:
            print('已注册，可以直接登录')

    print(userdic)

# zhuce()

def deng():
    cishu = 0
    while 1:
        name = input('name:')
        if name in userdic.keys():
            '''可以登录'''
            mima = input('mima:')
            if userdic[name] == mima:
                print('成功')
                break
            else:
                print('密码错误')
                cishu = cishu+1

        else:
            print('请先注册')

        if cishu == 3:
            print('机会用完')
            break
# while 1:
#     xuanze = int(input('''
#     ---------
#     1.zhuce
#     2.denglu
#     0.tuichu
#     -------
#     xuanzeshi:
#     '''))
#
#
#     if xuanze == 1:
#         zhuce()
#     elif xuanze ==2:
#         deng()
#     elif xuanze == 0:
#         exit(0)
#     else:
#         print('选择0-2')

hong = set()

while 1:
    haoi = int(input('输入红球号码'))
    if 1<= haoi<=33:
        hong.add(haoi)

    if len(hong) == 6:
        break

lan = 0

while 1:
    lani = int(input('输入蓝球号码'))
    if 1<= lani<=16:
        lan = lani
        break

print(hong,lan)


xhong = set()

import random
while 1:
    haoi = random.randint(1,33)
    xhong.add(haoi)

    if len(xhong) == 6:
        break

xlan = random.randint(1,16)


print(xhong,xlan)

if xlan == lan:
    '''有奖'''
    if len(xhong & hong) == 4:
        print('3等奖')
    elif len(xhong & hong) == 5:
        print('2等奖')
    elif len(xhong & hong) == 6:
        print('1等奖')
    else:
        print('5块 ')

else:
    print('谢谢惠顾')

