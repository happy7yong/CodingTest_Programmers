a, b = map(int, input().split())

#25를 더하고 작은 수에는 2를 곱하여 저장한 후 출력
def program(a,b) :
    if(a>b):
        b*=2
        a+=25
    else :
        b+=25
        a*=2
    return a,b


a,b = program(a,b)
print(a,b)