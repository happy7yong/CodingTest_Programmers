function solution(a, b) {
    var n=a<b ? b : a
    for(let i=1;i<=n;i++){
        if(a%i==0 && b%i==0){
            a=Math.ceil(a/i);
            b=Math.ceil(b/i);
        }
    }
    
    for(let i=0;i<n;i++){
        if(b%2==0){
            b=Math.ceil(b/2)   
        }else if(b%5==0){
            b=Math.ceil(b/5)
        }
    }
    
    return b==1?1:2;
}