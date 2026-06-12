plug = False

for _ in range(5) :
    a = int(input())
    if a%3!=0 :
        plug = True

print(0 if plug else 1)