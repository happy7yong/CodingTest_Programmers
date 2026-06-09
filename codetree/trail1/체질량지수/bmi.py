A,B = map(int,input().split())

def BMI(h,w):
    return (10000*w)//(h*h)

answer = BMI(A,B)
print(answer)

if answer >= 25 :
    print("Obesity")