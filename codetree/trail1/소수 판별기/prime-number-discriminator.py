n=int(input())
plug=False

for i in range(2,n):
    if n%i==0 :
        plug=True

print("P" if not plug else "C")

    