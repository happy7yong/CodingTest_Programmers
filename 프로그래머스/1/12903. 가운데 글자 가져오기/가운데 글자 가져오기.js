function solution(s) {
    var center = Math.ceil(s.length/2) 
    var answer = s.length%2==0 ? s[center-1]+s[center] : s[center-1]
    return answer;
}