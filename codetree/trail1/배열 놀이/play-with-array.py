n,q = list(map(int,input().split()))

elements = list(map(int,input().split()))
e2=0

for _ in range(q) :
    inputList = list(map(int,input().split()))# com e s
    com = inputList[0]
    if com == 1 :
        e=inputList[1]
        print(elements[e-1])
    elif com == 2:
        e=inputList[1]
        if e in elements :
            print(elements.index(e)+1)
        else :
            print("0")
    elif com == 3:
        e=inputList[1]-1
        s=inputList[2]
        arr=[]
        for ele in elements[e:s:] :
            arr.append(ele)
        print(" ".join(map(str,arr)))

