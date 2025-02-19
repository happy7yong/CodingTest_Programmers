function solution(n) {
    let answer = [];
    for(let i=0; i<n ; i++){
        i%2==0?answer[i]="수" : answer[i]="박"
    }
    return answer.join("");
}