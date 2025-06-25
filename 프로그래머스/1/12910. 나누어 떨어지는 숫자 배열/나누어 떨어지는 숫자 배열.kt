class Solution {
    fun solution(arr: IntArray, divisor: Int): IntArray {
        var answer = arr.filter{it%divisor==0}.toIntArray()
        answer.sort()
        var emptyanswer = intArrayOf(-1)
        return if (answer.isEmpty()) emptyanswer else answer
    }
}