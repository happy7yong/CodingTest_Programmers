function solution(s) {
    let count = 0;
    let lengthGap = 0;
    let zeroFilter = []; //0제거 String
    var lengthBinary = s;
        //[...s].filter(num => num!=0 ).join(""); //0으로 필터된 값을 길이로 바꾸고 2진수로 나타냄.
    
    while(lengthBinary!=1){
        zeroFilter = [...lengthBinary].filter(num => num!=0 ) //string으로 오면 0 필터
        lengthGap += lengthBinary.length - zeroFilter.length
        lengthBinary = zeroFilter.length.toString(2); //길이를 2진수로 바꿔서 STring
        count++
    }
    
    return [count,lengthGap];
}