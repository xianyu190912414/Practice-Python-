# 定义一个quadratic(a,b,c)函数，返回ax*x+bx+c=0的两个解
import math
def quadratic(a, b, c):
    k = math.sqrt(b**2-4*a*c)
    m = (-b+k)/(2*a)
    n = (-b-k)/(2*a)
    return m, n

print(quadratic(4, 2, -42))
