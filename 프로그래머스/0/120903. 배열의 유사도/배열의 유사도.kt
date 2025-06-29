class Solution {
    fun solution(s1: Array<String>, s2: Array<String>): Int {
        var count: Int = 0
        s1.forEach{s1_i->
            if(s2.any{s2_i -> s1_i == s2_i})
                count++
        }
        return count
    }
}