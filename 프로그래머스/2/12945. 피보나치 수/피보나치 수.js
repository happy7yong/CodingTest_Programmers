function solution(n) {
    var answer = 0;
    let fib = []; //저장할 배열
    fib[0] = 1;
    fib[1] = 1;
    
    for(let i=2;i<n;i++){
        fib[i]=fib[i-1]+fib[i-2];
        fib[i]%=1234567
    }
    
    return fib[fib.length-1];
}