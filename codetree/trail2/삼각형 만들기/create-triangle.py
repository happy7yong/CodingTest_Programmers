n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

#사각형 구하기 인듯 
#ijk 점으로 사각형 구하기 
#최대 넓이
max_val = 0

#-가 나올수도 있어서 offset 필요함.

#사각형 구하기 
def get_max(i,j,k) :
    selected = [points[i],points[j],points[k]]

    max_width = 0
    max_height = 0

    #세 점끼리 모두 비교 
    for idx in range(3) :
        for jdx in range(idx+1, 3) :
            x1,y1 = selected[idx]
            x2,y2 = selected[jdx]

            #y가 같으면 직선
            if y1 == y2 :
                max_width = max(max_width,abs(x1-x2))
                

            #x가 같으면 직선
            if x1 == x2 :
                max_height = max(max_height,abs(y1-y2))

    return max_width * max_height


#3개를 선택했음 (i,j,k)
for i in range(n) :
    for j in range(i+1,n) :
        for k in range(j+1,n) :
            seq = get_max(i,j,k)
            max_val = max(max_val,seq)

print(max_val)