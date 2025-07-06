class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {
        
        val total = brown + yellow 
        //brown은 테두리 
        //테두리=brown의 특징 
        //가로*2+세로*2-4 =
        //가로 세로 조건 1. total의 값이 나와야됨.즉 약수값중있음 2. 가로*2+세로*2-4=
        for(i1 in 1 .. total){
            if(total%i1==0){//약수
                var i2:Int=total/i1
                if((i2*2+i1*2)-4==brown){
                    var answer = intArrayOf(i2,i1)
                    return answer
                    
                }
            
            }
        }
        
        return intArrayOf()
    }
}
