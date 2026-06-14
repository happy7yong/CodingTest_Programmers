n = int(input())
arr = list(map(float,input().split()))
sum=0
cnt=0

for ele in arr :
    sum+=ele
    cnt+=1

avg = sum/cnt
print(round(avg,1))
if avg>=4.0 :
    print("Perfect")
elif avg>=3.0 :
    print("Good")
else : 
    print("Poor")