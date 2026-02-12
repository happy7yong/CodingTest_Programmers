function solution(citations) {
    var answer = 0;
    
    const n = citations.length;
    let citationsH = [];
    
    //n: 1~citation.length
    //인용 : 0~citation의 최댓값까지 가능
    //1. n편 중 i편의 논문은 i회 이상 인용 나머지 (n-i)편의 논문이 i이하 인용되었을 때, 
    //0 1 3 5 6 //각요소는 인용횟수
    
    //1. citations.length 중 i편의 논문은 i(citations의 요소 == i)회 인용했음.
    //i 조건 : i<=citations.length
    //2. citations.length-i편의 논문 <= i회 인용
    
    citations.sort((a,b)=>b-a); //내림차순으로 정렬 
    
    for(let i=0;i<n;i++){
        if(citations[i] >= i+1) answer = i+1
        
    }
    return answer;
}