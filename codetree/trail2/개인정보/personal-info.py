n = 5
persons=[]

class Person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

for _ in range(n):
    name, h, w = input().split()
    height=int(h)
    weight=float(w)
    persons.append(Person(name,height,weight))

persons_name = persons[:]
persons_height = persons[:]
persons_name.sort(key=lambda p : (p.name))
persons_height.sort(key=lambda p : (-p.height))

print("name")
for person in persons_name:
    print(person.name,person.height,person.weight)
print()
print("height")
for person in persons_height:
    print(person.name,person.height,person.weight)