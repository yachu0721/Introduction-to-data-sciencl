x = int(input("請輸入起始的正整數:"))
y = int(input("請輸入終止的正整數:"))
odds = []
for i in range(x, y+1):
  mod = i % 2
  if mod == 1:
      odds.append(i)
print(odds)
print("-----------------------")
print(len(odds)) # 計數
print("-----------------------")
print(sum(odds)) # 加總