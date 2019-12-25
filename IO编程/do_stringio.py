from io import StringIO

# 从内存中写
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# 从内存中读
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
