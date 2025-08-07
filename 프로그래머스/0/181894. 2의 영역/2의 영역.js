function solution(arr) {
    var answer = [];
    //slice로 해야할것같음 
    let first2 = arr.indexOf(2)
    let last2 = arr.lastIndexOf(2)
    
    answer = arr.slice(first2,last2+1)

    return answer.length==0?[-1]:answer;
}