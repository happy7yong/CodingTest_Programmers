n = int(input())

for i in range(1,n+1):
    for j in range(i,n+i):
        print(10+(2*j-1),end=" ")
    print()