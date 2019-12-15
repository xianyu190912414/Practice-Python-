# 用while循环求1+2+3+...+100的和
sum = 0
n = 1
while n < 101:
    sum += n
    n += 1
print(sum)

# 用while循环求1到20的阶乘
acc = 1
n = 1
while n < 21:
    acc *= n
    n += 1
print(acc)
