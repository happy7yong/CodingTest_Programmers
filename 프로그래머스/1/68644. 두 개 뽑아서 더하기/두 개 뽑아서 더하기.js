function solution(numbers) {
    var SumValue = [];
    numbers.sort((a,b)=>b-a)
    for(let i=0;i<numbers.length;i++){
        for(let j=i+1;j<numbers.length;j++){
            let element = numbers[j]+numbers[i]
            SumValue.push(element);
        }
    }
    
    let setSum = [...new Set(SumValue)].sort((a,b)=>a-b)
    return setSum;
}