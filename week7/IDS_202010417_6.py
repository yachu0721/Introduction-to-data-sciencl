input_height = float(input("請輸入身高（公分）："))
input_weight = float(input("請輸入體重（公斤）："))
bmi = input_weight / (input_height*0.01)**2
if bmi > 30:
    label = "Obese"
elif bmi > 25:
    label = "Overweight"
elif bmi > 18.5:
    label = "Normal weight"
elif bmi <= 18.5:
    label = "Underweight"
print(label)