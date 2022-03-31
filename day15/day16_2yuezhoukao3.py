#-*- coding = utf-8 -*-
#@Time : 2021/8/28 9:53
#@Author : lpl
#@File : day16_2yuezhoukao3.py


# def sushu(m,n):
#     biao = []
#     for j in range(m,n+1):
#         yinzi = 0
#         for i in range(1,j+1):
#             if j % i == 0:
#                 yinzi = yinzi +1
#
#         if yinzi == 2:
#             print(j,'ok')
#             biao.append(j)
#         else:
#             print(j,'no')
#
#     he = sum(biao)
#     print(he)
#
# sushu(2,5)
#
#
# def listFunc(n):
#     shu = []
#
#     for i in range(1,n+1):
#         zhi = i ** i
#         shu.append(zhi)
#
#     return sum(shu)
#
# a = listFunc(4)
# print(a)
#
# def func3(*args):
#     fen = list(args)
#
#     zuida = max(fen)
#     fen.remove(zuida)
#     zuixiao = min(fen)
#     fen.remove(zuixiao)
#
#     jun = sum(fen)/len(fen)
#     return jun
#
# jun = func3(1,7,7,7,7,10)
# print(jun)
#
# def jisuanwqi():
#     shu1 = int(input('shu1:'))
#     fu = input('fu:')
#     shu2 = int(input('shu2:'))
#
#     if fu == '+':
#         jieguo = shu1+shu2
#     elif fu == "-":
#         jieguo = shu1-shu2
#     elif fu == "*":
#         jieguo  = shu1*shu2
#     elif fu == "/":
#         jieguo = shu1/shu2
#     else:
#         print('暂时没有实现')
#
#     print(jieguo)

# jisuanwqi()


# qian = int(input('qian:'))
# if qian >=1000:
#     print('ri')
# elif qian>=800:
#     print('披萨')
# else:
#     print('kfc')

strZh = '十是十四是四十四是十四四十是四十'

set1 = set(strZh)
print(set1)

dict2 ={}
for i in set1:
    dict2[i] = []
print(dict2)

for biao in range(len(strZh)):
    if strZh[biao] == '是':
        dict2['是'].append(biao)
    elif strZh[biao] == '十':
        dict2['十'].append(biao)
    elif strZh[biao] == '四':
        dict2['四'].append(biao)
print(dict2)


# user = {'lplpl':'123456'}
# shibai = 0
# while 1:
#     userName = input('username：')
#     if userName not in user.keys():
#         print('不在user中')
#         if len(userName) == 5 and userName.isalpha() == True:
#             print('用户名没问题')
#             miam = input('miam:')
#             if len(miam) == 6 and miam.isdigit() == True:
#                 print('注册成功')
#                 user[userName] = miam
#                 break
#             else:
#                 print('注册失败,密码不规范')
#                 shibai = shibai +1
#         else:
#             print('注册失败,用户名不规范')
#             shibai = shibai+1
#
#     else:
#         print('用户名已经存在,请重新注册')
#
#     if shibai == 5:
#         print('注册失败次数,达到5次,结束循环')
#         break
#
#
# print(user)

user = {'lplpl':'123456','lolol':'654321'}

cishu = 0
while 1:
    userid = input('userid:')
    if userid in user.keys():
        print('在')
        mima = input('miam:')
        if mima == user[userid]:
            print('欢迎{}'.format(userid))
            break
        else:
            print('密码错误')
            cishu = cishu+1
    else:
        print('用户不存在')

    if cishu == 3:
        print('错误次数,达到3次,结束循环')
        break















