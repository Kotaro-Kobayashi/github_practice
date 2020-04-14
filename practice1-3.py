# BMIの計算
cm = float(input('身長(cm)を入力>>'))
kg = float(input('体重(kg)を入力>>'))

m = cm / 100

BMI = kg / m / m

print('君のBMIは{}ですよ' .format(BMI))
