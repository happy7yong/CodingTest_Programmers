class Solution {
    fun solution(array: IntArray): Int {
        var answer: Int = 0
        array.sort()
        answer=array[(array.size)/2]
        return answer
    }
}