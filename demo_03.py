"""
元组和字典
"""
# tuple(元组)
# list_a = []
# list_a.append(1)

tuple_a = ("aaa", 1111, 2222, "aaa")
# print(tuple_a)
# print(tuple_a[0])
# tuple_a[0] = "bbb"
# # index方法
# index = tuple_a.index("aaa")
# print(index)
# index = tuple_a.index("bbb")

# count 方法
# print(tuple_a.count("aaa"))

# 字典(dict)
# 定义
# items = {"name": "xiaohuaya", "age": 18, "friends": [], 11: "111", (111, 222): "jskdjksa"}

items = {"name": "xiaohuaya", "age": 18, "friends": []}
# 字典的key必须是不可变类型的，因为字典的底层存储是哈希表，对key做hash，要求就是key是不可变的
items1 = dict()
# print(type(items))
# print(type(items1))
# print(items)
# print(items["name"])
# print(items["name1"])

# 1.修改元素,添加元素
# items["name"] = "小虎牙啊"
# items["gender"] = 0
# print(items)

# 2.删除元素
# del items["gender"]
# print(items)
# del items
# print(items)
# items.clear()
# print(items)

# 3. 常用方法
# print(len(items))
# print(items.keys())
# print(items.values())
# print(items.items())

# 集合(集合里面的数据不能有重复)
# a = set()
# print(type(a))

# 遍历 我们可以使用for .... in ....语法遍历字符串， 列表，元组，字典

# 遍历字符串
# str_a = "abcdefghijklmn"
# for item in str_a:
#     print(item)

# 列表：
# list_a = [1,2,3,"aa", "bb"]
# for item in list_a:
#     print(item)

# 元组
# tuple_a = (1,2,3,2,3,4)
# for item in tuple_a:
#     print(item)

# 字典遍历
dict_a = {"a": 1, "b": 2, "c": 3, "d": 4}
# for item in dict_a.keys():
#     print(item, dict_a[item])

# for item in dict_a.items():
#     print(item)

# list_a = [1, 2, 3, "aa", "bb", 1, 2]
# for index, value in enumerate(list_a):
#     print("index:{}, value:{}".format(index, value))
# 只有set里面的元素是不可以重复的，list，tuple都是可以重复的，字典的key是不会重复的


tuple_a = (1, 2, 3, 4)
print(tuple_a[1])

# 错误使用
set_a = set([1, 2, 3])
# print(set_a[0])
