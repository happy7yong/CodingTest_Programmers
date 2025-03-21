function solution(score) {
    var score_order=[];
    let score_answer = [];
    
    for(let i=0;i<score.length;i++){
        score_order[i] = score[i].reduce((acc,cur)=>acc+cur)
    }
    
    let score_sum = score_order.slice();
    score_order.sort((a,b)=>b-a)

    
    for(let i=0;i<score_order.length;i++){
        for(let j=0;j<score_sum.length;j++){
            if(score_order[i] == score_sum[j]){
                let index = i+1
                if(score_order[i]==score_order[i-1] && i>0){
                   continue;
                }
                score_answer[j] = index
            }
        }
    }
    console.log("score_order : "+score_order);
    console.log("score_sum : "+score_sum);
    
    
    
    console.log(score_answer)
    return score_answer;
}