from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L))
print(sorted(L, key=str.lower, reverse=True))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda s: s[1]))
print(sorted(students, key=itemgetter(1), reverse=False))
