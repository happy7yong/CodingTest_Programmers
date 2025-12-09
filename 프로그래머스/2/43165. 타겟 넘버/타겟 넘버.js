//DFS 백트래킹

function dfs(index, numbers, sum, target, count){
    //1. 종료 조건 = 트리의 끝
    if(index === numbers.length){
        //리프노드
        return target == sum ? 1 :0 
    }
        
    //2. 분기점 
    const minus = dfs(index+1, numbers, sum - numbers[index], target, count)
    const plus = dfs(index+1, numbers, sum + numbers[index], target, count)
    
    return minus + plus
    
} 

function solution(numbers, target) {
    //target : 되어야하는 값
    //numbers : 그래프
    
    let sum = 0;
    let index = 0;
    let count = 0;
    return dfs(index, numbers, sum, target, count);
}