function number(depth,numbers, target, num,count){
    if(numbers.length === depth){
       //리프노드 : 리프노드를 루프까지 어떻게 가져올건지 
        if (num == target){ return 1;}else{return 0;}
    }
    
    let minus = number(depth+1,numbers,target,num-numbers[depth],count);
    let plus = number(depth+1,numbers,target,num+numbers[depth],count)
    
    return minus + plus;
}


function solution(numbers, target) {
    let depth=0;
    return number(depth,numbers, target,0,0);
}