N, B = map(int, input().split())

# 10진수인 정수 N을 B진수로 변경하여 출력

#B진수는 4또는 8
arr = []

while N>0 :
    arr.append(N%B)
    N//=B


print("".join(map(str,arr[::-1])))