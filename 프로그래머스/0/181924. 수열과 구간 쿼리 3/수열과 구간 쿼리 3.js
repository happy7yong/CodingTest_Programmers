function solution(arr, queries) {
    var answer = [...arr];
    for (let [start, end] of queries){
        var yet = answer[start]
        answer[start]=answer[end]
        answer[end]=yet
    }
    return answer;
}