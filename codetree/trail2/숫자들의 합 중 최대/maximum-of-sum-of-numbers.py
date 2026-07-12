s, e = map(int, input().split())

max_val = 0

for i in range(s,e+1) :
    a = list(map(int,str(i)))
    max_val = max(max_val,sum(a))

print(max_val)