# 注释，
# a = 10
# type(a)  # 判断a的数据类型
# str(a) # 把a转换成str类型
# # 运算符 + - * / // %  += -= *= < > == and or not
# # 判断语句和循环语句 while， if elif else for  for item in list:

# 1.字符转 str
# 2. 列表 list
# 3. 元祖 tuple
# 4. 字典 dict
#
# a = "我是一个python字符串"
# print(type(a))
# b = 100
# c = "100"
#
# d = '100'
# print(type(b))
# print(type(c))
# print(type(d))
# 字符串的输出 print()
# a = "我是一个python字符串"
# b = "我是b"
# print("a的值是什么：%s" % a)
# print("a的值是什么：{}, b的值是什么：{}".format(a, b))
# # print("a的值是什么：{}, b的值是什么：{}".format(a))  # error
# print("a的值是什么：{}".format(a, b))

# 字符串的输入

# username = input("请输入用户名：")
# print("用户名为：{}".format(username))
# password = input("请输入密码：")
# print("密码为：{}".format(password))

# 字符串的下标和切片
# a = "abcdefg"
# print(a[0])
# print(len(a))
# print(a[7])
# a = "abcdefghijk"
# a[起始:结束:步长]
# print(a[0:2:1])
# print(a[0:2])
# print(a[2:4])
# print(a[2:])
# print(a[2:-1])  # 从下标2开始到最后第二个之间的元素
#
# print(a[:])  # 全部数据
# print(a[::-1])


# 字符串的常见操作
# 1. find
# mystr = "hello world i use python"
# str = "wor"
# print(mystr.find(str))
# print(mystr.find(str, 0, 5))
# print(mystr.find("china"))

# 2 index

# mystr = "hello world i use python"
# str = "wor"
# print(mystr.index(str))
# print(mystr.index(str, 0, 5))


# 3. count
# mystr = "hello world i use python hello"
# str = "hello"
# print(mystr.count(str))
# print(mystr.count("you"))


# 4. replace 替换
# mystr = "hello world i use python hello"
# str = "HELLO"
# print(mystr.replace("hello", str, 1))
# print(mystr.replace("hello", str))

# 5.split
# mystr = "hello world i use python hello"
# print(mystr.split(" "))


# 6. isdigit 如果字符串只包含数字的话返回True，否则返回False

# a = "100000"
# b = "10000a"
# print(a.isdigit())
# print(b.isdigit())

# 7. join
# str = "_"
# str_list = ["my", "name", "is", "oldman"]
# print(str.join(str_list)) # my_name_is_oldman


# 列表
# nameList = ["oldman", "xiaozhang", "xiaowang", 1, 23]
# print(nameList[0])
# print(nameList[1])
# print(nameList[2])
# print(nameList[3])
# print(nameList[4])

# 1. 列表的循环遍历
# name_list = ["xiaozhang", "xiaowang", "xiaoli", 12]
# for item in name_list:
#     print(item)
# lenth = len(name_list)
# i = 0
# while i < lenth:
#     print(name_list[i])
#     i += 1

# 2. 添加元素 append, extend, inset
# list_a = ["xiaozhang", "xiaowang","xiaoli"]
# print("-----------添加元素之前list_a的数据-----------------")
# for item in list_a:
#     print(item)
# list_a.append("xiaozhang")
# print("-----------添加元素之后list_a的数据-----------------")
# for item in list_a:
#     print(item)
# a = [1, 2]
# b = [3, 4]
# a.extend(b)  # 把b中的元素逐一的添加到a中去
# for item in a:
#     print(item)
# a.insert(1, 5)
# for item in a:
#     print(item)

# 2. 修改元素
# list_a = ["xiaozhang", "xiaowang","xiaoli"]
# print(list_a[0])
# list_a[0] = "zhangxiao"
# print(list_a[0])

# 3. 查找元素 in,not in
# list_a = ["xiaozhang", "xiaowang","xiaoli"]
# in： 如果存在结果为True, 如果不存在，结构为False
# if "xiaozhang" in list_a:
#     print("在列表中找到了相同的元素")
# else:
#     print("没有找到")

# not in 如果不存在，则返回True，如果存在则返回Falser
# if "xiaozhang" not in list_a:
#     print("在列表中找到了相同的元素")
# else:
#     print("没有找到")

# index count
# a = ['a', 'b', 'c', 'd', 'a', 'b']
# print(a.index('a', 0, 3)) # 注意这个地方还是左闭右开
#
# print(a.count("a"))

# 4. 删除元素 del pop remove
# a = ['a', 'b', 'c', 'd', 'a', 'b']
# print("------------------删除之前-------------")
# for item in a:
#     print(item)
# del a[0]
# print("--------------------删除之后------------------")
# for item in a:
#     print(item)

# a = ['a', 'b', 'c', 'd', 'a', 'b']
# print("------------------删除之前-------------")
# for item in a:
#     print(item)
# a.pop()
# print("--------------------删除之后------------------")
# for item in a:
#     print(item)

# a = ['a', 'b', 'c', 'd', 'a', 'b']
# print("------------------删除之前-------------")
# for item in a:
#     print(item)
# a.remove("a")
# a.remove("a")
# print("--------------------删除之后------------------")
# for item in a:
#     print(item)

# 5. sort reverse

# a = [1, 3, 5, 7, 9, 0, 8, 2, 6, 4]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a = [1, 3, 5, 7, 9, 0, 8, 2, 6, 4]
# a.reverse()
# print(a)

# 列表的循环嵌套
import random

a = ["a", 1, [1, 2, 3]]
a = [1, 2, [3, 4], 5, 6]

# 一个公司，有三个办公室，一共有十名员工，请编写程序，完成随机分配
offices = [[], [], []]
names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)
i = 1
for office in offices:
    print("办公室{}的人数为：{}".format(i, len(office)))
    for name in office:
        print("名字是：{}".format(name))
    i = i + 1
