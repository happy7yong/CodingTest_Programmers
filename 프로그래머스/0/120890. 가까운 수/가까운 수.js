function solution(array, n) {
    var answer = [];
    array=array.sort((a,b)=>a-b)
    for(let i=0;i<array.length;i++){
        answer[i]=Math.abs(n-array[i])
    }
    var min = answer[0];
    var sum = array[0]
    
    for(let i=1;i<array.length;i++){
        if(min>answer[i]){
            min=answer[i]
            sum=array[i]
        }
    }
    
    return sum;
}