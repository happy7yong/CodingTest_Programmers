function solution(my_string) {
    var answer = [];
    answer = [...my_string].map(Number).filter(num => isNaN(num)==false).sort()
    return answer;
}