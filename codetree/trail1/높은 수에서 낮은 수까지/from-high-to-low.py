a,b = map(int,input().split())
max = max(a,b)
min = min(a,b)

for i in range(max,min-1,-1) :
    print(i,end=" ")
