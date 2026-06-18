arr = [ list(input().split()) for _ in range(5)]

arr_answer = [ [arr[i][j].upper() for j in range(3)] for i in range(5)]

print("\n".join(" ".join(ele) for ele in arr_answer))