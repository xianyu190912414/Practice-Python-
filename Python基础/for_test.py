names = ['Micheal', 'Harry', 'Bob']
for n in names:
    print('Hello, %s!' % n)

# 对于for循环，range(n)和list(range(n))是等价的
for x in range(10):
    print(x, end=' ')

print()

for y in list(range(10)):
    print(y, end=' ')
