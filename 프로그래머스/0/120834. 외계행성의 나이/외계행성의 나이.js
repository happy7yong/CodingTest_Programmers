function solution(age) {
    var answer = '';
    var age_arr = age_arr=age.toString().split("");
    
    for(let i=0;i<age_arr.length;i++){
        switch (age_arr[i]) {
            case "0" :
                age_arr[i]="a"
                break;
            case "1" :
                age_arr[i]="b"
                break;
            case "2" :
                age_arr[i]="c"
                break;
            case "3" :
                age_arr[i]="d"
                break;
            case "4" :
                age_arr[i]="e"
                break;
            case "5" :
                age_arr[i]="f"
                break;
            case "6" :
                age_arr[i]="g"
                break;
            case "7" :
                age_arr[i]="h"
                break;
            case "8" :
                age_arr[i]="i"
                break;
            case "9" :
                age_arr[i]="j"
                break;
        }   
    }
    
    answer=age_arr.join("")
    return answer;
}