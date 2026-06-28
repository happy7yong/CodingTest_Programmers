N = input()

arr = list(map(int,list(N)))
arr_2 = []

def int_digit(arr,number):
    n=len(arr)-1
    sum=0
    for i in arr :
        sum+=i*number**n
        n-=1
    return sum

def int_2(n) :
    while n > 0 :
        arr_2.append(n%2)
        n//=2

int2 = int_digit(arr,2)*17
int_2(int2)

print("".join(map(str,arr_2[::-1])))