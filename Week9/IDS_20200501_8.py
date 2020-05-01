x = int(input("請輸入一個正整數:"))
i = 1 # start
divisor_counter = 0 # 歸零
while i <= x: # stop
    if x % i == 0:
        divisor_counter += 1
        print("{}可以被{}整除".format(x, i))
        print("因數個數目前有{}個".format(divisor_counter))
        print("======")
    i += 1 # step
    if divisor_counter > 2:
        break    
print("### Answer ###")
print("總共執行了{}次迴圈".format(i - 1))
if divisor_counter == 2:
    print("{}是質數".format(x))
else:
    print("{}不是質數".format(x))