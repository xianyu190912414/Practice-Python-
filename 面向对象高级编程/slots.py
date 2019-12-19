class Student(object):

    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age')

class GraduateStudent(Student):
    pass

s = Student()
s.name = 'Micheal'
s.age = 25
# s.score = 99

g = GraduateStudent()
g.score = 99
print('g.score = ', g.score)
