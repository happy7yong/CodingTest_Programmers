
function solution(n) {
    var answer = [];
    for(let i=2;i<=n;i++){
        while(n%i==0){
            n/=i
            answer.push(i)
        }
    }
    return answer.filter((num,index)=>num!=answer[index+1]).sort((a,b)=>a-b);
}