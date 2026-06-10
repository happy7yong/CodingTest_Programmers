ageA,genderA = input().split()
ageB,genderB = input().split()

if int(ageA) >= 19 and genderA == "M" :
    print(1)
elif int(ageB) >= 19 and genderB == "M":
    print(1)
else :
    print(0)