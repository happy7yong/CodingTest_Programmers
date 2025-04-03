function solution(myString, pat) {
    var answer = 0;
    return myString.toUpperCase().includes(pat.toUpperCase())?1:0;
}