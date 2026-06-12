a,b,c=map(int,input().split())
plug=False

for i in range(a,b+1):
    if i%c==0: #c의 배수 하나라도 있으면 True
        plug=True

print("NO" if plug else "YES")