#어떤 문제인가? 연속해서 괄호 두개씩 만들수있는 서로 다른 가지 수 
#내가 어떤 행동을 할 수 있지? (를 발견하면 (가 있는지 확인하고 있다면 ))를 확인한다.
#반복 조건은? (를 하나씩 확인 
#제외 조건은? 다음 (가 있을때만 확인한다
#사용할 반복문? (를 확인하고 ))를 확인한다.

input_str = list(input())
n= len(input_str)
cnt=0

for idx in range(n) :
    if idx < n-1 and (input_str[idx] == "(" and input_str[idx+1] == "(") :
        for findIdx in range(idx,n) :
            if findIdx < n-1 and (input_str[findIdx] == ")" and input_str[findIdx+1] == ")") :
                cnt+=1

print(cnt)



