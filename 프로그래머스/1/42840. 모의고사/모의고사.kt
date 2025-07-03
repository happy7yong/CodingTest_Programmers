class Solution {
    fun solution(answers: IntArray): IntArray {
        var count = intArrayOf(0,0,0) //count 저장
        var student:List<IntArray> = listOf(
            intArrayOf(1,2,3,4,5),
            intArrayOf(2,1,2,3,2,4,2,5),
            intArrayOf(3,3,1,1,2,2,4,4,5,5)
        )
        
        //각 자리에 매치해야됨.
        for((index, ele) in answers.withIndex()){
            //answers값이 끝날때까지 돌아, 
            //student값을 돌려
            student.forEachIndexed{ stdIdx, it ->
                if(ele == it[index%it.size])
                    count[stdIdx] ++
            }
        }
        
        var Max = count.maxOrNull()?: 0 //최고 값
        //Max랑 같은 값일 경우 모두 추출 
        
        return count.mapIndexed{index, value -> 
            if(value == Max){
                index+1
            }else null
        }.filterNotNull().toIntArray()
    }
}