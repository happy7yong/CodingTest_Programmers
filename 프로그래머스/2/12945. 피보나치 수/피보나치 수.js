function solution(n) {
    var fib = [];
    fib[0]=1;
    fib[1]=1;
    
    for(let i=2;i<n;i++){
        fib[i]=fib[i-1]+fib[i-2]
        fib[i]%=1234567
    }
    console.log(fib)
    return fib[n-1];
}