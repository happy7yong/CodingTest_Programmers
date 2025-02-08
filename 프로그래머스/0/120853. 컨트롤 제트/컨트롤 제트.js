function solution(s) {
    var answer = [];
    answer=s.split(" ")
    for(let i=0;i<answer.length;i++){
        if("Z"==answer[i]){
           answer[i-1]=0;
        }
    }
    return answer.filter((num,index)=>"Z"!=num).map(Number).reduce((acc,cur)=>acc+Number(cur));
}