n = int(input())
max_val = n

def print_deci(n):
    #재귀함수는 무조건 종료조건이 필요하다.
    if n==0:
        print()
        return 
    
    print(max_val-n+1,end=" ")#얕은것부터
    print_deci(n-1)
    print(max_val-n+1,end=" ")#깊은것부터

print_deci(n)