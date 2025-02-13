function solution(num, k) {
    
    return num.toString().indexOf(k)<0 ? -1 : num.toString().indexOf(k)+1;
}