function solution(sides) {
    var max = 0;
    for(let i=0;i<sides.length;i++){
        if(sides[i] > max){
            max = sides[i]
        }
    }
    var sides_acc = sides.reduce((acc,cur)=>acc+cur)
    var answer = (max < sides_acc - max) ? 1 : 2;
    return answer

}