function solution(n) {
    var answer = [];
    var str =n.toString();
    answer=str.split("");
    for(let i=0;i<str.length;i++){
        answer[i]=parseInt(answer[i]);
    }
    answer.reverse();
    
    return answer;
}