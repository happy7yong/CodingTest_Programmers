function solution(myString) {
    var answer = [];
    answer = myString.split("x")
    answer = answer.map(num=>num.length)
    return answer;
}