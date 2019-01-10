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
# # 实例化一个类的队形
# car = Car()
#
# # 给类对象的属性复制
# car.color = "黑色"
# car.wheel_num = 4
# print(car.color)
# print(car.wheel_num)
# # 调用对象的实例方法
# car.print_info()



class Car2:
    # 初始化函数，用来完成一些默认的设置
    def __init__(self, color, wheel_num):
        self.color1 = color
        self.wheel_num1 = wheel_num

    def do(self, a, b):
        pass


car = Car2("黑色", 4)
print(car.color1)
print(car.wheel_num1)
