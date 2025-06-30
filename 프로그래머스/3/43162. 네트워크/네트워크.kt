class Solution {
    fun solution(n: Int, computers: Array<IntArray>): Int {
        var answer = 0
        var visited=MutableList(n){false} //방문 체크할 배열 생성
        
        var startV = 0
        var count = 0
        visited.forEachIndexed{ Index, it->
            if(!it){
                dfs(computers,visited,Index)
                count++
            }
        }

        
        return count
    }
    
    
    fun dfs(computers:Array<IntArray>,visited:MutableList<Boolean>,currentV:Int){
        visited[currentV] = true//방문했어요.
        println(currentV)
        
        for(neighborV in 0 until computers[currentV].size){
            if(computers[currentV][neighborV]==1 && !visited[neighborV]){//1이면 방문
                dfs(computers,visited,neighborV)
            }
            
        }

        
    }
    
    
}