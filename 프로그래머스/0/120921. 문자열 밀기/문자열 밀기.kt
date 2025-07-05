class Solution {
    fun solution(A: String, B: String): Int {
        var answer: Int = 0
        var A_len = A.length
        
        for(i in 0 until A_len){
            var A_sub = A.substring(A_len-i)+A.substring(0,A_len-i)
            println(A_sub)
            if(A_sub==B){
                return i
            }
        }
        return -1
    }
}