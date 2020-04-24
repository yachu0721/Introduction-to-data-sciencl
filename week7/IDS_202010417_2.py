monthly_income = input("請輸入月薪：")
saving_account = input("請輸入存款：")
monthly_income = int(monthly_income)
saving_account = int(saving_account)
print(type(monthly_income))
print(type(saving_account))
ans = ""
# 條件判斷(begin)
if monthly_income > 40000 or saving_account > 500000:
    ans = "發信用卡"
# 條件判斷(end)
print(ans)