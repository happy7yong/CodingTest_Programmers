n = int(input())

person_arr = [ ]

class Person :
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

for _ in range(n):
    n_i, h_i, w_i = input().split()
    person_arr.append(Person(n_i, int(h_i), int(w_i)))

person_arr.sort(key=lambda p : p.height)

for person in person_arr :
    print(person.name,person.height,person.weight)