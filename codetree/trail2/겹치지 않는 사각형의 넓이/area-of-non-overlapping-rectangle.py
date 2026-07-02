offset = 1000
max_val = 2000

arr = [[0 for i in range(max_val+1)] for _ in range(max_val+1)]

rect = [tuple(map(int,input().split())) for _ in range(2)]
m_p = tuple(map(int,input().split()))


#AB에 해당하는 범위를 1로 만든다음
#M에 해당하는 범위를 0으로 만듬
#1 카운트

for x1,y1,x2,y2 in rect :
    x1,y1,x2,y2 = x1+offset,y1+offset,x2+offset,y2+offset

    for y in range(y1,y2) :
        for x in range(x1,x2) :
            arr[x][y] = 1


m_x1,m_y1,m_x2,m_y2 = m_p
m_x1+=offset
m_x2+=offset
m_y1+=offset
m_y2+=offset


for y in range(m_y1,m_y2) :
    for x in range(m_x1,m_x2) :
        arr[x][y] = 0

#1 갯수 세기
cnt=0
for row in arr :
    for ele in row :
        if ele==1 : cnt+=1

print(cnt)

