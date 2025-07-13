function solution(arr, queries) {
    var answer = [];
    
    for(let [start, end, k] of queries){
        var minArr = arr.slice(start,end+1).filter((v)=>v > k) 
        var min = minArr.length == 0 ? -1 : Math.min(...minArr)
        answer.push(min)
    }
    return answer;
}