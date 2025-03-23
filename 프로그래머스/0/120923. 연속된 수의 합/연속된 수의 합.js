function solution(num, total) {
    var Average_number = Math.floor(total/num)
    var Successive = new Array(num).fill(Average_number);
    var Rest = total%num
    var count = num-1
    
    for(let i=0;i<Rest;i++){
        Successive[i]++
    }
    Successive.sort((a,b)=>a-b)
    
    for(let i=1;i<=Math.floor(num/2);i++){
        if(num%2!=0 && count>1 ){ //연속수가 홀수일경우
            Successive[Math.floor(num/2)-i]-=i
            Successive[Math.floor(num/2)+i]+=i
        }else if(count>1){ //연속수가 짝술일경우
            console.log(count , num, Successive)
            Successive[(num/2)-1-i]-=i
            Successive[num/2+i]+=i
        }
        
        count-=2
        
    }
    
    return Successive;
}