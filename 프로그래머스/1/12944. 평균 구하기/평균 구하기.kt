class Solution {
    fun solution(arr: IntArray): Double {
        
        var ain=0;
        
        for( a in arr){
            ain+=a;  
            
        }
        
        var answer=ain.toDouble()/arr.size;
        
        
        
        return answer
    }
}