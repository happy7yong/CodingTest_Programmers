function solution(arr, k) {
    var answer = [];
    if(k%2==0){
        answer = arr.map((num)=>num+k)
    }else{
        answer = arr.map((num)=>num*k)
    }
    return answer;
}