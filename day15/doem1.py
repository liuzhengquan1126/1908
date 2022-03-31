#-*- coding = utf-8 -*-
#@Time : 2021/8/27 18:34
#@Author : lpl


def func1(a,b,c):
    he = a+b+c
    return he
#
# he1 = func1(1,2,3)
# print(he1)

def func2(a,b,c = 1):
    ji = a*b*c
    return ji

# ji1 = func2(2,3,4)
# print(ji1)
#
# ji2 = func2(2,3)
# print(ji2)

def func3(a,b,*args):
    print(a,type(a))
    print(b,type(b))
    print(args,type(args))

    he = sum(args)+a+b
    return he

# d = func3(1,2,3,4,5)
# print(d)

def func4(a,b,**kwargs):
    print(a, type(a))
    print(b, type(b))
    print(kwargs, type(kwargs))

    kwargs[a] = b
    return kwargs


# de = func4(1,2,m = 4,n=5,y=6)
# print(de)

num =100

def func5():
    global num
    num = num+10
    print(num)

