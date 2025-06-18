class Solution {
    fun solution(n: Int): Int {
        var answer = n.toString().map{it.toString().toInt()}.reduce{ rec,acc ->rec+acc}

        return answer
    }
}