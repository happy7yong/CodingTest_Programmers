function solution(order) {
    var count = 0;
    var answer = [...order.toString()].map(Number)
    for(let i=0;i<answer.length;i++){
        if(answer[i]==3 || answer[i]==6 || answer[i]==9){
            count+=1;
        }
    }
    return count;
}