n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

def trigger():
    j = 0  # a의 인덱스

    for i in range(m):  # b의 인덱스
        # a에서 b[i]를 찾을 때까지 j 이동
        while j < n and a[j] != b[i]:
            j += 1

        # 끝까지 갔는데 못 찾음
        if j == n:
            return False

        # 찾았으면 다음 위치부터 다시 탐색
        j += 1

    return True

if trigger():
    print("Yes")
else:
    print("No")