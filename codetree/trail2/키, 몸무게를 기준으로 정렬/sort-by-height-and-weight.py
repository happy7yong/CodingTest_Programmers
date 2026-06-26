n = int(input())
persons = []

class Person:
    def __init__(self,name,height,weight) :
        self.name = name
        self.height = height
        self.weight = weight

for _ in range(n):
    name,height,weight = input().split()
    height=int(height)
    weight=int(weight)
    persons.append(Person(name,height,weight))

persons.sort(key=lambda p :(p.height,-p.weight))

for person in persons :
    print(person.name,person.height,person.weight)


