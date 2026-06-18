arr_1 = [ list(map(int,input().split())) for _ in range(3)]
input()
arr_2 = [ list(map(int,input().split())) for _ in range(3)]

answer = [[arr_1[i][j] * arr_2[i][j] for j in range(3)] for i in range(3)]

print("\n".join(" ".join(map(str,row)) for row in answer))