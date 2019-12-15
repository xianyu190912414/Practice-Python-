height = float(input('请输入你的身高（/米）：'))
weight = float(input('请输入你的体重（/千克）:'))
BMI = weight / height ** 2
if BMI <= 18.5:
    print('偏瘦')
elif BMI <= 25:
    print('正常')
elif BMI <= 28:
    print('过重')
elif BMI <= 32:
    print('肥胖')
else:
    print('肥胖')
