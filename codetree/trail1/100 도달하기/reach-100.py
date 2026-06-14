n=int(input())

arr = [1,n]
pp = 1
p = n

while True:
    pp,p = p,pp+p
    arr.append(p)

    if p>100 :
        break;

print(" ".join(map(str,arr)))
