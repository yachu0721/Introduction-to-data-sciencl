x = int(input("請輸入一個正整數:"))
divisors = []
for i in range(1, x+1):
    if x % i == 0:
        divisors.append(i)
print(divisors)