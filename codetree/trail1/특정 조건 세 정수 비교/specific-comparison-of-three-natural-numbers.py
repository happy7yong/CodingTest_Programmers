n,m,k = map(int,input().split())

print(1 if n == min(n,m,k) else 0,end=' ')
print(1 if n==m==k else 0)