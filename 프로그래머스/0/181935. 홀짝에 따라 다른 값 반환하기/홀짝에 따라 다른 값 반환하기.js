function solution(n) {
    var answer = 0;
    if(n%2!=0){//홀수
        for(let i=1;i<=n;i++){
            if(i%2!=0){
                answer+=i
            }
        }
        
    }else{//짝수
        for(let i=1;i<=n;i++){
            if(i%2==0){
                answer+=i*i
            }
        }
    }
    
    return answer;
}