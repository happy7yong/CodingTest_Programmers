n = int(input())
sequence = list(map(int, input().split()))

sequence_sort = sorted(sequence[:])
#cnt 배열
sequence_sort_arr = []

#정렬된 걸 앞에 인덱스를 기억해두기 
for (index,ele) in enumerate(sequence_sort) :
    sequence_sort_arr.append((index,ele))
    

sequence_index = [0] * n
sequence_sort_tf = [False] * n

for (index,ele) in enumerate(sequence) :
    for (idx, s) in enumerate(sequence_sort) :
        if ele == s and not sequence_sort_tf[idx] :
            sequence_index[index] = idx+1
            sequence_sort_tf[idx] = True
            break
    
print(" ".join(map(str,sequence_index)))
