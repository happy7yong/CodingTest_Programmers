function solution(sides) {
    var stack_sides = []
    let sMax = Math.max(...sides);
    let sMin = Math.min(...sides);
    let sides_sum = sides.reduce((acc,cur)=>acc+cur)
    
    //sides에 큰 변이 있을 경우
    for(let i=1;i<=sMax;i++){
        if(sMin+i>sMax){
            stack_sides.push(i)
            console.log(i)
        }
    }
    
    //나머지 한 변이 큰변일 경우
    for(let i=sides_sum-1;i>sMax;i--){
        stack_sides.push(i)
        console.log(i)
    }
  
    return stack_sides.length;
}