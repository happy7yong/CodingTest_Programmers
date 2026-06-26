start_h, start_m, end_h, end_m = map(int, input().split())

sum=0
mins = 0
hour = 0
cnt=0

while True :
    if start_h == end_h and start_m == end_m :
        break;
    
    start_m+=1
    cnt+=1

    if start_m == 60 :
        start_m=0
        start_h+=1

print(cnt)
