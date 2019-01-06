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

do_log('test.txt')
