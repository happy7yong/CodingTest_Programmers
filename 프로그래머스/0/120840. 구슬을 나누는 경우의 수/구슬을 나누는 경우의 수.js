function Sum(num){
    var sum=1;
    for(let i=1;i<=num;i++){
        sum*=i;
    }
    return sum
}

function solution(balls, share) {
    var answer = 1;
    answer = Sum(balls)/(Sum(balls-share)*Sum(share))
    var answer_arr = answer%1 <0.5 ? Math.floor(answer) : Math.ceil(answer)
    return answer_arr;
}