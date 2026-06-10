mathA, engA = map(int,input().split())
mathB, engB = map(int,input().split())

if mathA > mathB :
    print("A")
elif mathA == mathB :
    if engA > engB :
        print("A")
    else : 
        print("B")
else :
    print("B")

