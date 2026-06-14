a,b= map(int,input().split()) 

# 2 4 6 8
for i in range(2,9,2) :
    for j in range(b,a-1,-1) :
        print(f"{j} * {i} = {j*i}",end="")
        if not a>=j : print(" / ",end="")
    print()