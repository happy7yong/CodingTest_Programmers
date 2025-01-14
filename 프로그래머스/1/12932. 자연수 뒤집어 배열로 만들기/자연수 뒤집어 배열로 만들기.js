function solution(n) {
    var answer = [];
    for(let i=0;n>0;i++){
        answer[i]=n%10;
        n=parseInt(n/=10);
    }
    
    return answer;
}