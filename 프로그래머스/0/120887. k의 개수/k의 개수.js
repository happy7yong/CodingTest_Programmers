function solution(i, j, k) {
    var answer = 0;
    let k_str = String(k);
    
    for(let n=i;n<=j;n++){
        answer += [...String(n)].filter(_=>_==k).length
    }
    
    
    return answer;
}