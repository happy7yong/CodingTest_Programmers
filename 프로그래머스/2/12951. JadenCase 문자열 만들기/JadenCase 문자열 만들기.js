function solution(s) {
    var answer = s.toLowerCase().split(" ")
    
    for(let i=0;i<answer.length;i++){ 
        if(/^[A-Za-z]$/.test(answer[i][0])){
            answer[i] = answer[i][0].toUpperCase() + answer[i].slice(1) }
    }
    return answer.join(" ");
}