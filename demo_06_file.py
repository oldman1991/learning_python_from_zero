# 文件操作
# f = open("test.txt", 'r')
# content = f.read(10) # 读取字节
# redilines方法读取所有的行，返回行的list
# print(type(f))
# content = f.readlines()
#
# for lin in content:
#     print(lin)
# print(type(content))
# content = f.readline()
# print(type(content))
# print(content)
# content1 = f.readline()
# print(content1)
# line = f.readline()
# while line:
#     print(line)
#     line = f.readline()
# f.close()


def do_log(path):
    f = open(path, 'r')
    result_list = []
    line = f.readline()
    while line:
        data = line.split(',')
        result_list.append({
            "datetime": data[0],
            "user_id": data[1],
            "method": data[2]
        })
        line = f.readline()
    f.close()
    print(result_list)


# do_log('test.txt')

# f= open("test.txt", "a+")
# f.write("hello world! I am coming\n")
# f.close()

# 文件的备份

def copy_file(file_path):
    """
    文件copy
    :param file_path: 被复制文件的路径
    :return:
    """
    oldfile = open(file_path, "r")
    if oldfile:
        # 提取文件的猴嘴
        file_flag_num = file_path.find(".")
        if file_flag_num > 0:
            file_flag = file_path[file_flag_num:]
    new_flie_name = file_path[:file_flag_num] + "[复件]" + file_flag
    # 创建新文件
    new_file = open(new_flie_name, "w")
    for line in oldfile.readlines():
        new_file.write(line)
    oldfile.close()
    new_file.close()

# copy_file("test.txt")

# 文件的重命名
import os
# os.rename("test.txt", "test1.txt")

# 文件的删除
# os.remove("test[复件].txt")

# 文件夹的操作，创建，获取当前目录
# os.mkdir("new")
print(os.getcwd())