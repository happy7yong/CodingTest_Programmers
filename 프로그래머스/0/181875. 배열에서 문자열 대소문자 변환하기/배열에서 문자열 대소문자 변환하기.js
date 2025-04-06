function solution(strArr) {
    var answer = [];
    answer = strArr.map((num,index)=>{
        return index%2==0 ? num.toLowerCase() : num.toUpperCase();
        
    })
    return answer;
}