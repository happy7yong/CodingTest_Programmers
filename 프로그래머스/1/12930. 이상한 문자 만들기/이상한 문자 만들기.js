function solution(s) {
    var answer = '';//단어별 홀수자리 
    //단어별로 끊어서 -> 하나이상의 공백 문자가 걸림 
    
    let S_split = s.split(' ')
    let S_app = S_split.map(apb=>
        [...apb].map((a,index)=>index%2==0? a.toUpperCase() : a.toLowerCase() ).join("")
    ).join(" ")
    
    return S_app;
}