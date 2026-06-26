m1, d1, m2, d2 = map(int, input().split())


numsOfDate = [0,31,28,31,30,31,30,31,31,30,31,30,31]
cnt=0

while True :
    cnt+=1
    if m1 == m2 and d1 == d2 :
        break
    
    d1+=1
    if numsOfDate[m1] < d1 :
        d1 = 1
        m1 += 1

print(cnt) 