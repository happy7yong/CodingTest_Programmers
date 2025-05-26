import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        //String을 toChar로 바꿈 : 정적배열 
        char[] charArray = a.toCharArray();
        for(int i=0;i<charArray.length;i++){
            if(Character.isUpperCase(charArray[i])){ 
                charArray[i] = Character.toLowerCase(charArray[i]);
            }else{
                charArray[i] = Character.toUpperCase(charArray[i]);
            }
        }
        
        //char->String
        System.out.printf(String.valueOf(charArray));
    }
}