n = int(input())

class Student :
    def __init__(self,height,weight,index) :
        self.height = height
        self.weight = weight
        self.index = index

students = []

for i in range(1,n+1) :
    height,weight = input().split()
    height = int(height)
    weight = int(weight)
    students.append(Student(height,weight,i))

students.sort(key=lambda s:(-s.height,-s.weight,s.index))

for student in students :
    print(student.height,student.weight,student.index)

