arr = [ input() for i in range(10)]
endString = input()
answer_arr=[]

for ele in arr :
    if ele[-1] == endString :
        answer_arr.append(ele)

print("\n".join(answer_arr) if answer_arr else "None")