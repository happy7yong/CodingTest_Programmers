const hpSol = (hp,answer) => {
    if(~~(hp/5)>0){
        answer += ~~(hp/5)
        hp%=5;
    }
    
    if(~~(hp/3)>0){
        answer += ~~(hp/3)
        hp%=3;
    }
    
    answer += hp

    return answer
}

function solution(hp) {
    var answer = 0;
    
    answer = hpSol(hp,answer)
    return answer;
}