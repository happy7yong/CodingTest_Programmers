arr = ["apple", "banana", "grape", "blueberry", "orange"]

ch = input()
cnt=0

answer_arr = []

for word in arr :
    if word[2] == ch or word[3] == ch :
        cnt+=1
        answer_arr.append(word)
answer_arr.append(cnt)

print("\n".join(map(str,answer_arr)))