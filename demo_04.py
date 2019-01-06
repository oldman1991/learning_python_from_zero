# a = 1
# b = a
# print(id(a))
# print(id(b))
# # print(b)
# a = 2
# print(id(a))
# print(id(b))
# # print(a)
# # print(b)
#
# a = [1, 2]
# b = a
# print(id(a))
# print(id(b))
# print(b)  #
# a.append(3)
# print(a)  #
# print(b)  #
#
# print(id(b))
# print(id(a))

# 可变类型：
# 列表lsit，字典dict

# 不可变类型：
# 字符串str，数值类型(int，long，bool，float)， 元组tuple

# a = (1, 2, 3)
# b = a
# print(id(a))
# print(id(b))
# a = (1, 2, 3, 4)
# print(id(a))
# print(id(b))

# 函数


# def printInfo():
#     """
#     打印信息方法
#     :return:
#     """
#     print("======================================")
#     print("人生苦短，我用python")
#     print("=======================================")
#
# print(help(printInfo))
# printInfo()
# def add(a, b):
#     """
#     打印a加b之后的值
#     :param a:
#     :param b:
#     :return:
#     """
#     c = a + b
#     print(c)
#
#
# add(1, 2)
# add(a=1, b=2)
# add(b=2, a=1)

# def add_no_return(a, b):
#     """
#
#     :param a:
#     :param b:
#     :return:
#     """
#     c = a+b
#     # print(c)
#
#
# def add(a, b):
#     """
#     返回a+b的值
#     :param a:
#     :param b:
#     :return: a+b的值
#     """
#     c = a + b
#     return c
#
# res1 = add_no_return(1,2)
# res2 = add(1, 2)
# print(res1)
# print(res2)

# def testB():
#     print('-------------testb strat-----')
#     print('这里是testb的函数执行的代码....')
#     print('-------------------testb end')
#
#
# def testA():
#     print('-------------testa strat-----------')
#     testB()
#     print('-----------------------------testb end-----------')
#
# testA()

# def testA():
#     a = 100
#     print(a)
#
#
# def testB():
#     a = 101
#     print(a)

# a = 100
#
#
# def testA():
#     global a
#     a = 300
#     print(a)
#
#
# def testB():
#     print(a)
#
# testA()
# testB()

# a = 100
# def testA():
#     a = a+100
#     print(a)

# a = [1, 2]
#
#
# def testA():
#     a.append(3)
#     print(a)
# testA()
"""
在函数中不使用global声明全局变量时不能修改全局变量的本质是不能修改全局变量的指向，即不能将全局变量指向新的数据。
对于不可变类型的全局变量来说，因其指向的数据不能修改，所以不使用global时无法修改全局变量。
对于可变类型的全局变量来说，因其指向的数据可以修改，所以不使用global时也可修改全局变量。
"""


def divid(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


sh, yu = divid(5, 2)
print(sh)
print(yu)
"""
可变对象，不可变对象，方法的定义，全局变量，局部变量，global
"""