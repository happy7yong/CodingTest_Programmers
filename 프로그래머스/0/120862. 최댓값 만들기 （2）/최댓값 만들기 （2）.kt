class Solution {
    fun solution(numbers: IntArray): Int {
        var answer: Int = 0
        numbers.sort()
        var numOfNumbers = numbers.size
        var numbersFirst = numbers[0]*numbers[1]
        var numbersLast = numbers[numOfNumbers-1]*numbers[numOfNumbers-2]
        
        answer = if(numbersFirst > numbersLast) 
            numbersFirst
        else if(numbersFirst < numbersLast)
            numbersLast
        else
            numbersLast
            
        return answer
    }
}