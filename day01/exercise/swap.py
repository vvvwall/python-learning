
# 2. 交量交换练习:
#    已知有两个变量:
#      a 绑定 10000
#      b 绑定 20000
#    问,在不创建任何新数据对象的情况下，如何让a 和 b 交换绑定的对象
#    a = 10000
#    b = 20000
#    ....
#    print(a)  # 20000
#    print(b)  # 10000

a = 10000
b = 20000
# C语言做法， 用临时的第三个变量来绑定一个数据
# temp = a
# a = b
# b = temp  # 交换

a, b = b, a

print(a)  # 20000
print(b)  # 10000