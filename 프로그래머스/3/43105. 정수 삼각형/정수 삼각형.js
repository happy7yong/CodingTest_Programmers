//경우의 수 가장 많은 것부터 



function solution(triangle) {
    const dp = triangle.map(row=>[...row])
    
    for(let i=triangle.length-2;i>=0;i--){
        for(let j=0;j<triangle[i].length;j++){
            dp[i][j] += Math.max(dp[i+1][j],dp[i+1][j+1]) //조건
        }
    }
    
    //장점 : 조건에 부합하지 않으면 수행하지 않음 
    //-> dp[0][0]가 자식노드 중 큰값이 아닌 노드는 합쳐지지도 않음. 
    
    return dp[0][0];
}