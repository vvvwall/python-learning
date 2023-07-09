# 练习:
#   1. 北京出租车计价:
#     收费标准:
#       3公里以内收费13元
#       基本单价: 2.3元/公里 (超出3公里以外)
#       空驶费:超过15公里后，每公里加收单价的50%的空驶
#             费(即3.45元/公里)
#     要求:
#       输入公里数，打印出费用金额(以元为单位四舍五入)

km = int(input("请输入公里数: "))

# 方法1
# money = 0
# if 0 <= km <= 3:
#     money = 13  # 起步
# elif 3 < km <= 15:
#     money = 13 + 2.3 * (km - 3)
# else:
#     money = 13 + 2.3 * (km - 3) + 2.3 * 0.5 * (km - 15)

# 方法2
money = 13
if km > 3:
    money += 2.3 * (km - 3)

if km > 15:
    money += 2.3 * 0.5 * (km - 15)


print("您需要花费:", round(money))












