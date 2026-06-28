a, b = map(int, input().split())
n = input()
arr = list(map(int,list(n)))
arr_b_digit = []

#예) 2진수에서 4진수로 바꾸기
#예) 2 -> 10 -> 4

def digit_int(a,arr):
    sum = 0
    i = len(arr)-1
    for ele in arr :
        sum+=ele*(a**i)
        i-=1
    return sum

def int_digit(n) :
    while n > 0 :
        arr_b_digit.append(n%b)
        n//=b
    
        

answer_int = digit_int(a,arr)
int_digit(answer_int)

print("".join(map(str,arr_b_digit[::-1])))