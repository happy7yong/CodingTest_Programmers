n = int(input())
#블럭을 넣었음
blocks = [int(input()) for _ in range(n)]

#뺄 범위
deleted = [tuple(map(int, input().split())) for _ in range(2)]

#temp 배열을 만들어서 사용하라?
temp=[]
temp2= []

cnt=0

#뺄범위에 따라 우선 빼볼까
for s,e in deleted :
    s-=1
    e-=1
    cnt+=1

    if cnt==1 :
        for idx in range(len(blocks)) :
            if s<=idx and idx<=e :
                continue
            
            temp.append(blocks[idx])
    elif cnt == 2 :
        for idx in range(len(temp)) :
            if s<=idx and idx<=e :
                continue
            
            temp2.append(temp[idx])

print(len(temp2))
print("\n".join(map(str,temp2)))
