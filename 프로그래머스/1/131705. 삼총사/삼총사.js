function solution(number) {
    var answer = 0;
    let count = 0;
    
    for(let i=0;i<number.length-2;i++){
        for(let j=i+1;j<number.length-1;j++){
            for(let k=j+1;k<number.length;k++){
                answer=number[i]+number[j]+number[k]
                if(answer==0) count++ 
            }
        }
    }
    return count;
}