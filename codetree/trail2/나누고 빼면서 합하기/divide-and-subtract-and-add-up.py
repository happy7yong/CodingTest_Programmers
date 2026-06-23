n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum=0

#m이 1이 될때까지 홀수면 1을빼고, 짝수면 2로나누는 함수
def oddevenF(m):
    if m%2==0 :
        m//=2
    else :
        m-=1
    return m

#arr의 m번째 원소를 계속 더함. 

while True :
    if m==1 :
        sum+=arr[m-1]

        break;
    sum+=arr[m-1]
    m= oddevenF(m)

print(sum)

