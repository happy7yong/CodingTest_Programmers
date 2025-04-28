function solution(myString) {
    var answer = [];
    answer = myString.split("x")
    return answer.filter(num=>num.length!=0).sort();
}