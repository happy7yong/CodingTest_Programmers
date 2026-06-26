n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

students.sort(key=lambda s :( s[0],-s[1]))

for student in students :
    print(" ".join(map(str,student)))