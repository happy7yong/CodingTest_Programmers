import java.util.*;

class Solution {
    public String solution(String my_string) {
        String[] str = my_string.split("");
        String answer = "";
        
        for(int i=str.length-1;i>=0;i--){ 
            answer += str[i];
        }
        
  

        return answer;
    }
}