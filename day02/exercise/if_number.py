# 练习：
#   任意输入一个数
#     1) 判断这个数是否大于100
#     2) 判断这个数是否小于0
#     3）判断这个数是否在80~100之间

n = int(input("请输入一个数: "))
# 1) 判断这个数是否大于100
if n > 100:
    print(n, "大于100")
else:
    print(n, '不大于100')

# 2) 判断这个数是否小于0
if n < 0:
    print(n, '小于0')
else:
    print(n, '不小于0')
# 3）判断这个数是否在80~100之间
if 80 < n < 100:
    print(n, '在80~100之间')
else:
    print(n, '不在80~100之间')
