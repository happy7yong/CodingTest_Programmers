class Solution {
    fun solution(s: String): String {
        var arr = s.split(" ").map{it.toString().toInt()}.toList(); //문자열에서 숫자로 변환
        
        var MaxNum = arr.maxOrNull()
        var MinNum = arr.minOrNull()
        
        var answer = listOf(MinNum,MaxNum).joinToString(" ");
        return answer
    }
}