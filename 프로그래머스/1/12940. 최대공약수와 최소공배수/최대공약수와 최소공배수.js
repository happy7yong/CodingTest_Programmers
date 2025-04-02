function solution(n, m) {
    var answer = [];
    let GCD = 0;
    let LCM = 0;
    
    for(let i=1;i<Math.max(n,m);i++){
        if(n%i==0 && m%i==0){
            GCD=i;
        }
    }
    console.log(GCD)
    return [GCD,n/GCD*m/GCD*GCD];
}