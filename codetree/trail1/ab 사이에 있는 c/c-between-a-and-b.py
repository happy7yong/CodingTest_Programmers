a,b,c=map(int,input().split())
plg=0

for i in range(a,b+1) :
    if i%c==0 :
        print("YES")
        plg=1
        break;
if plg==0: print("NO")

