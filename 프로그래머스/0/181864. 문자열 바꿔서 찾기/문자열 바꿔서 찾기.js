function solution(myString, pat) {
    var answer = 0;
    
    let Str = [...myString].map(_=>_=="A"?"B":_=="B"?"A":"B").join("");
    return Str.includes(pat)? 1: 0 ;
    return 0;
}