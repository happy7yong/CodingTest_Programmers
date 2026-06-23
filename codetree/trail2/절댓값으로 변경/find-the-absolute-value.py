n = int(input())
arr = list(map(int, input().split()))

def adc(arr):
    arr = [ ele*(-1) if ele < 0 else ele for ele in arr]
    return arr

arr = adc(arr)

print(" ".join(map(str,arr)))