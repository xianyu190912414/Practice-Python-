def foo(s):
     n = int(s)
     assert n != 0, 'n is zero'
     return 10 / 0

def main():
    foo('0')

main()
