function solution(money) {
    var answer = [];
    answer[0]=0;
    while(money-5500>=0){

        answer[0]+=1;
        money-=5500;
  
    }
    answer[1]=money
    return answer;
}