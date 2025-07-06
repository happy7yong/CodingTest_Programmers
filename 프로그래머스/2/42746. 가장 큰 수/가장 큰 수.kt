class Solution {
    fun solution(numbers: IntArray): String {
        //각 앞자리로 비교할 예정
        //앞자리가 똑같으면 뒷자리 비교 -> 한자리가 부족할 경우
        var numberSort = numbers.sortedWith{ a,b->
            (b.toString()+a.toString()).compareTo(a.toString()+b.toString())
        }
        var answer = numberSort.joinToString("")
        //모든 값이 0일경우
        return if(answer.startsWith("0")) "0" else answer
    }
}