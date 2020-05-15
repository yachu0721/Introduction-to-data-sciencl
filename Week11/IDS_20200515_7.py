living_area = input("請輸入您的居住城市:")

# 方法一
living_cost = None
if living_area == '臺北市':
    living_cost = 17005
elif living_area == '新北市':
    living_cost = 15500
elif living_area == '桃園市':
    living_cost = 15281
elif living_area == '臺中市':
    living_cost = 14596
elif living_area == '臺南市':
    living_cost = 12388
elif living_area == '高雄市':
    living_cost = 13099
elif living_area == '非六都之縣市':
    living_cost = 12388
elif living_area == '金門縣連江縣':
    living_cost = 11648

if living_cost is None:
    print("請重新輸入居住縣市")
else:
    print("{}的每人每月最低生活費為{:,}".format(living_area, living_cost))