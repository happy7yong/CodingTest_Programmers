n,m = map(int,input().split())

arr_1 = [list(map(int,input().split())) for _ in range(n)]
arr_2 = [list(map(int,input().split())) for _ in range(n)]
arr_answer = [[0 if arr_1[i][j]==arr_2[i][j] else 1 for j in range(m)] for i in range(n) ]

print("\n".join(" ".join(map(str,row)) for row in arr_answer))

