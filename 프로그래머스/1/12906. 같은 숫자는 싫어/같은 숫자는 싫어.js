function solution(arr)
{
    var answer = [];
    var answerRep = 0;
    for(let i=0;i<arr.length;i++){
                if((arr[i]!=answer[answer.length-1]) || (answer.length==0)){
                    answer.push(arr[i]);
                }
    }
    
    return answer;
}