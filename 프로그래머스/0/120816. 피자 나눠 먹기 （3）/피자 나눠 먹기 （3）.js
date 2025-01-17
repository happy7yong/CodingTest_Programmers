function solution(slice, n) {
    var result = 0;
    result+=Math.floor(n/slice);
    if(n%slice>0){
        result+=1;
    }
    return result;
}