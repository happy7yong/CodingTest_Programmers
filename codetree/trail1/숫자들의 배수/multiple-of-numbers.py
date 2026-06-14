n = int(input())
arr = []
i=1
cnt=0

while True :
    current = n*i
    i+=1
    arr.append(current)
    if current%5==0 :
        cnt+=1
    
    if cnt==2 :
        break;

print(" ".join(map(str,arr)))
    