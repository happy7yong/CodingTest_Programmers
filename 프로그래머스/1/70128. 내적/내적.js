function solution(a, b) {
    var sum = 0;
    for(let i=0;i<a.length;i++){
        sum += a[i]*b[i]
        console.log(sum)
        
    }
    return sum;
}