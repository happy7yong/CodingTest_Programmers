function solution(my_string, letter) {
    var answer =  [...my_string].filter(num => num!=letter).join("")
    return answer;
}