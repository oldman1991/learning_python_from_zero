#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/01/11

# 面向对象

# 继承


class Cat:
    def __init__(self, name, color="白色"):
        self.name = name
        self.color = color

    def run(self):
        print("{}在奔跑".format(self.name))


class Bosi(Cat):
    def set_new_name(self, new_name):
        self.name = new_name

    def eat(self):
        print("{}在吃东西".format(self.name))

    def run(self):
        print("我是Bosi的run方法")


# bs = Bosi("印度猫")
# # 虽然子类没有定义__init__方法，但是父类有，所以子类在继承父类的时候这个方法就被继承了，所以
# # 只要创建Bosi的对象，就会默认调用继承的那个__init__方法
# print(bs.name)
# print(bs.color)
# bs.eat()
# bs.set_new_name("波斯猫")
# bs.run()

# 多继承
# python中是可以多继承的
# 父类中的方法，属性，子类都会继承
class A:
    def print_a(self):
        print("-----A-----")

    def do(self):
        print("----A do-----")


class B:
    def print_b(self):
        print("----B-----")

    def do(self):
        print("----B do-----")


class C(A, B):
    def print_c(self):
        print("-----C-------")


# objc_c = C()
# objc_c.print_a()
# objc_c.print_b()
# objc_c.print_c()
# print(C.__mro__) # C类对象搜索方法时的先后顺序
# objc_c.do()


# 在子类中重写父类的方法
# 就是在子类中有一个和父类名字一样的方法，在子类中的方法会覆盖掉父类中同名的方法

class Dog():
    def say(self):
        print("dog.say")


class HbDog(Dog):
    def say(self):
        print("habog.say")

    def say_father(self):
        super().say()

        # def say(self, aaa):
        #     print(aaa)


doga = HbDog()
doga.say()
doga.say("aaa")
doga.say_father()


# master 分支一般是线上的
# test 分支是在测试环境上的
# dev 分支是你在开发的时间用的
