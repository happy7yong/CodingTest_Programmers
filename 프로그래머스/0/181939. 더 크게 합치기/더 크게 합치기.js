function solution(a, b) {
    var answer = 0;
    let sum = [];
    
    sum.push(a.toString() + b.toString());
    sum.push(b.toString() + a.toString());
    
    return Math.max(sum[0],sum[1]);
}