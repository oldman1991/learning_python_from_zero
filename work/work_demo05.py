#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/1/10

# 1，编程实现9*9乘法表
# 2. 用函数实现一个判断，用户输入一个年份，判断是否是闰年
# 3. 用函数实现输入某年某月某日，判断一下这一天是这一年的第几天，需要考虑闰年
import datetime


def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(str(j) + "*" + str(i) + "=" + str(i * j), end="\t")  # \t 横向制表符
        print()


# multiplication_table()


def is_leap_year(year):
    assert type(year) == int
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


# print(is_leap_year(1997))
# print(is_leap_year(2000))


def get_which_days(date):
    date_today = datetime.datetime.strptime(date, '%Y-%m-%d')
    print(type(date_today))
    print(date_today.year)
    print(date_today.month)
    print(date_today.day)
    count = 0
    # 判断该年是平年还是闰年
    if (date_today.year % 4 == 0 and date_today.year % 100 != 0) or date_today.year % 400 == 0:
        print('%d年是闰年，2月份有29天！' % date_today.year)
        li1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(date_today.month - 1):
            count += li1[i]
        return count + date_today.day
    else:
        print('%d年是平年，2月份有28天！' % date_today.year)
        li2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(date_today.month - 1):
            count += li2[i]
        return count + date_today.day


print(get_which_days('2018-02-1'))
