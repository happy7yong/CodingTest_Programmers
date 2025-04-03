function solution(str_list, ex) {
    var answer = '';
    return str_list.filter(num=>!num.includes(ex)).join("");
}