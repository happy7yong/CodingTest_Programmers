class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        String[] myStr = my_string.split("");
        for(String apb :myStr){
            answer += apb.repeat(n);
        }
        return answer;
    }
}