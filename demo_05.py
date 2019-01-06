def printInfo(name, age=18, score=100):
    # 函数参数
    # 带有默认值得参数一定位于参数列表的最后面
    """
    默认值参数
    :param name:
    :param age:
    :param score:
    :return:
    """
    # ctrl +d 复制当前行到下一行
    # ctrl +y 删除当前行
    print("name:{}".format(name))
    print("age:{}".format(age))
    print("score:{}".format(score))


# printInfo("xiaoming", 19)


# 不定长参数
def func(a, b, *args, **kwargs):
    print("a:{}".format(a))
    print("b:{}".format(b))
    print("args:{}".format(args))
    for key, value in kwargs.items():
        print("key:{}, value:{}".format(key, value))


# 格式化 alt+enter
# func(1, 2, 3, 4, 5, m=6, n=7)
# c = (3, 4, 5)
# d = {"m": 6, "n": 7}
# func(1, 2, *c, **d) # func(1,2 3,4,5,m=6,n=7)
# func(1, 2, c, d) # func(1,2, (1,2,3),{"m": 6, "n": 7})
# func(1,2, (1,2,3),{"m": 6, "n": 7})


# 引用传参
def add(a):
    """
    Python中函数参数是引用传递（注意不是值传递）。
    对于不可变类型，因变量不能修改，所以运算不会影响到变量自身；
    而对于可变类型来说，函数体中的运算有可能会更改传入的参数变量。
    :param a:
    :return:
    """
    a += a


# a_init = 1
# add(a_init)
# print(a_init)
# a_init = [1, 2]
# add(a_init)
# print(a_init)


# 递归函数
def calNum(n):
    """
    计算N的阶乘
    n! = n*(n-1)!
    :param n:
    :return:
    """
    """
    归纳出来计算的逻辑，n! = n*(n-1)!
    """
    if n >= 1:
        result = n * calNum(n - 1)
    else:
        result = 1
    return result


# print(calNum(4))


# 匿名函数 lambda
def operate_parms(a, b, opt):
    """
    匿名函数
    :param a:
    :param b:
    :param opt:
    :return:
    """
    print("result={}".format(opt(a, b)))


# operate_parms(1, 2, lambda x, y: x + y)

# def opt(a,b):
#     return a+b
# operate_parms(1,2, opt)


# 作业：
# 1，编程实现9*9乘法表
# 2. 用函数实现一个判断，用户输入一个年份，判断是否是闰年
# 3. 用函数实现输入某年某月某日，判断一下这一天是这一年的第几天，需要考虑闰年
name = input("我是谁？")
print("name是：{}".format(name))
