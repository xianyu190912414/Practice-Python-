class Fib(object):
    def __init__(self):
        # 初始化两个计数器a, b
        self.a, self.b = 0, 1
    def __iter__(self):
        # 实例本身就是迭代对象，故返回自身
        return self 
    def __next__(self):
        # 给出循环的公式
        self.a, self.b = self.b, self.a + self.b
        # 设定退出循环的条件
        if self.a > 1000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n, end=' ')
