function solution(my_string, s, e) {
    var answer = '';
    answer = [...my_string.slice(s,e+1)].reverse().join("")
    return my_string.slice(0,s)+answer+ my_string.slice(e+1)

}