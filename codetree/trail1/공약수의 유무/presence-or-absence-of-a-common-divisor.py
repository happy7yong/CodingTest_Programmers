a,b=map(int,input().split())
plug=False

for i in range(a,b+1):
    if 1920%i==0 and 2880%i==0 :
        plug=True

print(1 if plug else 0)