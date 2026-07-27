a = input()

#유상반조정사
#유형 : 완전탐색
#상태 : 2진법으로 바꿔진 값
#반복기준 : 2진법 숫자 단위 0 1 바꾸며 최댓값일 경우 max에 넣기
#목적 : 2진법으로 주어진 후 한자리만 바꿔 최댓값 구하기
#조건위반/이동조건
#정답갱신시점
#사용할 템플릿 : 자릿수단위로 완전탐색

str=list(map(int,list(a)))

def din(d_list) :
    sum_val = 0
    len_v = len(d_list)-1

    for idx,val in enumerate(d_list) :
        if val == 1 :
            sum_val+=2**(len_v-idx)
    
    return sum_val


max_val = 0
#하나하나씩 숫자01 바꾸기 > 10진법으로 바꾼 후 비교 > 더 크면 max에 넣기

for i in range(len(str)) :
    arr = str[:]
    #정확히 한자리 숫자만 바꾼다.
    arr[i] = 1 if str[i]==0 else 0
    
    max_val = max(din(arr),max_val)

print(max_val)

    
