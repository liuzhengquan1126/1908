#-*- coding = utf-8 -*-
#@Time : 2021/8/30 15:37
#@Author : lpl
#@File : moni3.py


# 1.a="dskjfds45678sdkj"使用循环,返回2,4,5,6位数据
# 2.使用循环,将"12345666245"中的"5"是的下标全部打印
# 3.	使用循环找出‘12345666245’中所有的3位数，返回所有的三位数列表
# 4.找出1-100内 和3有关的数(带3或者3的倍数)，返回所有数据列表
# 5.趣味排序，现有下列数据，其中每组数据第一个数据是姓名，
# 第二个数据是身高，第三个数据是体重，现请跟据每组数据的身高进行升序排序

#下标

def f1():
    data = []
    a="dskjfds45678sdkj"
    for i in range(len(a)):
        if i ==1 or i == 3 or i ==4 or i ==5:
            data.append(a[i])
    return data

b = f1()
print(b)

shu = "12345666245"
for i in range(len(shu)):
    if shu[i] == '5':
        print(i)


data3 = []
for i in range(len(shu)-2):
    str3 = shu[i]+shu[i+1]+shu[i+2]
    shu3 = int(str3)
    data3.append(shu3)

print(data3)

data4 = []
for i in range(1,101):
    if i %3 ==0 or '3' in str(i):
        data4.append(i)

print(data4)


user = [['徐琬琪',175,76],['徐国哲',178,75],['丁长庆',177,72],['马冰森',170,75]]

for i in range(len(user)-1):
    for j in range(len(user)-1-i):
        if user[j][1] > user[j+1][1]:
            user[j],user[j+1] = user[j+1],user[j]

print(user)

userxin = sorted(user,key=lambda x:x[1],reverse=False)
print(userxin)

try:
    def xie(fname,neirong):
        f = open(fname,'w')
        f.write(neirong)
        f.close()

    # xie('hah.txt','''1，   登录-修改昵称
    # 2.    登录-修改密码
    # 3.    登录-上传头像
    # 4.    登录-根据用户ID查询用户信息
    # 5.    登录-收货地址列表
    # 6.    登录-新增收货地址
    # 7.    登录-收货地址列表（收货地址id）-设置默认收货地址
    # 8.    登录-收货地址列表（收货地址id）-修改收货信息
    # 9.    登录-查询用户钱包
    # 10.   登录-收货地址列表（收货地址id）-删除收货地址
    # 11.   查询app最新版本信息
    # ''')

    def du(fname):
        f = open(fname,'r')
        datai = f.readlines()
        f.close()
        return datai

    # f = du('hah.txt')
    # print(f)

    nn = '''1，   登录-修改昵称
    2.**  登录-修改密码
    3.    登录-上传头像
    4.    登录-根据用户ID查询用户信息
    5.    登录-收货地址列表
    6.    登录-新增收货地址
    7.    登录-收货地址列表（收货地址id）-设置默认收货地址
    8.    登录-收货地址列表（收货地址id）-修改收货信息
    9.    登录-查询用户钱包
    10.   登录-收货地址列表（收货地址id）-删除收货地址
    11.   查询app最新版本信息'''

    xie('1905测试.txt',nn)

    f2 =du('1905测试.txt')
    print(f2)

    print(f2[2:7])
except Exception as e:
    print(e)


'''
try:
    代码
except Exception as e:
    print(e) 
finally:
    必须执行
'''

