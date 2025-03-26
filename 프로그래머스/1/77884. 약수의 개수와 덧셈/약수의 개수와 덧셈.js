function solution(left, right) {
    var sum = 0;
    for(let i=left;i<=right;i++){
        let count=0;
        for(let j=1;j<=i;j++){
            if(i%j===0){
                count++
            }
        }
        console.log(i,count)
        if(count%2==0){
            sum+=i 
        }else{
            sum-=i  
        }
    }
    
    return sum;
}