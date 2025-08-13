function solution(myString, pat) {
    var count = 0;
    let myStringSlice = myString

    while(myStringSlice.includes(pat)){//못찾을때 까지
        let findIdx = myStringSlice.indexOf(pat); //내가 원하는 문자열 찾음
        count++
    
        myStringSlice = myStringSlice.slice(findIdx+1) //내꺼 찾음 

    }

    return count;
}