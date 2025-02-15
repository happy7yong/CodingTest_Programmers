function solution(numbers) {
    var num = numbers.sort((a,b)=>a-b);
    var sum = 0;
    let i=0;
    
    while(numbers.length>i){
        for(let j=0;j<=9;j++){
            num[i]!=j ? sum+=j : i++
        }
    }
    return sum;
}