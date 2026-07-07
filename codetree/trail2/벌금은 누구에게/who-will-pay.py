N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

#N명의 학생이 있고, K번 이상 벌칙받으면 벌금 M번진행
#최초로 K번 이상이 되는 애 
#배열을 학생이라고 했을때, 점점+1로 값을 증가 시켜야겠음
#배열 인덱스 : 학생번호 / 배열 값 : 학생 벌금 받은 횟수 그 횟수가 K이상이 되었을때 

students = [0 for _ in range(N+1)]

ans = -1

for i in student :
    students[i] +=1

    if students[i] >= K:
        ans = i
        break
    
print(ans)

