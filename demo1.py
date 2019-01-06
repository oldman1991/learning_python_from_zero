# coding=utf-8

def func1(a, b):
    # print(a)
    # 打印出b的值
    print("你好")
    """

    :param a:
    :param b:
    :return:
    """

    """
    这是一个方法打印a,b的值
    
    
    """
    print(b)


num1 = 100
num2 = '50'

# int , str, bool, list, tuple, dict
# # type
# print(type(num1))
# num1 = "100"
# print(type(num1))
# 1. + - *
# a = "aa"
# print(a*2)
#
# # /?
# # //
#
# a = 19
# b =3
# print(a/b)
# print(a//b)
# print(a%b)
# **

# a = 2
# b = 3
# # print(a**b)
#
# # =  += a+=b: a= a+b  -= *= /= %= **= //= a**=b : a= a**b
# a+=b
# print(a)
# res = num1 +num2 #  res = 100 +50
# print(res)


# a = "100"
# print(a)
# print(type(a))
# print(type(int(a)))
# int()

# a = "10.1"
# print(float(a))
#
# int()
# float()
# a = 10.1
# print(type(a))
# print(type(str(a)))
# a = 1.1
# print(int(a))


# def demo1(a):
#     if a == 1:
#         print("我的值是1")
#         print("我的值是1")
#     elif a== 2:
#         print("我的值是2")
#     else:
#         print("我的值既不是1也不是2")
#
#
# # !=
# # > < >= <=
# demo1(3)


# def demo2(a, b):
#     if a==1 and b == 2:
#         print("a的值是1，b的值是2")
#     else:
#         print("不是1和2")
#
# demo2(1, 3)
#
# def demo3(a, b):
#     if a and b:
#         print("两个有一个是真的")
#     else:
#         print("两个都是假的")
#
#
# demo3(False, False)


# not # 非
# def demo4(a):
#     print(a)
#     print( a)
# demo4(True)

# def demo4(a):
#     while a < 10:
#         print(a)
#         a += 1
#
# demo4(0)

# def sum_num():
#     num = 0
#     a = 1
#     while a <= 100:
#         num += a
#         a += 1
#     return num
#
#
# print(sum_num())

# def sum_num1():
#     num = 0
#     a = 1
#     while a <= 100:
#         if a % 2 == 0:
#             num += a
#         a = a + 1
#     return num
#
# print(sum_num1())



"""
 *
 * *
 * * *
 * * * *
 * * * * *
"""


# def print_demo():
#     a = 1
#     while a <= 5:
#         b = 1
#         while b <= a:
#             print("* ", end='')
#             b += 1
#         print("\n")
#         a += 1
#
#
# print(print_demo())



def for_demo():
    a = "abcdefghijklmn"
    for item in a:
        print(item)
for_demo()

