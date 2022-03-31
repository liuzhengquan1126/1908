#-*- coding = utf-8 -*-
#@Time : 2021/9/1 15:38
#@Author : lpl
#@File : jiami.py

'''A B C D E  '''
# def jiami(str = 'qwer'):
#     da = {"A":'C',"B":'D','C':'E','D':'A','E':'B',"a":'c',"b":'d','c':'e','d':'a','e':'b'}
#     # xiao = {"a":'c',"b":'d','c':'e','d':'a','e':'b'}
#
#     xin = ''
#     for i in str:
#         if i.isalpha():
#             xin = xin +da[i]
#         else:
#             xin = xin+i
#
#     return xin

'''
ord（字母）           # 将字母转化为对应的ascii 码值
chr(数字)  #   将数字转化为对应 字符    
'''
# print(ord('a')+2)
# print(chr(99))

def jiami2(str1):
    xin = ''
    for i in str1:
        if i.isalpha() and('a'<= i <='x' or 'A'<=i <= "X"):
            xin =xin + chr(ord(i)+2)
        elif i == 'y':
            xin = xin + 'a'
        elif i =='z':
            xin = xin +'b'
        elif i == 'Y':
            xin = xin +'A'
        elif i == 'Z':
            xin = xin +"B"
        else:
            xin = xin+i

    return xin

def wenjianjiami(fname):
    f = open(fname,'r')
    str2  = f.read()
    f.close()
    miwen = jiami2(str2)

    name = str(fname).split('.')[0]
    f = open(name + '-加密后.txt','w')
    f.write(miwen)
    f.close()

wenjianjiami('hehehe.txt')

