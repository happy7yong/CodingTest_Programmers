function solution(d, budget) {
    var answer = 0;
    d.sort((a,b)=>a-b)
    for (const item of d){
        budget-=item
        console.log(budget, item)
        if(budget<0){
            break;   
        }
        answer+=1
    }
        
    return answer;
}