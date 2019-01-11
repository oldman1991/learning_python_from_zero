#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/01/10

# 面向对象oo
# 定义一个类
# class Car:
#
#     #
#     def print_info(self):
#         print("I am a car")
#
#
# # 实例化一个类的对象
# car = Car()
#
# # 给类对象的属性复制
# car.color = "黑色"
# car.wheel_num = 4
# print(car.color)
# print(car.wheel_num)
# # 调用对象的实例方法
# car.print_info()
import time


class Car2:
    # 初始化函数，用来完成一些默认的设置
    # 1. __init__方法，在创建对象时默认被调用，不需要手动调用
    # 2. __init__方法中，默认有一个参数名字self，如果在创建对象时传递了2个参数，那么
    # __init__(self)中self作为第一个参数外还需要两个参数
    # 3. __init__方法中的self参数，不需要开发者传递，python的解释器会自动把当前对象引用
    # 传递给self
    def __init__(self, color, wheel_num):
        self.color1 = color
        self.wheel_num1 = wheel_num

    def do(self):
        print(self.color1)

    def __str__(self):
        return "I am a car"


# 在python中方法名称如果是__XX__()的，那么就有特俗功能，我们俗称“魔法方法”
# 在使用print输出对象的时间，只要自己定义了__str__（）方法，
# 那么就会打印从这个函数中return的数据

# car = Car2("黑色", 4)
# car.do()
# print(car)
# print(car.color1)
# print(car.wheel_num1)


class People:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) < 3:
            self.__name == "xiaoming"
        else:
            self.__name = name


# p = People("xiaozhang")
# # print(p.__name)  # 错误的写法

# print(p.get_name())
# 如果在属性名前面加了2个下划线'__', 则表明该属性是私有属性，否则为共有属性(方法也是一样的，
# 方法名前面加了2个"__"下划线表示方法是私有的，否则是公有的)


# __del__方法 在删除一个对象时，python解释器也会默认的调用一个方法就是__del__方法
class Animal(object):
    # 初始化方法
    def __init__(self, name):
        print("__init__方法被调用")
        self.__name = name

    # 析构方法
    # 当对象被回收的时候，会自动被调用
    def __del__(self):
        print("__del__方法被调用")
        print("{}对象马上就要被干掉了".format(self.__name))

dog = Animal("京巴狗")
del dog

cat = Animal("波斯猫")
cat2 = cat
cat3 = cat
print("-----马上开始删除cat对象-----")
del cat
print("-----马上开始删除cat2对象-----")
del cat2
print("-----马上开始删除cat3对象-----")
del cat3

print("程序5秒钟后结束")
time.sleep(5)

# 当有一个变量保存了对象的引用时，此对象的引用计数就会加1
# 当使用del删除变量指向的对象时，对象的引用计数会减一
# 当对象的引用计数为0时，会触发垃圾回收
