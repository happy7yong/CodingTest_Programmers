function solution(number) {
    var answer = 0;
    let sum = [...number].map(Number).reduce((acc,rec)=>acc+rec)
    return sum%9;
}