const 약수 = (num) => {
    var count =0;
    for(let i=1;i<=num;i++){
        if(num%i==0){
            count+=1
        }
    }
    return count
}

function solution(n) {
    var answer = 0;
    for(let i=1;i<=n;i++){
        if(약수(i)>=3){
            answer+=1;
        }
    }
    return answer;
}