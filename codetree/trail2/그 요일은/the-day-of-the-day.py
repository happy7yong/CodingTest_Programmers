m1, d1, m2, d2 = map(int, input().split())
A = input()

numsOfMonth = [0,31,29,31,30,31,30,31,31,30,31,30,31]
dayOfTheWeek = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

m1sumDays = d1
m2sumDays = d2

for i in range(1,m1) :
    m1sumDays+=numsOfMonth[i]

for i in range(1,m2) :
    m2sumDays+=numsOfMonth[i]

gap = m2sumDays - m1sumDays

#한바퀴 모두 돌았을때 7로 나누는 것임.
answer=gap//7

for idx,day in enumerate(dayOfTheWeek) :
    if A == day :
        if idx <= gap%7 :

            answer+=1

print(answer)