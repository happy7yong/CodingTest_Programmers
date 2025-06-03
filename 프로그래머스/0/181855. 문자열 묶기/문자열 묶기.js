function solution(strArr) {
    var answer = 0;
    //문자열의 길이에 따라 문자열 목록을 저장
    let arr = [];
    let arr_leng = [];
    arr[0] = [0];
    
    for(let str of strArr){
        if(!arr[str.length]) arr[str.length]=[];
        arr[str.length].push(str.length)
    }
    console.log(arr)
    arr_leng = arr.map(_=> _.length)
    console.log(arr_leng)
    return Math.max(...arr_leng);
}