function solution(my_string, m, c) {
    var answer = '';
    for(let i=0;i<Math.ceil(my_string.length/m);i++){
        answer+=my_string[(c-1)+m*i]
    }
    return answer;
}