n = int(input()) 
start="A"
sum=ord(start)

for i in range(1,n+1) :
    for j in range(n) :
        print(chr(sum),end="")
        sum=sum+1
    print()