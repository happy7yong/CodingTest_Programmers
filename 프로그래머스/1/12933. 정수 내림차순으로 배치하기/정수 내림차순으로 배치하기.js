function solution(n) {
    var answer = 0;
    let array = [];
    
    for(let i=0;n>0;i++){
        array[i]=n%10;
        n=~~(n/10);
        
    }
    array.map(Number);
    answer=array.sort((a,b) => b-a);
    answer=parseInt(answer.join(''))
    
    return answer;
}