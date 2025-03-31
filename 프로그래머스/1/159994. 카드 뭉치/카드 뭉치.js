function solution(cards1, cards2, goal) {
    let answer = "No";
    let goal_ori = [...goal]
    
    //1. shift사용 하여 각 card1, card2 
    for(let i=0;i<goal_ori.length;i++){
        if(goal[0]==cards1[0]){ //항상 goal[0]과 비교
            cards1.shift()
            goal.shift()
        }else if(goal[0]==cards2[0]){
            cards2.shift()
            goal.shift()
        }
        console.log("goal :" + goal, "cards1 :" + cards1, "cards2 :" + cards2)
    }
    
    if(goal.length==0){
        answer =  "Yes"
    }
    return answer;
}