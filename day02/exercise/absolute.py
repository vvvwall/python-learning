# 练习:
#   1. 写一个程序，输入一个数，用if语句计算这个数
#    的绝对值并打印出来
#   2. 写一个程序，输入一个数，用条件表达式计算这
#    个数的绝对值并打印出来

n = int(input("请输入一个数: "))
# 方法1
# if n < 0:
#     a = -n
# else:
#     a = n
# 方法2
a = n  # 先用a绑定原来的数
if a < 0:  # 如果a为负数，则翻转符号
    a = -a  # << 翻转符号
print('绝对值是:', a)

b = -n if n < 0 else n
print("用条件表达式计算过的绝对值是:", b)



