a, b = map(int, input().split())

def isDecimal(ele) :
    for i in range(2,ele) :
        if ele%i==0 :
            return False
    return True

def print_s(a,b) :
    sum=0
    for i in range(a,b+1) :
        if isDecimal(i) :
            sum+=i
    
    return sum

print(print_s(a,b))