n = int(input())
students = []

class Student :
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

for _ in range(n):
    name,kor,eng,math = input().split()
    kor,eng,math = int(kor),int(eng),int(math)
    students.append(Student(name,kor,eng,math))

students.sort(key=lambda s:(s.kor+s.eng+s.math))

for student in students :
    print(student.name,student.kor,student.eng,student.math)
    



