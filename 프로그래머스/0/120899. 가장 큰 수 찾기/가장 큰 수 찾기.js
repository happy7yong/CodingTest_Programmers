function solution(array) {
    var answer = [];
    var sum=0;
    for(let i=0;i<array.length;i++){
        if(sum<array[i]){
            sum=array[i]
            answer[0]=array[i]
            answer[1] = array.indexOf(array[i])
        }
    }
    return answer;
}