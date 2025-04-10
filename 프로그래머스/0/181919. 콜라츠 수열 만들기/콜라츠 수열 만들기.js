function solution(n) {
    var answer = [];
    let value = 0;
    
    while(n != 1){
        answer.push(n);
        if(n%2==0){
            n/=2
        }else{
            n=3*n+1
        }
    }
    answer.push(n);
    
    return answer;
}