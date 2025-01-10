function solution(arr) {
    var answer = 0;
    let ain=0;
    
    for(let a of arr){
        ain += a;
    }
    
    answer= ain /arr.length;
    
    return answer;
}