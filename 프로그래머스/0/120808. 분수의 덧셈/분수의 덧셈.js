function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    var numer_total=0
    var denom_total=0
    var gcd = 1; //최대공약수
    //분자
    numer1*=denom2
    numer2*=denom1
    numer_total=numer1+numer2
    
    //분모
    denom_total=denom1*denom2
    
    //약수
    for(let i=1;i<denom_total+numer_total;i++){
        if((numer_total%i==0)&&(denom_total%i==0)){
            gcd=i;
        }
    }
    
    
    
    answer=[numer_total/gcd,denom_total/gcd]
    return answer;
}