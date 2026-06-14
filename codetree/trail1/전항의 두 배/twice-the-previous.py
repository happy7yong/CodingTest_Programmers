A1,A2 = map(int,input().split())

p = A2
pp = A1
arr=[pp,p]

while True :
    pp,p = p,2*pp+p
    arr.append(p)
    if len(arr) == 10 :
        break;

print(" ".join(map(str,arr)))