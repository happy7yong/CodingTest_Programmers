sum = 0
avg = 0;
cnt = 0
for i in range(10) :
    a = int(input())
    if a >= 0 and a <= 200 :
        sum+=a
        cnt+=1

print(sum, round(sum/cnt,1))
