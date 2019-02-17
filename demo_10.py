#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/02/17
"""
类属性，实例属性
"""

class People():
    name = 'Tom'  # 公有的类属性
    __age = 12  # 私有的类属性
#
#
# p = People()
# print(p.name)
# print(People.name)
# print(p.__age)  # 错误的写法，不能再类外通过实例对象访问私有的类属性
# print(People.__age)  # 错误的写法， 不同在类外通过类对象访问私有的类属性


# class People(object):
#     address = '河南'  # 类属性
#
#     def __init__(self):
#         self.name = 'oldman'  # 实例属性
#         self.age = 18  # 实例属性
#
#
# p = People()
# p.age = 12  # 实例属性
# print(p.name)
# print(p.address)
# print(p.age)
#
# print(People.address)
# # print(People.age)
#
# p.address = 'beijing'
# print(p.address)  # 实例属性会屏蔽掉同名的类属性
# print(People.address)
# del p.address  # 删除实例属性
# print(p.address)


# 类方法
# 是类对象所拥有的方法，需要用修饰器@classmethod来标识其为类方法，
# 对于类方法，第一个参数必须是类对象，
# 一般以cls作为第一个参数（当然可以用其他名称的变量作为其第一个参数，
# 但是大部分人都习惯以'cls'作为第一个参数的名字，就最好用'cls'了），
# 能够通过实例对象和类对象去访问。
# class People(object):
#     country = 'china'
#
#     @classmethod
#     def getCountry(cls):
#         return cls.country
#
#     @classmethod
#     def setCountr(cls, country):
#         cls.country = country
#
#     @staticmethod
#     def staticGetCountry():
#         return People.country


# print(People.getCountry())  # 可以通过类对象调用
# p = People()
# print(p.getCountry())  # 也可以通过实例对象去调用
#
# p.setCountr('zhongguo')
# print(p.getCountry())
# print(People.getCountry())
# print(People.staticGetCountry())
import time

"""
从类方法和实例方法以及静态方法的定义形式就可以看出来，
类方法的第一个参数是类对象cls，那么通过cls引用的必定是类对象的属性和方法；
而实例方法的第一个参数是实例对象self，那么通过self引用的可能是类属性、
也有可能是实例属性（这个需要具体分析），不过在存在相同名称的类属性和实例属性的情况下，
实例属性优先级更高。
静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用
"""


# __new__()方法

# class A(object):
#     def __init__(self):
#         print("这是一个init方法")
#
#     def __new__(cls, *args, **kwargs):
#         print("这是new方法")
#         return object.__new__(cls, *args, **kwargs)
#
#
# a = A()
# print(a.age)


# 单例模式

# class Singleton(object):
#     __instance = None
#     __initflag = False
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, age, name):
#         if not self.__initflag:
#             self.age = age
#             self.name = name
#             self.__initflag = True
# a = Singleton(18, 'oldman')
# b = Singleton(20, 'john')
# print(id(a))
# print(id(b))
# # a.age = 22
# # print(b.age)
# print(a.name)
# print(b.name)

# 异常
# try:
#     print(1)
#     # open('123.txt', 'r')
#     print(2)
# except Exception as e:
#     print(e)
# # finally:
# #     print(3)
# else:
#     print("没有异常")

# 异常的传递
# try:
#     f = open('test1.txt')
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(2)
#             print(content)
#     finally:
#         f.close()
#         print('关闭文件')
# except:
#     print('没有这个文件')

def test1(a):
    print("------test1-1-------")
    # print(num)
    if a > 2:
        raise ValueError("数值不能大于2")
    print("----test1-2")

def test2():
    print("--------test2-1----")
    test1(3)
    print('----test2-2----')

def test3():
    try:
        print('-----test3-1----')
        test2()
        print('-----test3-2')
    except Exception as e:
        print(e)
test3()

"""
如果try嵌套，那么如果里面的try没有捕获到这个异常，
那么外面的try会接收到这个异常，然后进行处理，如果外边的try依然没有捕获到，那么再进行传递。。。
如果一个异常是在一个函数中产生的，例如函数A---->函数B---->函数C,而异常是在函数C中产生的，
那么如果函数C中没有对这个异常进行处理，
那么这个异常会传递到函数B中，如果函数B有异常处理那么就会按照函数B的处理方式进行执行；
如果函数B也没有异常处理，那么这个异常会继续传递，以此类推。。。如果所有的函数都没有处理，
那么此时就会进行异常的默认处理，即通常见到的那样
注意观察上图中，当调用test3函数时，
在test1函数内部产生了异常，此异常被传递到test3函数中完成了异常处理，而当异常处理完后，
并没有返回到函数test1中进行执行，而是在函数test3中继续执行

"""