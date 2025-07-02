class Solution {
    fun solution(sizes: Array<IntArray>): Int {
        var answer: Int = 0
        //만약 가로길이와 세로길이중 가장 큰 값을 왼쪽에 두기 
        
        //1. 명함 모두 확인하여 각각중 Max값을 가로로 넣기 
        var width:MutableList<Int> = mutableListOf()
        var height:MutableList<Int> = mutableListOf()
        
        for(size in sizes){
            width.add(size.maxOrNull() ?: 0)
            height.add(size.minOrNull() ?: 0)
        }
        println("$width $height")
        
        
        return (width.maxOrNull()?:0)*(height.maxOrNull()?:0)
    }
}