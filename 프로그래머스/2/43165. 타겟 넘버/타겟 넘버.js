//DFS 백트래킹

function dfs(start, arr, visited = new Set()){
    
    visited.add(start);
    
    for(const next of arr[start]){
        
    }
    
} 

function solution(numbers, target) {
    var answer = numbers[0];


    dfs(answer,numbers);
    return answer;
}