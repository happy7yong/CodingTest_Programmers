function solution(numbers, direction) {
    var answer = [];
    
    for(let i=0;i<numbers.length;i++){
        if(direction == "right"){
            answer[i+1] = numbers[i]
            if(i==numbers.length-1){
                answer[0]=numbers[i]
            }
        }
        if(direction=="left"){
            answer[i-1] = numbers[i]
            if(i==0){
                answer[numbers.length-1]=numbers[0]
            }
        }
    }
    answer.length = numbers.length
    return answer;
}