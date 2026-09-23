n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
for _ in range(t) :
    l_end = l[n-1]
    r_end = r[n-1]
    d_end = d[n-1]

    for i in range(n-1, 0, -1) :
        l[i] = l[i-1]
        r[i] = r[i-1]
        d[i] = d[i-1]
    
    l[0] = d_end
    r[0] = l_end
    d[0] = r_end

print(*l)
print(*r)
print(*d)
