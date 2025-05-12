class Solution {
    public int solution(int n) {
        int answer = 1;
        int pizza_count = 1;
        
        while((6*pizza_count)%n!=0){
            pizza_count++;
        }
        return pizza_count;
    }
}