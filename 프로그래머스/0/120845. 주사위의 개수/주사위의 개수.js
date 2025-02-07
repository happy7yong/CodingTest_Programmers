function solution(box, n) {
    var answer = 0;
    var box_num = []
    for(let j=0;j<=2;j++){
        box[j]=Math.floor(box[j]/n)
    }
    
    answer = box[0]*box[1]*box[2]
    return answer;
}