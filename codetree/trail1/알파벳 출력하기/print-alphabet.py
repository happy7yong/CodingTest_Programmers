n = int(input())
start = "A"
end="Z"
endAlp = ord(end)
startAlp = ord(start)
sum = ord(start)


for i in range(1,n+1) :
    for j in range(i) :
        alp=chr(sum)
        print(alp,end="")
        sum+=1
        if sum>endAlp :
            sum=startAlp
    print()