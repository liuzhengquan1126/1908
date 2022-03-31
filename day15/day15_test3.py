#-*- coding = utf-8 -*-
#@Time : 2021/8/27 19:12
#@Author : lpl
#@File : day15_test3.py

# fang = lambda n:n**2
#
# for i in range(1,6):
#     fi = fang(i)
#     print(fi)

# import calendar
#
# nian = int(input('输入年份：'))
# jieguo = calendar.isleap(nian)
# # print(jieguo)
#
# if jieguo == True:
#     print(calendar.month(nian,2))
# else:
#     print('不是闰年')


# import random,math
# n = random.randint(1,99)
#
# jie2 = math.sqrt(n)
# print(jie2)
#
# i = 1
# while i < 100:
#     cha = i - jie2
#     jue = abs(cha)
#     if jue <=0.5:
#         print(i)
#         break
#     i = i+1
#
# import random
# str1 = "abcde"
# str2="ABCDE"
# str3 ="0123456789"
#
# fu1 = random.uniform(0,200)
# shu1 = math.ceil(fu1)
# fu2 = random.uniform(0,200)
# shu2 = math.ceil(fu2)
# fu3 = random.uniform(0,200)
# shu3 = math.ceil(fu3)
# fu4 = random.uniform(0,200)
# shu4 = math.ceil(fu4)
#
# yu1 = shu1 % len(str1)
# yu2 = shu2 %len(str3)
# yu3 = shu3 % len(str2)
# yu4 = shu4 %len(str3)
#
# zifu1 = str1[yu1]
# zifu2 = str3[yu2]
# zifu3 = str2[yu3]
# zifu4 = str3[yu4]
# yan = zifu1+zifu2+zifu3+zifu4
# print(yan)

'''
文件处理：
获取路径
os。getcwd()
切换路径
os.chdir()  #cd

新建文件
f = open('aaaa.txt','w')
f.close()

向文件中写入
f = open('cccc.txt','w')
f.write(内容)
f.close()

从文件中读取
f = open(r'路径','r',encoding='utf8')
neirong = f.read()
print(neirong)
f.close()
'''

# import os
#
# # ①　代码实现创建一个新文件”a.txt”，要求文件保存到桌面，向其中写入如下内容（4）
# os.chdir(r'C:\Users\Administrator\Desktop')
# # 向其中写入如下内容
# f = open('a.txt','w')
# f.write('''哥舒歌
# 西鄙人 〔唐代〕
# 北斗七星高，哥舒夜带刀。
# 至今窥牧马，不敢过临洮。
# ''')
# f.close()

# ②　代码实现再次打开文件，并向文件中写入如下内容，要求保留之前的内容（a）（5）
# f1 = open('a.txt','a')
# f1.write('''译文
# 黑夜里北斗七星挂得高高，哥舒翰勇猛守边夜带宝刀。
# 吐蕃族至今牧马只敢远望，他们再不敢南来越过临洮。
# ''')
# f1.close()

# ③　代码实现以只读方式打开文件，读取文件中的全部内容并打印到控制台（5）
# f2 = open('a.txt','r')
# neu = f2.read()
# print(neu)
# f2.close()


# import pymysql
#
# db = pymysql.connect(user='root',password='root',host='localhost',database='test123')
# yb = db.cursor()
#
# yb.execute('drop table book;')
# yb.execute('create table book(bookid int(10),author char(11),bookname char(11),printTime char(11));')
#
# yb.execute('desc book;')
# a = yb.fetchall()
# print(a)
#
# yb.execute('insert into book(bookid,author,bookname) values (1,"lpl","python3"),(2,"lzc","flask"),(3,"scy","session");')
# db.commit()
#
#
# yb.execute('select * from book;')
# b = yb.fetchall()
# print(b)
#
# db.close()






























