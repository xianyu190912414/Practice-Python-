# ————利用埃氏筛法求1000以内的素数————
# 构造产生奇数列表的函数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 构造不能因式分解的判断函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 构造产生素数列表的函数，利用filter,将可以因式分解的奇数剔除
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

# 构造主函数，将素数控制在1000以内
def main():
    for n in primes():
        if n < 1000:
            print(n, end=' ')
        else:
            break
            
# 运行主函数，产生1000以内的质数
if __name__ == '__main__':
    main()
