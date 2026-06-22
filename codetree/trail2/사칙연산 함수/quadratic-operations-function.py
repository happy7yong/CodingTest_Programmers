a, o, c = input().split()
a = int(a)
c = int(c)

sum=0

def add(a,c) : return a+c
def subt(a,c) : return a-c
def multip(a,c) : return a*c
def divis(a,c) : return a//c

def isWhatCalc(a,o,c) :
    if o=="+" :
        return add(a,c)
    elif o=="-" :
        return subt(a,c)
    elif o=="/" :
        return divis(a,c)
    elif o=="*" :
        return multip(a,c)
    else :
        return False

if isWhatCalc(a,o,c) :
    print(f"{a} {o} {c} =",isWhatCalc(a,o,c))
else :
    print("False")