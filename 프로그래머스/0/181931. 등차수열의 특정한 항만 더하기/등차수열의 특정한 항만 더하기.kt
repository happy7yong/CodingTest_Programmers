class Solution {
    fun solution(a: Int, d: Int, included: BooleanArray): Int {
        var sum: Int = 0
        included.forEachIndexed{index, it ->
            if(it) 
                sum+= a+index*d
            
        }
        return sum
    }
}