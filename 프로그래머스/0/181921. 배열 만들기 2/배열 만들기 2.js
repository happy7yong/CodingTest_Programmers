function solution(l, r) {
    //l보다 r 중간 값 중 5과 0으로만 이루어진 숫자
    
    //r보다 큰 값이 나올때까지 만듬 
    
    //r의 자릿수 확인하기 2자리면 2*2 3자리면 2*2*2
    //한자리에 두가지의 경우가 올수 있음. num에 있는 요소
    //경우의 모든 숫자 만들어놓고 filter로 돌리기 
    const num = ["0", "5"]; 
    let rStringLen = [...(r.toString())].length//자릿수 

    let caseNum = [""];
    
    
    for(let numEle=0; numEle<rStringLen; numEle++){ //자릿수만큼 반복 -> 증가
        caseNum = caseNum.flatMap(it=>num.map(i=>it+i))
    }
    
    caseNum = caseNum.map(Number)//모든 문자열을 숫자로 바꿔줌
    //이제 l과 r 범위 안에 있는 것만 filter
    caseNum = caseNum.filter(it=>it>=l && it<=r)
    
    console.log(caseNum)
    return caseNum.length==0?[-1]:caseNum
}