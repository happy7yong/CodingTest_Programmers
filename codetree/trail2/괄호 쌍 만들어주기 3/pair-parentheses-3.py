inputStr =list(map(str,input()))

#문자열안에 괄호 쌍 만들어주기

cnt = 0

for idx,ele in enumerate(inputStr) :
    if "(" == ele :
        for j in range(idx,len(inputStr)) :
            if ")" == inputStr[j] :
                cnt+=1

print(cnt)