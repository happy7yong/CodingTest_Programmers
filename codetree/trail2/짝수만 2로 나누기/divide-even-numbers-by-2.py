n = int(input())
arr = list(map(int, input().split()))

def even_div(arr) :
    for index,ele in enumerate(arr) :
        if ele%2==0 :
            arr[index] = ele//2
            

even_div(arr)

print(" ".join(map(str,arr)))