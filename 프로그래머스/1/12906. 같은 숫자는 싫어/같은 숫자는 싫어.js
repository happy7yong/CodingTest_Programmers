function solution(arr)
{
    var answer = []; //저장할 배열
    answer.push(arr[0]);
    for(let i=1;i<arr.length;i++){
        arr[i] != answer[answer.length-1] ? answer.push(arr[i]) : 0    
    }
    
    return answer;
}