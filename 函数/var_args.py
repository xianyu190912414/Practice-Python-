# 构建一个带有可变参数的函数
def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ','.join(args)))

hello('Hi')
hello('Hi','Sarah')
hello('Hello', 'Micheal', 'Bob', 'Adam')

# 先构造tuple,然后将tuple作为可变参数传入函数
names = ('Bart', 'Lisa')
hello('Hello', *names)
