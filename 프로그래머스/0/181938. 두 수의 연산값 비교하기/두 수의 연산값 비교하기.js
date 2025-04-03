function solution(a, b) {
    var answer = 0;
    let str=[a,b];
    let strJ = str.join("");
    
    return strJ >= 2*a*b ? parseInt(strJ) : 2*a*b;
}