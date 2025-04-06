function solution(num_str) {
    var answer = [...num_str]
    return answer.map(Number).reduce((acc,rec)=>acc+rec);
}