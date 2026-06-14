n = int(input())
start="A"
end="Z"
startAlp = ord(start)
endAlp = ord(end)

sum=startAlp


for i in range(n) :
    for _ in range(i) :
        print(" ",end=" ")

    for _ in range(n-i) :
        print(chr(sum),end=" ")
        sum+=1
        if sum>endAlp :
            sum=startAlp
    print()