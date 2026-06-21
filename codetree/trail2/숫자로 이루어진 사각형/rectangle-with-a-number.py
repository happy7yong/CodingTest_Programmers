n = int(input())

def din_rect(n) :
    cnt=0

    for i in range(n) :
        for j in range(n) :
            cnt+=1
            cnt%=10
            if cnt == 0 :
                cnt+=1
            print(cnt,end=" ")
        print()

din_rect(n)