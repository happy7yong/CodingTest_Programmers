function solution(s) {
    var answer = '';
    return [...s].filter((num)=> s.indexOf(num) == s.lastIndexOf(num)).sort().join("");
}