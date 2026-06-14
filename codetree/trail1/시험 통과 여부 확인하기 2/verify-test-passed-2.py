n = int(input())
stu_cnt=0

#한번 돌때마다 한 학생의 4가지 시험 점수
for _ in range(n) :
    stu_list = list(map(int,input().split()))
    sum_val = sum(stu_list)
    len_val = len(stu_list)
    avg = sum_val/len_val

    if avg >= 60 :
        print("pass")
        stu_cnt +=1
    else :
        print("fail")

print(stu_cnt)