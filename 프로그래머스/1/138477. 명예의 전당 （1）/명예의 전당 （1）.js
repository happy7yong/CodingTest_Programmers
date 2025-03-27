function solution(k, score) {
    var hall = [];
    var finalScore = [];
    
    for(let day=0;day<score.length;day++){
        //명예의 전당에 숫자 넣기
        hall.push(score[day])
        
        hall.sort((a,b)=>b-a)
        if(hall.length>k){
            hall.pop()
        }
        finalScore.push(Math.min(...hall))
    }
    return finalScore;
}