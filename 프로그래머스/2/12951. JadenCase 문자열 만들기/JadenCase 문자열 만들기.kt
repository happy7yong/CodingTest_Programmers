class Solution {
    fun solution(s: String): String {
        var answer = ""
        var str = s.lowercase().split(" ")
        
        //map 사용
        var strArr = str.map{
            if(it.isNotEmpty()) it[0].uppercaseChar() + it.substring(1)
            else it
            
        }
        answer = strArr.joinToString(" ")
        return answer
    }
}